from chatterbot import ChatBot
from chatterbot.training.trainers import ChatterBotCorpusTrainer
def response(a):
    
    chatbot = ChatBot("Ron Obvious")
    chatbot.set_trainer(ChatterBotCorpusTrainer)


    chatbot.train("chatterbot.corpus.english")


    b = str(chatbot.get_response(a))
    return b
