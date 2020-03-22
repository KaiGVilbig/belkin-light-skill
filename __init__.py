from mycroft import MycroftSkill, intent_file_handler


class BelkinLight(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('light.belkin.intent')
    def handle_light_belkin(self, message):
        self.speak_dialog('light.belkin')


def create_skill():
    return BelkinLight()

