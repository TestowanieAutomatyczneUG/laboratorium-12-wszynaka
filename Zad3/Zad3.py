class Messenger:
    def __init__(self):
        self.template = TemplateEngine()
        self.server = MailServer()

    def send_message(self, email, text):
        if type(email) is str and type(text) is str:
            return self.server.send_message(self.template.make_message(email, text))

    def get_message(self, email):
        if type(email) is str:
            return self.server.get_message(email)

class MailServer:
    pass

class TemplateEngine:
    pass