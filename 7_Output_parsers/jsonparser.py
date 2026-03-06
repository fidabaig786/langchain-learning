from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv() 

Model = ChatOpenAI(model='gpt-4o-mini')

parser = JsonOutputParser()

# Prompt

template = PromptTemplate(
    template = "give me the name , age and city of a {politician} in json format", 
    input_variables = ["politician"]
)

chain = template | Model | parser

result = chain.invoke({"politician": "Barack Obama"})

print(result)
print(type(result))
