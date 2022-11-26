class Reply:
    def __init__(self, msg):
        self.msg = msg


    # def message(self):
    #     r = "Sorry, I don't understand."
    

    #     if self.msg in ['Hello', 'hello']:
    #         r = 'Hi'
    #     elif self.msg == 'I have a question':
    #         r = 'How can I help you?'
    #     elif self.msg == 'Who are you?':
    #         r = 'I am robot'

    #     return r

    def message(self):
        self.msg = self.msg.lower()

        #Bots greeting response
        bot_greetings = ['howdy', 'hi', 'hey', 'hello']
        #User greeting
        user_greetings = ['hi', 'hey', 'hello', 'greetings', 'wassup']

        for word in self.msg.split():
            if word in user_greetings:
                r = random.choice(bot_greetings)
                return r



