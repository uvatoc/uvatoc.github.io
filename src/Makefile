###
### Makefile for building and pushing site
###

GITHUB_PAGES_BRANCH=gh-pages
THEME = toc
THEME19 = toc19

MARKDOWN = python3 -m markdown
BASEDIR = .
LATEXDIR = $(BASEDIR)/latex
DOCSDIR = $(BASEDIR)/docs
PAGEDIR = $(BASEDIR)/content/
LATEXIFY = python3 $(LATEXDIR)/utils/latexify.py

html:
	hugo --theme=$(THEME)

f19:
	hugo --config config2019.toml --theme=$(THEME19) --contentDir content19 --layoutDir layouts19 --destination public19
	mv public19 ../f19

f20:
	hugo --config config2020.toml --theme=toc20 --contentDir content20 --layoutDir layouts20 --destination public20
	mv public20 ../f20

f21:
	hugo --config config2020.toml --theme=toc21 --contentDir content21 --layoutDir layouts21 --destination public21
	mv public21 ../f21


develop:
	sleep 1 && echo "Opening local browser..." &&  open http://localhost:1313 &
	hugo server --theme=$(THEME) --buildDrafts --watch

github: html
	cp -r ./docs ./public/
	cp -r ./images ./public/
	cp -r ./public/* ../
	rm -r ./public
	git add -A :/; git commit -m "Rebuilt site" ; git push

toc.sty:
	pandoc --read=markdown+raw_tex --template=./latex/toc.template ./latex/temp-latex.md -o ./docs/test.tex
	echo 'manually extract from test.tex'

pledge.pdf: $(PAGEDIR)/pledge.md
	$(LATEXIFY) $< > $(LATEXDIR)/temp-latex.md
	pandoc --read=markdown+raw_tex --template=$(LATEXDIR)/tocbig.template $(LATEXDIR)/temp-latex.md -o $(DOCSDIR)/$@


%.pdf: $(PAGEDIR)/%.md
	$(LATEXIFY) $< > $(LATEXDIR)/temp-latex.md
	pandoc --read=markdown+raw_tex --template=$(LATEXDIR)/toc.template $(LATEXDIR)/temp-latex.md -o $(DOCSDIR)/$@

%.pdf: $(PAGEDIR)/post/%.md
	$(LATEXIFY) $< > $(LATEXDIR)/temp-latex.md
	pandoc --read=markdown+raw_tex --template=$(LATEXDIR)/toc.template $(LATEXDIR)/temp-latex.md -o $(DOCSDIR)/$@

.PHONY: html clean develop
