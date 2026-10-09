from vector import retriever
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

model = OllamaLLM(model = "llama3:8b")

template = """
You are an expert in answering questions about hotels in tripadvisor

Here are some relevant reviews: {reviews}

Here is the question to answer: {question}
"""
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model


while True:
    print("\n\n----------------------------------")
    question = input("What would you like to ask? (type 'quit' to exit): ")
    print("\n\n")
    if question == "quit":
        break

    reviews = retriever.invoke(question)
    result = chain.invoke({"reviews": reviews, "question": question})
    print(result)