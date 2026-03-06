from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_classic.output_parsers import StructuredOutputParser, ResponseSchema
from dotenv import load_dotenv

load_dotenv()

Model = ChatOpenAI()

schema = [
    ResponseSchema(name='Fact 1', description='The first fact about the politician '),
    ResponseSchema(name='Fact 2', description='The second fact about the politician'),
    ResponseSchema(name='Fact 3', description='The third fact about the politician')
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template = 'Give me three facts about the {policitian} \n {format_instruction}',
    input_variables=['policitian'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)


chain = template | Model | parser

result = chain.invoke({'policitian': 'Imran Khan'})

print(result)

