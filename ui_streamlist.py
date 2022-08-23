import streamlit as st
from templates.Templates import PromptTemplate
from generators.title_to_abstract import title_to_abstract_generator
from generators.topic_to_abstract import topic_to_abstract_generator

from app import generate
from Settings import Settings


prompt = PromptTemplate()
settings = Settings()


st.title('Scientific Paper Abstract Writer')

option = st.selectbox('Please select one',
                      ('Title to Abstract', 'Topic to Abstract'))

st.write('You selected:', option)

if option == 'Title to Abstract':
    title = st.text_input('Please input the title of the paper. Five or more words are suggested for best results.')
    if st.button('Generate'):
        st.write(generate({'title': title}, 'title')['result'][0])
else:
    topic = st.text_input(
        'Please input the topic of the paper. Example: Topic_1 , Topic_2, Topic_3 ')
    list_topic = topic.split(',')
    if st.button('Generate'):
        st.write(generate({'topic': list_topic}, 'topic')['result'][0])
