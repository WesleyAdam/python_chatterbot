from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

#wordlist to training a chatbot
conversation = ['olá',
                'como vai?',
                'sim, estou bem. E você?',
                'hoje estou roboticamente inteligente',
                'você é muito elegante',
                'vai se foder']

#create a chatbot
chatbot = ChatBot('Rony')

chatbot.set_trainer(ListTrainer)
chatbot.train(conversation)


response = chatbot.get_response('sabe falar palavrão?')
print(response)
