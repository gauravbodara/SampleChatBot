# -*- coding: utf-8 -*-
"""
Created on Wed May  9 15:15:50 2018

@author: admin
"""

import nltk

def builtEngines(whichOne):
    if whichOne == 'eliza':
        nltk.chat.eliza.demo()
    elif whichOne == 'iesha':
        nltk.chat.iesha.demo()
    elif whichOne == 'rude':
        nltk.chat.rude.demo()
    elif whichOne == 'suntsu':
        nltk.chat.suntsu.demo()
    elif whichOne == 'zen':
        nltk.chat.zen.demo()
    else:
        print("NO Engine avilable")
    
def myEngine():
    chatPairs = (
            (r"(.*?)Stock Price(.*)",
                ("Today Stock price is 100",
                 "I am unable to find out stock price.")),
            
             (r"(.*?)not well(.*)",
                ("Oh, take care .May be you should visit doctor",
                 "Did you take some medicines?")),
             (r"(.*?)raining(.*)",
                ("Its monsoon season what more do you expect",
                 "yeah its good for farmers")),  
             (r"How(.*?)health(.*)",
                ("I am always healthy",
                 "I am program .I am super healthy")),
              (r".*",
                ("I am good how are you today ? ",
                 "What brings you here")),
              )
              
    def chat():
        print("!"*80)
        print(">>My engine<<")
        print("Talk to the program using normal english")
        print("="*80)
        print("Enter quit when done")
        chatbot=nltk.chat.util.Chat(chatPairs,nltk.chat.util.reflections)
        chatbot.converse()
        
    chat()

if __name__=='__main__':
    builtEngines('eliza')
    print()
    myEngine()            