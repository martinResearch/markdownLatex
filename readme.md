# Goal

Markdown format does not allow yet to write directly latex equations.
This Python script will parse your markdown file using a regular expression matcher and will generate an image for each markdown image insertion command of the type

	![latex:your_latex_equation](your_image_file_name) 

you just need to run in the shell

	python create_latex_images.py your_markdown_file.md
	
Note: on linux you may have to use

	sudo python create_latex_images.py your_markdown_file.md
for some reason we need sudo to generate png images or we get all white images


**we recommand using svg image files** because

* they give nice vector images without visible pixel aliasing artefacts
* they are in a text format which is **good for versioning** with git or mercurial: as long as you don't change an equation, the corresponding svg get regenerated as you launch the script but as its textual content remains unchanged no change will be detected and commited.
# Installation

the python script calls the executables pdflatex, pdf2svg 
## Windows

install [MiKTeX](https://miktex.org/download)  add the folder C:\Program Files\MiKTeX 2.9\miktex\bin\x64 in your windows PATH environnement variable

## Linux
	
	sudo apt-get install texlive-latex-base

# Examples

## Using PNGs

	![latex:$I(t)=\int_{x=0}^t f(dx) dx$](./images/integral.png) 
	
Gives: 

![latex:$I(t)=\int_{x=0}^t f(dx) dx$](./images/integral.png)

	![latex:\huge $I(t)=\int_{x=0}^t f(dx) dx$](./images/integral2.png) 
	
Gives: 

![latex:I(t)=\huge $\int_{x=0}^t f(dx) dx$](./images/integral2.png)
 

	


## Using SVGs

	![latex:$I(t)=\int_{x=0}^t f(dx) dx$\](./images/integral.svg) 

Gives:

![latex:$I(t)=\int_{x=0}^t f(dx) dx$](./images/integral.svg)

lager size:

	![latex:\huge $I(t)=\int_{x=0}^t f(dx) dx$](./images/integral3.svg)


![latex:\huge $I(t)=\int_{x=0}^t f(dx) dx$](./images/integral3.svg)



	



