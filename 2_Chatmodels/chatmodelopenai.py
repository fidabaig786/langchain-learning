from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

Model=ChatOpenAI(model='gpt-4')

result=Model.invoke("what is the capital of italy")


print(result.content)

