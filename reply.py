class Reply:
    def __init__(self, msg):
        self.msg = msg


    def message(self):
        r = "Sorry, I don't understand."
    

        if self.msg in ['Hello', 'hello']:
            r = 'Hi'
        elif self.msg == 'I have a question':
            r = 'How can I help you?'
        elif self.msg == 'Who are you?':
            r = 'I am robot'

        return r

 