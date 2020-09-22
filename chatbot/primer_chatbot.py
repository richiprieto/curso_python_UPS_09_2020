from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
#from chatterbot.response_selection import get_most_frequent_response
from chatterbot.response_selection import get_first_response
from chatterbot.comparisons import levenshtein_distance
#from chatterbot.filters import get_recent_repeated_responses

chatbot = ChatBot(
    "Chatterbot",
    trainer="chatterbot.trainers.CorpusTrainer",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    database_uri="sqlite:///database.sqlite3",
    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
            "default_response": "Disculpe, no entiendo su pregunta",
            "maximum_similarity_threshold": 0.90,
        }
    ],
    response_selection_method=get_first_response,
    statement_comparison_function=levenshtein_distance,
    read_only=True,
)

trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("./mi_corpus.yml")

# Solo usar para hablar con el chatbot por consola

while True:
    peticion = input("Tu: ")
    respuesta = chatbot.get_response(peticion)
    print("Bot: ", respuesta)
