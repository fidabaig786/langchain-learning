from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser 

load_dotenv()

Model = ChatOpenAI()
parser = StrOutputParser()
# Prompt1
template1 = PromptTemplate(
    template = "Write a detail report on the {topic}",
    input_variables = ["topic"]
)

# Prompt2
template2 = PromptTemplate(
    template = " write a 3 line summary of the follwoing text {text}",
    input_variables=["text"]
)

chain = template1 | Model | parser | template2 | Model | parser 

result = chain.invoke({"topic": "AI technology" })

print(result)

