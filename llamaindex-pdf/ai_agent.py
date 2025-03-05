
from llama_index.llms.ollama import Ollama
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext, ServiceContext
from llama_index.core import load_index_from_storage
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import Settings
import chainlit as cl
import os

llm = Ollama(model="llama3.2", request_timeout=120)
Settings.llm = llm
embed_model = HuggingFaceEmbedding( model_name="BAAI/bge-large-en-v1.5", trust_remote_code=True)
Settings.embed_model = embed_model


if os.path.exists(".store"):
    storageContext = StorageContext.from_defaults(persist_dir="./.store")
    index = load_index_from_storage(storageContext)
else:
    documents = SimpleDirectoryReader("data").load_data()
    index = VectorStoreIndex.from_documents(documents, show_progress=True)
    index.set_index_id("vector_index")
    index.storage_context.persist("./.store")

query_engine = index.as_query_engine(response_mode='tree_summarize', use_async=True)

@cl.on_chat_start
async def on_chat_start():
    await cl.Message(content = "Hello.. I am an Physics AI Agent..Ask me anything on Physics..").send()

@cl.on_message
async def on_message(message: cl.Message):
    response = query_engine.query(message.content)
    print(response)
    await cl.Message(content = str(response)).send()    