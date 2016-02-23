Alexa Plex
==========

Alexa app for interacting with Plex Server and Client.

Setup
-----

### Create Lambda function

Create an AWS Lambda function named `alexa-plex-py` using the
`alexa-skills-kit-color-expert-python` blueprint. Set the handler to
`aplexa.lambda_handler`. Or use the `aws` CLI:

```bash
aws lambda create-function \
--region us-east \
--function-name alexa-plex-py \
--role arn:aws:iam::account-id:role/lambda_basic_execution  \
--handler aplexa.lambda_handler \
--runtime python2.7 \
--timeout 15 \
--memory-size 512
```

The `aws` CLI will need to be configured as described in the [AWS Developer Guide][3]

For more info on setting up AWS Lambda functions see the [AWS Lambda Developer Guide][4].


### Create new Alexa Skill

Create a new Alexa Skill using the new lambda function `alexa-plex-py`,
`intent-schema.json` and `sample-utterances.txt`.  Once created the application
id can be found for the `ALEXA_APP_ID` environment variable mentioned below.


### Create `.env` file

Define some environment variables to configure the app by creating a `.env` file.

```
# Username used to log into plex.tv
PMS_USERNAME=
# Password used to log into plex.tv
PMS_PASSWORD=
# Plex server to access. This is usually the hostname of the server running PMS
PMS_SERVERNAME=
# Plex client to access. THis is usually the hostname of the server running PHT
PMS_CLIENT=
# The id of the Alexa app. Get this after creating the skill above.
ALEXA_APP_ID=
```


### Deploy the code

After configuring the `aws` CLI, use `make` the zip and push the code to AWS Lambda.

```bash
# make with no args will just create the zip
make

# This will create the zip and upload it.
make deploy

# For more options
make help
```

See also
--------

* [Alexa Skills Kit Docs][5]
* [NodeJS Alexa Plex][6]


[3]: http://docs.aws.amazon.com/lambda/latest/dg/setup-awscli.html
[4]: http://docs.aws.amazon.com/lambda/latest/dg/welcome.html
[5]: https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/developing-an-alexa-skill-as-a-lambda-function
[6]: https://github.com/OverloadUT/alexa-plex
