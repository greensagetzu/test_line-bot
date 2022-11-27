import random


class Reply:
    def __init__(self,msg):
        self.msg = msg


    def greeting_response(self):

        #Bots greeting response
        bot_greetings = ['Howdy !', 'Hi !', 'Hey !', 'Hello !']
        #User greeting
        user_greetings = ['hi', 'hey', 'hello', 'greetings', 'wassup']

        for word in self.msg.split():
            if word in user_greetings:
                r = random.choice(bot_greetings)
                return r 

    def problem(self):
        user_problems = ['how', 'to', 'learn', 'code', 'coding', 'apps']

        for word in self.msg.split():
            if word in user_problems:
                r = f"Start by typing: 'How to learn coding' on Google."
                return r

    def random_response(self):

        random_list = [
        "Please try writing something more descriptive.",
        "Oh! It appears you wrote something I don't understand yet",
        "Do you mind trying to rephrase that?",
        "I'm terribly sorry, I didn't quite catch that.",
        "I can't answer that yet, please try asking something else."
        ]

        list_count = len(random_list)
        random_item = random.randrange(list_count)

        return random_list[random_item]

   