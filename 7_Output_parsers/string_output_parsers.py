from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

Model = ChatOpenAI()


# Prompt1

template1 = PromptTemplate(
    template= "Write a detail report on the {topic} " ,
    input_variables=["topic"]
)

# Prompt2

template2 = PromptTemplate(
    template= "Write a an 2 line summary on the {text} " ,
    input_variables=["text"]

)

prompt1 = template1.invoke({"topic": "AI in healthcare"})

result =Model.invoke(prompt1) 

prompt2 = template2.invoke({"text": result.content})

result = Model.invoke(prompt2)

print(result.content)





