import ollama
import streamlit as st


if "messages" not in st.session_state:
    st.session_state["messages"] = []

for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Hi the new llama here"):
    st.session_state["messages"].append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    placeholder = st.empty()
    full_response = ""

    response = ollama.chat(
        model="llama3.2:latest",
        messages=st.session_state["messages"],
        stream=True,
    )

    for chunk in response:
        if chunk["message"]["content"]:
            full_response += chunk["message"]["content"]
            placeholder.markdown(full_response + "|")
    placeholder.markdown(full_response)
    st.session_state["messages"].append({"role": "assistant", "content": full_response})
