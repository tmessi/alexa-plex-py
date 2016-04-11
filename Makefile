VE_DIR ?= .build/env
LAMBDA_FUNC_NAME ?= aplexa-plex-py

all: aplexa.zip

deploy: aplexa.zip
	source $(VE_DIR)/bin/activate; aws lambda update-function-code --zip-file fileb://aplexa.zip --function-name $(LAMBDA_FUNC_NAME)

aplexa.zip: requirements.txt .env aplexa.py alexa/*
	cd $(VE_DIR)/lib/python2.7/site-packages; zip -r ../../../../../aplexa.zip *
	zip -r aplexa.zip * .env

requirements.txt: $(VE_DIR)/bin/activate requirements.in
	source $(VE_DIR)/bin/activate; $(VE_DIR)/bin/pip-compile requirements.in
	source $(VE_DIR)/bin/activate; $(VE_DIR)/bin/pip-sync requirements.txt
	touch requirements.txt

$(VE_DIR)/bin/activate: dev_requirements.txt
	test -d $(VE_DIR) || virtualenv $(VE_DIR)
	$(VE_DIR)/bin/pip install -Ur dev_requirements.txt
	touch $(VE_DIR)/bin/activate

clobber: clean
	rm -rf $(VE_DIR)

clean:
	rm -f aplexa.zip

help:
	@echo "Available targets:"
	@echo "  all       - Build .zip"
	@echo "  deploy    - Build .zip and upload to AWS"
	@echo "  clean     - Remove the generated .zip"
	@echo "  clobber   - Remove virtualenv and .zip"
	@echo ""
	@echo "Configuration variables:"
	@echo "  LAMBDA_FUNC_NAME   - Specify an alternative function name for deploy"


.PHONY: all clean clobber deploy help
