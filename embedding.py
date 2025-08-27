import os
from langchain_community.document_loaders import PyPDFLoader
import asyncio
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma


file_path = "data/Rich Dad Poor Dad.pdf"

loader = PyPDFLoader(file_path)
pages = []

pages_to_skip = set([i for i in range(1, 17) if i != 2] + [i for i in range(235, 242)])

async def load_pages():
    i = 1
    async for page in loader.alazy_load():
        if i not in pages_to_skip:
            pages.append(page)
        
        i += 1

asyncio.run(load_pages())

db_location = "./chromadb"

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2") 

if not os.path.exists(db_location):
    vector_store = Chroma.from_documents(
        documents = pages,
        embedding = embeddings,
        persist_directory = db_location
    )

else:
    vector_store = Chroma(
        embedding_function = embeddings,
        persist_directory = db_location
    )

retriever = vector_store.as_retriever(kwargs={"k":3})
