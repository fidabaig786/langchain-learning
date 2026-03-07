from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field

from dotenv import load_dotenv

load_dotenv()

Model = ChatOpenAI()

class person(BaseModel):
    name : str = Field(description='Name of the person')
    age : int = Field(description='Age of the person')
    city: str = Field(description='The city of the person')


parser = PydanticOutputParser(pydantic_object=person)

template = PromptTemplate(
    template = 'give me the name , age , city of a person from {place} \n {format_instruction}',
    input_variables=['place'],
    partial_variables=({'format_instruction': parser.get_format_instructions()})
)

chain = template | Model | parser

result = chain.invoke({'place':'Pakisani'})

print(result)




