import random

# from newspaper import Article
# import string
# import nltk
# from sklearn.feature_extraction.text import CountVectorizer 
# from sklearn.metrics.pairwise import cosine_similarity 
# import numpy as np
# import warnings
# warnings.filterwarnings('ignore')

# #Download the punkt package
# nltk.download('punkt', quiet = True)

# #Get the article
# article = Article('https://www.mayoclinic.org/diseases-conditions/chronic-kidney-disease/symptoms-causes/syc-20354521')
# article.download()
# article.parse()
# article.nlp()
# corpus = article.text 

# #print(corpus)

# #Tokenization
# text = corpus
# sentence_list = nltk.sent_tokenize(text)  #A list of sentences

# #Print the list of sentences
# #print(sentence_list)

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

    # def index_sort(list_var):
    #     length = len(list_var)
    #     list_index = list(range(0, length))

    #     x = list_var
    #     for i in range(length):
    #         for j in range(length):
    #             if x[list_index[i]] > x[list_index[j]]:
    #                 #swap
    #                 temp = list_index[i]
    #                 list_index[i] = list_index[j]
    #                 list_index[j] = temp

    #     return list_index

    # Create the bots response
    # def bot_rsponse(self):
    #     self.msg = self.msg.lower()
        
    #     sentence_list.append(self.msg)
    #     bot_rsponse = ''
    #     cm = CountVectorizer().fit_transform(sentence_list)
    #     similarity_scores = cosine_similarity(cm[-1], cm)
    #     similarity_scores_list = similarity_scores.flatten()
    #     index = index_sort(similarity_scores_list)
    #     index = index[1:]
    #     reponse_flag = 0

    #     j = 0
    #     for i in range(len(index)):
    #         if similarity_scores_list[index[i]] > 0.0:
    #             bot_rsponse = bot_rsponse+' '+sentence_list[index[i]]
    #             reponse_flag = 1
    #             j = j + 1
    #         if j > 2:
    #             break

    #     if reponse_flag == 0:
    #         bot_rsponse = bot_rsponse+' '+"I apologize, I don't understand."

    #     sentence_list.remove(self.msg)

    #     return bot_rsponse






