PROJECT := graypy
PACKAGE := python-$(PROJECT)
RELEASE := $(shell git describe --abbrev=0 --tags)
MKFILE_DIR := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))

$(PACKAGE).spec:
	sed -e 's,@COMMIT@,$(RELEASE),g' $@.in > $@ 

sources: $(PACKAGE).spec
	git archive --prefix=$(PROJECT)-$(RELEASE)/ --format=tar $(RELEASE) | gzip > $(PACKAGE)-$(RELEASE).tar.gz
