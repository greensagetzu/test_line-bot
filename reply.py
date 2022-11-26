import random

class Reply:
    

    def __init__(self,msg):
        self.msg = msg


    def greeting_response(self):
        self.msg = self.msg.lower()

        #Bots greeting response
        bot_greetings = ['Howdy !', 'Hi !', 'Hey !', 'Hello !']
        #User greeting
        user_greetings = ['hi', 'hey', 'hello', 'greetings', 'wassup']

        for word in self.msg.split():
            if word in user_greetings:
                r = random.choice(bot_greetings)
                return r + " I am Doc Bot for short. I will answer your question about chronic Kidney Disease. If ypu want to exit, type bye."

    def exit(self):
    	




