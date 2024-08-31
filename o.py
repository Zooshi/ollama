import ollama
import streamlit as st

prompt = "List 10 great Consumer Staple stocks to invest in."

chat = ollama.chat(
    model="llama3.1:8b", messages=[{"role": "user", "content": prompt}], stream=True
)

for chunk in chat:
    print(chunk["message"]["content"], end="", flush=True)
