# vim: set et ts=4 sw=4 fileencoding=utf-8:
'''
alexa
=====
'''


class Response(object):
    '''
    Build an Alexa response
    '''
    def __init__(self,
                 output,
                 title=None,
                 reprompt_text=None,
                 should_end_session=True,
                 session_attributes=None):
        self.output = output
        self.title = title or 'Plex'
        self.reprompt_text = reprompt_text
        self.should_end_session = should_end_session
        self.session_attributes = session_attributes or {}

    def to_dict(self):
        '''
        Convert to expected dict response.
        '''
        return {
            'version': '1.0',
            'sessionAttributes': self.session_attributes,
            'response': {
                'outputSpeech': {
                    'type': 'PlainText',
                    'text': self.output
                },
                'card': {
                    'type': 'Simple',
                    'title': 'Plex - ' + self.title,
                    'content': 'Plex - ' + self.output
                },
                'reprompt': {
                    'outputSpeech': {
                        'type': 'PlainText',
                        'text': self.reprompt_text
                    }
                },
                'shouldEndSession': self.should_end_session
            }
        }
