from langchain_openai import ChatOpenAI
from dotenv import load_dotenv  

from typing import TypedDict, Annotated

load_dotenv()

class movie(TypedDict):
    summary: Annotated[str, "A Brief summary about the movie"]
    sentiment: Annotated[str, "Give the sentiment of the movie in positive, negative or neutral"]

Model=ChatOpenAI(model='gpt-4')


structured_result=Model.with_structured_output(movie)

result=structured_result.invoke("what is the movie 'the godfather' about?")


print(result)

print(result['summary'])
print(result['sentiment'])