from langchain_openai import ChatOpenAI
from dotenv import load_dotenv  

from typing import TypedDict

load_dotenv()

class movie(TypedDict):
    summary: str
    sentiment: str

Model=ChatOpenAI(model='gpt-4')


structured_result=Model.with_structured_output(movie)

result=structured_result.invoke("what is the movie 'the godfather' about?")


print(result)

print(result['summary'])
print(result['sentiment'])
