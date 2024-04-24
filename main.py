from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from colorama import Fore

load_dotenv()

# Définition du prompt
prompt = ChatPromptTemplate.from_template("raconte moi une blague {topic}")

# Création du modèle OpenAI
model = ChatOpenAI(model="gpt-3.5-turbo")

# Création du parser de sortie pour transformer la réponse en chaîne de caractères
output_parser = StrOutputParser()

# Création du chaînage
chain = prompt | model | output_parser

# Invocation du chaînage avec le sujet spécifique et récupération de la réponse
result = chain.invoke({"topic": "ice cream"})

# Affichage de la réponse en vert
print(Fore.GREEN + result + Fore.RESET)
