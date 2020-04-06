PROJECT := graypy
PACKAGE := python-$(PROJECT)
VERSION := 2.1.0# from graypy/__init__.py
RELEASE := CROC1
MKFILE_DIR := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))

$(PACKAGE).spec: clean
	sed -e 's,@VERSION@,$(VERSION),g' -e 's,@RELEASE@,$(RELEASE),g' $@.in > $@

sources: $(PACKAGE).spec
	tar czf $(PACKAGE)-$(VERSION).tar.gz graypy setup.py setup.cfg README.rst LICENSE

clean:
	rm -f $(PACKAGE).spec

.PHONY: sources clean
