from langchain_openai import ChatOpenAI
from dotenv import load_dotenv  

from typing import TypedDict, Annotated, Optional

from pydantic import BaseModel, Field

load_dotenv()

class movie(BaseModel):
    key_themes: list[str] = Field(description="The key themes explored in the movie")
    summary: list[str] = Field(description="A brief summary of the movie")  
    pros: Optional[str] = Field(description="The positive aspects of the movie, if any")
    cons: Optional[str] = Field(description="The negative aspects of the movie, if any]")



    #summary: Annotated[str, "A brief summary of the movie"]
    #sentiment: Annotated[str, "The overall sentiment of the movie, e.g., positive, negative, neutral"]
    #pros : Annotated[Optional[str], "The positive aspects of the movie, if any"]
    #cons : Annotated[Optional[str], "The negative aspects of the movie, if any]"]

Model=ChatOpenAI(model='gpt-4o-mini')


structured_result=Model.with_structured_output(movie)

result=structured_result.invoke("what is the movie 'the godfather' about?")


print(result)