from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import numpy

from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-small', dimensions=300)
 

document=["Babar Azam is one of Pakistan’s leading batsmen and has captained the national team across formats. He is known for his elegant stroke play and consistency in international cricket.",
          "Wasim Akram is regarded as one of the greatest left-arm fast bowlers in cricket history. He played a crucial role in Pakistan’s victory at the 1992 Cricket World Cup.",
          "Imran Khan was the captain of Pakistan’s national team when they won the 1992 Cricket World Cup. After retiring from cricket, he became the Prime Minister of Pakistan.",
          "Shaheen Afridi is a prominent fast bowler known for his pace and ability to take early wickets. He has been an important player for Pakistan in all three formats of the game.",
          "Shahid Afridi was famous for his aggressive batting style and powerful hitting. He holds several records and was one of the most popular cricketers in Pakistan."
          ]
query= 'who is Imran Khan'


doc_embedding=embedding.embed_documents(document)

query_embedding=embedding.embed_query(query)

scores = cosine_similarity([query_embedding],doc_embedding)[0]

index, score = sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]

print(query)

print(document[index])

print("the similary score is ",score)





