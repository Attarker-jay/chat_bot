#from dotenv import load_dotenv
#from pydantic import BaseModel
#from langchain_openai import ChatOpenAI
#from langchain_anthropic import ChatAnthropic
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
#from vector import retriever

# using external llm
# setting up an llm
#load_dotenv()
#llm = ChatOpenAI(model="gpt-4o-2024-11-20")
#llm = ChatAnthropic(model="claude-3-5-sonnet-20241022")
#response = llm.invoke("what is the meaning of life?")
#print(response)

# local llm
model=OllamaLLM(model="llama3.2")

templete = """
You are an expert in answering questions about basketball.
Here are some releveant reviews: {reviews}
Here is the question to answer: {question}
"""

prompt = ChatPromptTemplate.from_template(templete)
chain = prompt | model

while True:
     print("\n\n-------------------------------------")
     question = input("Ask your question (q to quit): ")
     print("\n\n")
     
     if question == "q":
         break
     
     
     #reviews = retriever.invoke(question)
     response = chain.invoke({"reviews": [] ,"question": question}) 
     print(response)
