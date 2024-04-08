import streamlit as st
import ollama
import time



# input prompt

prompt = st.chat_input("Talk with Yuri!")

if prompt:

    #Display prompt from user
    with st.chat_message("You"):
        st.write(prompt)

    #process
    with st.spinner("Let me thing...给我点时间琢磨一下....."):
        result = ollama.chat(model="llama2", messages=[{
            "role" :"user",
            "content": prompt,


        }])
        response = result["message"]["content"]
        st.write((response))


# def stream_data(text, delay: float = 0.02):
#     for word in text.split():
#         yield word + " "
#         time.sleep(delay)



# # input prompt

# prompt = st.chat_input("Talk with Yuri!")

# if prompt:

#     #Display prompt from user
#     with st.chat_message("You"):
#         st.write(prompt)

#     #process
#     with st.spinner("Let me thing...给我点时间琢磨一下....."):
#         result = ollama.chat(model="llama2", messages=[{
#             "role" :"user",
#             "content": prompt,


#         }])
#         response = result["message"]["content"]
#         st.write_stream(stream_data(response))