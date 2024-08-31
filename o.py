import ollama
import streamlit as st

prompt = "List 10 great Consumer Staple stocks to invest in which are not mainstream."

chat = ollama.chat(
    model="qwen2:7b", messages=[{"role": "user", "content": prompt}], stream=True
)

for chunk in chat:
    print(chunk["message"]["content"], end="", flush=True)
