# vim: set et ts=4 sw=4 fileencoding=utf-8:
'''
aplexa
======
'''
from __future__ import print_function

import logging

import dotenv
from getenv import env
from plexapi.myplex import MyPlexUser

from alexa import Response

dotenv.read_dotenv()

logger = logging.getLogger(__name__)
PLEX_USER = MyPlexUser.signin(env('PMS_USERNAME'), env('PMS_PASSWORD'))
PLEX = PLEX_USER.getResource(env('PMS_SERVERNAME')).connect()


def get_welcome_response():
    '''
    Get the welcome response when waiting for more.
    '''
    return Response(
        'Plex is listening..',
        'Welcome',
        should_end_session=False,
    ).to_dict()


def get_on_deck(intent, session):
    '''
    Get the shows on deck.
    '''
    logger.info('get_on_deck intent_name=%s, sessionId=%s',
                intent['name'],
                session['sessionId'])
    return Response('On deck', 'On Deck').to_dict()


def start_movie(intent, session):
    '''
    Start playing a movie.
    '''
    logger.info('start_movie intent_name=%s, sessionId=%s',
                intent['name'],
                session['sessionId'])
    if 'showName' in intent['slots']:
        show = intent['slots']['showName']['value']
        movie = PLEX.library.section('Movies').get(show)
        print(PLEX.clients())
        client = PLEX.client(env('PMS_CLIENT'))
        client.playMedia(movie)
        speech_output = 'Started movie ' + show
    else:
        speech_output = 'No show specified'
    return Response(speech_output, intent['name']).to_dict()


def on_session_started(request, session):
    '''
    Called when the session starts
    '''
    logger.info('on_session_started requestId=%s, sessionId=%s',
                request['requestId'],
                session['sessionId'])


def on_launch(request, session):
    '''
    Called when the user launches the skill without specifying what they want
    '''
    logger.info('on_launch requestId=%s, sessionId=%s',
                request['requestId'],
                session['sessionId'])
    return get_welcome_response()


def on_session_ended(request, session):
    '''
    Called when the user ends the session.

    Is not called when the skill returns ``should_end_session=true``
    '''
    logger.info('on_session_ended requestId=%s, sessionId=%s',
                request['requestId'],
                session['sessionId'])


def on_intent(request, session):
    '''
    Called when the user specifies an intent for this skill
    '''
    logger.info('on_intent requestId=%s, sessionId=%s',
                request['requestId'],
                session['sessionId'])
    intent = request['intent']
    intent_name = request['intent']['name']

    if intent_name == "OnDeckIntent":
        return get_on_deck(intent, session)
    elif intent_name == "StartShowIntent":
        return start_movie(intent, session)
    else:
        raise ValueError("Invalid intent")


def lambda_handler(event, context):  # pylint: disable=unused-argument
    '''
    Main entry point for aws lamba.

    Routes the incoming request based on type. The JSON body of the
    request is provided in the event parameter.
    '''
    event_app_id = event['session']['application']['applicationId']
    logger.info('event.session.application.applicationId=%s', event_app_id)

    if event_app_id != 'amzn1.echo-sdk-ams.app.{}'.format(env('ALEXA_APP_IP')):
        raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])
