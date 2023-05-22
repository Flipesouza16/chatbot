from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot import languages
languages.ENG.ISO_639_1 = "en_core_web_sm"
import wikipedia
import json
# download(model="en_core_web_sm")
import spacy
from spacy.cli.download import download

with open('config.json', mode='r', encoding="utf-8") as configFile:
    config = json.load(configFile)

list_traning = config['list_greating'] + config['list_programing']

chatbot = ChatBot('Arquiteta')
trainer = ListTrainer(chatbot)

trainer.train(list_traning)

opcoes_sair = config['list_leaving']

def print_welcome():
    message = config['welcome']
    print(message)

def answer_question(question):
    response = chatbot.get_response(question)
    if response.confidence > 0.5:
        return response
    else:
        return search_content(question)

def search_content(text):
    try:
        wikipedia.set_lang("pt")
        content = wikipedia.summary(text, sentences=2)
        return content
    except Exception as e:
        print("Erro ao buscar conteúdo: " + str(e))

def init_architecta():
  is_running = True

  print_welcome()

  while is_running:
    request = input('Você: ')
    
    if(request in opcoes_sair):
        is_running = False

    response = answer_question(request)
    print('Bot: ',response)


if __name__ == '__main__':
    init_architecta()
