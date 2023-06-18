# Dependències software (en ubuntu 20.04):
# $> apt install texlive-base texlive-latex-base texlive-latex-extra texlive-lang-spanish texlive-science texlive-bibtex-extra biber

DOC=memoria

pdf:
	pdflatex $(DOC)
	biber   $(DOC)
	pdflatex $(DOC)
	pdflatex $(DOC)

clean:
	rm -f *.pdf *.log *.aux *.out *.toc *.bbl *.blg *.dvi *.lof *.lot *.idx *.bcf *.run.xml *~

