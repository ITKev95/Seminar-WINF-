from openai import OpenAI
import streamlit as st

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

def click_one():
    st.session_state["openai_model"] = "gpt-3.5-turbo"
    st.session_state.messages.append({"role": "assistant", "content": "Switched to GPT-3.5-Turbo"})

def click_two():
    st.session_state["openai_model"] = "gpt-4o"
    st.session_state.messages.append({"role": "assistant", "content": "Switched to GPT-4"})

def click_three():
    st.session_state.messages.append({"role": "assistant", "content":st.session_state["openai_model"]})

st.set_page_config(page_title="Your own Chat Bot")

st.image('chatbot.jpg')

st.title("Your own GPT chatbot!")
st.write("This is a simple chatbot that uses OpenAI's GPT to generate responses")
st.write("You can switch between different models by clicking the buttons below")
st.write("If you click on “current version” the currently selected model will be displayed")
st.write("The preselected model is GPT-3.5-Turbo")



col1, col2, col3= st.columns([1,1,1])

with col1:
    st.button('1 gpt-3.5-turbo', on_click=click_one)
with col2:
    st.button('2 gpt-4', on_click=click_two)
with col3:
    st.button('3 current version', on_click=click_three)

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})
