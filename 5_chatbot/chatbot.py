from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

model = ChatOpenAI()

chat_history=[
     SystemMessage(content='You are a good writer')
]

while True:
    user_input=input(HumanMessage(content="You: "))
    chat_history.append(user_input)
    if user_input == 'exit':
        break
    response = model.invoke(chat_history)
    chat_history.append(AIMessage(content=response.content))
    print("AI: ", response.content)


