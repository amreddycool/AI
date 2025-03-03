from llama_index.core.tools import FunctionTool
from llama_index.core.agent import ReActAgent
from llama_index.llms.ollama import Ollama
from llama_index.core import Settings
import nest_asyncio
import chainlit as cl

import requests
import json

#from traceloop.sdk import Traceloop

#Traceloop.init()

nest_asyncio.apply()
llm = Ollama(model="llama3.2", request_timeout=120)
Settings.llm = llm

def exchangeRate(fromCurrency, toCurrency): 
    """Get exchange rate from a currency to a currency
       POST JSON message in this format: {"fromCurrency":"GBP", "toCurrency":"EUR"}"
    """
    url = "http://localhost:5000/exchangeRate"
    data = {}
    data["fromCurrency"] = fromCurrency
    data["toCurrency"] = toCurrency
    print("Calling.."+url +" with "+json.dumps(data))
    return requests.post(url, json=data, headers={"Content-Type":"application/json"}).text

add_tool = FunctionTool.from_defaults(fn=exchangeRate)

agent = ReActAgent.from_tools([add_tool], llm=llm, verbose=True)

@cl.on_chat_start
async def on_chat_start():
    await cl.Message(content = "Hello.. I am an Forex AI Agent..Ask me current rates..").send()
    cl.user_session.set("agent", agent)

@cl.on_message
async def on_message(message: cl.Message):
    agent = cl.user_session.get("agent")
    response = agent.chat(message.content)
    await cl.Message(content = str(response)).send()