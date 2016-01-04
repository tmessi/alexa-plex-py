Alexa Plex
==========

Alexa app for interacting with Plex Server and Client.

Setup
-----

Create [virtualenv](https://virtualenv.readthedocs.org/en/latest/) and install
requirements using [pip-tools](https://github.com/nvie/pip-tools).


```bash
virtualenv .pyenv/aplexa
source .pyenv/aplexa/bin/activate
pip install pip-tools
pip-compile requirements.in
pip-sync requirements.txt
```

Then define some environment variables to configure the app by creating a
`.env` file.

```
# Username used to log into plex.tv
PMS_USERNAME=
# Password used to log into plex.tv
PMS_PASSWORD=
# Plex server to access. This is usually the hostname of the server running PMS
PMS_SERVERNAME=
# Plex client to access. THis is usually the hostname of the server running PHT
PMS_CLIENT=
# The id of the Alexa app.
ALEXA_APP_ID=
```

Create an AWS Lambda function named `alexa-plex-py` using the
`alexa-skills-kit-color-expert-python` blueprint. Set the handler to
`aplexa.lambda_handler`. For more info on setting up AWS Lambda functions see
the [AWS Lambda Developer Guide](http://docs.aws.amazon.com/lambda/latest/dg/welcome.html).

Create a new Alexa Skill using the new lambda function, `intent-schema.json`
and `sample-utterances.txt`.  Once created the application id can be found for
the `ALEXA_APP_ID` environment variable listed above.


Configure the `aws` CLI as described in the [AWS Developer
Guide](http://docs.aws.amazon.com/lambda/latest/dg/setup-awscli.html). Then use
the `deploy.sh` script to create a zip and push the code to AWS Lambda.


See also
--------

* [Alexa Skills Kit Docs](https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/developing-an-alexa-skill-as-a-lambda-function)
* [NodeJS Alexa Plex](https://github.com/OverloadUT/alexa-plex)
