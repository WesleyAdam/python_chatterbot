from chatterbot import ChatBot
from exception import FarewellReply
# Uncomment this import to training the chatterbot
#from chatterbot.trainers import ChatterBotCorpusTrainer

# Creating a chatbot object
bot = ChatBot('MX31')

# Uncomment this line of code if you want to training the
# chatbot with the corpus data in a specific language
#bot.set_trainer(ChatterBotCorpusTrainer)
#bot.train('chatterbot.corpus.portuguese')

# Dialog looping
while True:
    reply = input('User: ').lower()
    try:
        response = bot.get_response(reply)
        
        # Verifying if user said some farewell phrase to bot
        if reply == 'tchau' or reply == 'até mais':
            raise ReplyError(response)
        else:
            print('MX31: ',response)
    except FarewellReply as f:
        print('MX31: ',f)
        break
