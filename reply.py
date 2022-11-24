class Reply:
    def __init__(self, msg):
        self.msg = msg


	def message(self, msg):
        r = "Sorry, I don't understand."
    

        if msg in ['Hello', 'hello']:
            r = 'Hi'
        elif msg == 'I have a question':
            r = 'How can I help you?'
        elif msg == 'Who are you?':
            r = 'I am robot'

        return r