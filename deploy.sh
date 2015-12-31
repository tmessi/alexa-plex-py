#!/bin/bash
echo Build started
rm -rf aplexa.zip
zip -r aplexa.zip * .env
pushd .pyenv/aplexa/lib/python2.7/site-packages
zip -r ../../../../../aplexa.zip *
popd
echo files are ready
echo uploading zip file, please wait...
aws lambda update-function-code --zip-file fileb://aplexa.zip --function-name alexa-plex-py
echo upload is done, exiting.
