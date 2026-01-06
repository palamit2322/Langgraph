from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

llm=ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.5
)

response=llm.invoke("Capital of India")

print(response.content)