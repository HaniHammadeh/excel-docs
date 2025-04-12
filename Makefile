# Minimal Makefile for Sphinx
SPHINXBUILD   = sphinx-build
SOURCEDIR     = source
BUILDDIR      = _build

html:
	$(SPHINXBUILD) -b html $(SOURCEDIR) $(BUILDDIR)/html
