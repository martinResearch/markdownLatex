# This script will parse you readme.md file and create images for each equation found as 
# [latex:your_equation](your_image_file)
#
# we recommand using svg image files as they give nice vectorial images without pixel aliasing
# and they are in a text format which is good for versioning with git or mercurial 
# has the svg text remains unchanged for unchanged euation and thus it avoids pushing again and again the same 
# images on the server of the aleready compile equations each time a new equation is created 
# Martin de La Gorce April 2016

import tempfile
import shutil
import sys
import platform

for arg in sys.argv: 
    print arg

dirpath = tempfile.mkdtemp()
# ... do stuff with dirpath
print 'temporary directory for latex compilation = %s'%dirpath
if len(sys.argv)==1:
    texfile='./readme.md'
elif len(sys.argv)==2: 
    texfile=sys.argv[1]
else:
    raise Exception('wrong number of arguments')
import re

import os

textfilefolder=os.path.dirname(texfile)

def formula_as_file( formula, file, negate=False,header='' ):
    laxtex_tmp_file=os.path.join(dirpath,'tmp_equation.tex')
    pdf_tmp_file=os.path.join(dirpath,'tmp_equation.pdf')
    latexfile = open(laxtex_tmp_file, 'w')
    latexfile.write('\\documentclass[preview]{standalone}')    
    #latexfile.write('\\input{header.tex}') 
    latexfile.write('\\usepackage{wasysym}')  
    latexfile.write('\\usepackage{amssymb}')     
    latexfile.write('\n\\begin{document}')   
    latexfile.write('%s'%formula)
    latexfile.write('\n\\end{document}  ') 
    latexfile.close()

    if platform.system()=='Linux':
		
		cmd='pdflatex -output-directory="%s"  %s'%(dirpath,laxtex_tmp_file)
		print('runing command:%s'%cmd)
		os.system( cmd )
		if file.startswith('https://raw.github.com'):
			file='./'+re.findall(r"""/master/(.*)""", file)[0]   
		file=os.path.join(textfilefolder,file) 
		if file[-3:]=='svg': 
			os.system( 'pdf2svg %s %s'%(pdf_tmp_file,file) )
		elif file[-3:]=='pdf':
			shutil.copyfile(pdf_tmp_file,file)
		else: 		
			cmd='convert -density 100  %s -quality 90  %s'%(pdf_tmp_file,file)
			print('runing command:%s'%cmd)
			os.system(cmd  )

    elif platform.system()=='Windows':

		if file.startswith('https://raw.github.com'):
			file='./'+re.findall(r"""/master/(.*)""", file)[0]    
		file=os.path.join(textfilefolder,file) 
		if file[-3:]=='svg': 
			cmd='latex -output-directory="%s"  %s'%(dirpath,laxtex_tmp_file)
			dvi_tmp_file=os.path.join(dirpath,'tmp_equation.dvi')
			print('runing command:%s'%cmd)
			os.system( cmd )
			cmd='dvisvgm %s -o %s'%(dvi_tmp_file,file)
			print('runing command:%s'%cmd)
			os.system( cmd )
			
			
		elif file[-3:]=='pdf':
			cmd='pdflatex -output-directory="%s"  %s'%(dirpath,laxtex_tmp_file)
			print('runing command:%s'%cmd)
			shutil.copyfile(pdf_tmp_file,file)
		elif file[-3:]=='png':
			cmd='latex -output-directory="%s"  %s'%(dirpath,laxtex_tmp_file)
			dvi_tmp_file=os.path.join(dirpath,'tmp_equation.dvi')
			print('runing command:%s'%cmd)		
			os.system(cmd  )
			cmd='dvipng  %s -o %s'%(dvi_tmp_file,file)
			print('runing command:%s'%cmd)
			os.system(cmd  )
		else:
			raise('extension %s not supported'%file[-3:])
    else:
		raise('unsuported platform %s'%platform.system())

raw = open(texfile)
filecontent=raw.read()

latex_equations= re.findall(r"""[^\t]!\[latex:(.*?)\]\((.*?)\)""", filecontent)
listname=set()
for eqn in latex_equations:        
    if eqn[1] in listname:
        raise Exception('equation image file %s already used'%eqn[1])
        
    listname.add(eqn[1])
    formula_as_file(eqn[0],eqn[1])
    
shutil.rmtree(dirpath)
print 'DONE'
