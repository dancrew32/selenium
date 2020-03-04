VERSION := v0.26.0
ARCH := linux64
FILE = geckodriver-$(VERSION)-$(ARCH).tar.gz

make:
	vim makefile

checkin:
	git add -A && git commit && git push origin master

venv:
	virtualenv -p python3 venv

gecko:
	wget https://github.com/mozilla/geckodriver/releases/download/$(VERSION)/$(FILE) && \
	tar -zxvf $(FILE) && rm $(FILE) \

deps: gecko
	./venv/bin/pip3 install -r requirements.txt

test:
	./venv/bin/python -m unittest discover -s . -p '*_test.py'

shell:
	./venv/bin/ipython

plugin:
	firefox https://addons.mozilla.org/en-US/firefox/addon/selenium-ide/ \
	https://www.seleniumhq.org/selenium-ide/docs/en/introduction/command-line-runner/

side:
	yarn add selenium-side-runner geckodriver && \
	./node_modules/.bin/selenium-side-runner \
	-c "browserName=firefox moz:firefoxOptions.args=[-headless]" test.side

#node:
# wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.2/install.sh | bash &&
# Add to ~/.bashrc
# export NVM_DIR="$HOME/.nvm" \
# [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm \
# [ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion" \
# nvm use --lts

