VERSION := v0.26.0
ARCH := linux64
FILE = geckodriver-$(VERSION)-$(ARCH).tar.gz

make:
	vim makefile

venv:
	virtualenv -p python3 venv

gecko:
	wget https://github.com/mozilla/geckodriver/releases/download/$(VERSION)/$(FILE) && \
	tar -zxvf $(FILE)

deps: gecko
	./venv/bin/pip3 install -r requirements.txt

test:
	./venv/bin/python -m unittest discover -s . -p '*_test.py'
