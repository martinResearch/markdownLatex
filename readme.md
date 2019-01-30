# Goal

Markdown format does not allow yet to write directly latex equations.
This Python script will parse your markdown file using a regular expression matcher and will generate an image for each markdown image insertion command of the type

	![latex:your_latex_equation](your_image_file_name) 

you just need to run in the shell

	python create_latex_images.py your_markdown_file.md
	
In linux you may have to use the sudo command:

	sudo python create_latex_images.py your_markdown_file.md
	
For some reason we need sudo to generate png images or we get all white images

**we recommand using svg image files** because

* they give nice vector images without visible pixel aliasing artefacts
* they are in a text format which is **good for versioning** with git or mercurial: as long as you don't change an equation, the corresponding svg get regenerated as you launch the script but as its textual content remains unchanged no change will be detected and commited.
# Installation

the python script calls the executables pdflatex, pdf2svg and convert
 
## Windows

the script calls the executables pdflatex, latex, dvipng and dvisvgm. 

You can:

 * install [MiKTeX](https://miktex.org/download) 
 * add the folder C:\Program Files\MiKTeX 2.9\miktex\bin\x64 in your windows PATH environnement variable. If you don't the script will look for miktex in C:\Program Files.

At the first run , miktex popup windows will appear to install missing packages.
 
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



# Alternatives
* [Readme2tex](https://github.com/leegao/readme2tex) is a Python script that "texifies" your readme. It takes in Github Markdown and replaces anything enclosed between dollar signs with rendered Latex.
* [latex.codecogs.com](latex.codecogs.com). Renders latex expressions provided in the url:

		![description](https://latex.codecogs.com/svg.latex?\huge&space;$I(t)=\int_{x=0}^t&space;f(dx)&space;dx$)
	
	![description](https://latex.codecogs.com/svg.latex?\huge&space;$I(t)=\int_{x=0}^t&space;f(dx)&space;dx$)


* [Texify](https://github.com/apps/texify) is a GitHub App built on top of readme2tex that automatically takes your markdown files and replaces anything enclosed between dollar signs with rendered LaTeX.

* [KaTeXify](https://github.com/FlorianFranzen/KaTeXify) is a browser plugin to add LaTeX mathematic equation support to GitHub, based on KaTex.

* [GitHub with MathJax](https://chrome.google.com/webstore/detail/mathjax-plugin-for-github/ioemnmodlmafdkllaclgeombjnmnbima) is Chrome extension that renders MathJax expressions.

# Improvements

could write a github app similar to [Texify](https://github.com/apps/texify) but that uses the same syntax as here to include equations in md files (instead of the .tex.md file used in Texify) so that no change appear on the md file in the commit made by the app and one edit the md file as usual.



	



