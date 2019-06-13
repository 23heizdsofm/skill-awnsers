from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG

__author__ = '23heizdsofm'
LOGGER = LOG.create_logger( __name__ )

class SkillAwnsers( MycroftSkill ):

    def __init__( self ):
        super( SkillAwnsers, self ).__init__( name="SkillAwnsers" )
        LOGGER.info( "__init__" )

    @intent_handler( IntentBuilder( "" ).require( "awnsers" ) )
    def handle_awnsers_intent( self, message ):
        LOGGER.info( "responses" )
        self.speak_dialog( "responses", data={} )

def create_skill():
    return SkillAwnsers()
