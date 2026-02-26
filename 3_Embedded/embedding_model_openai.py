from langchain_openai import OpenAIEmbeddings

from dotenv import load_dotenv

load_dotenv()

embedding=OpenAIEmbeddings(model='text-embedding-3-small', dimensions=20)

result = embedding.embed_documents("What is the famous sport of Pakistan")

print(str(result))




