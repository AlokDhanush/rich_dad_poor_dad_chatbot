import os
import warnings, logging
from langchain_ollama import OllamaLLM
from langchain.prompts import ChatPromptTemplate
from embedding import retriever

os.environ["CHROMA_TELEMETRY_ENABLED"] = "false"
warnings.filterwarnings("ignore")
logging.getLogger("chromadb").setLevel(logging.ERROR)


model = OllamaLLM(model="llama3.2", temperature=0.7)

TEMPLATE = """
You are a helpful assistant that helps people find information in 'Rich Dad Poor Dad' book. Use the following pieces of context to answer the question at the end.\
If you don't know the answer, just say that you don't know, don't try to make up an answer.
Context:
{context}

Question:
{question}

Answer:
"""

prompt = ChatPromptTemplate.from_template(TEMPLATE)

chain = prompt | model 

while True:

    print("\n------------------------------------------------------\n")

    query = input("Ask a question about the book ('exit' to quit): ")

    if query == "exit":
        break

    docs = retriever.get_relevant_documents(query)

    context = "\n".join(doc.page_content for doc in docs)

    result = chain.invoke({"context": context, "question": query})

    print("RESPONSE:\n", result)  