import os
import openai
import streamlit as st
from streamlit_chat import message

from neo4j_driver import run_query
from english2cypher import generate_cypher
from graph2text import generate_response

# Hardcoded UserID
USER_ID = "Tomaz"

# On the first execution, we have to create a user node in the database.
run_query("""
MERGE (u:User {id: $userId})
""", {'userId': USER_ID})

st.set_page_config(layout="wide")
st.title("NeoGPT with context : GPT-4 + Neo4j")


def generate_context(prompt, context_data='generated'):
    context = []
    # If any history exists
    if st.session_state['generated']:
        # Add the last three exchanges
        size = len(st.session_state['generated'])
        for i in range(max(size-3, 0), size):
            context.append(
                {'role': 'user', 'content': st.session_state['past'][i]})
            context.append(
                {'role': 'assistant', 'content': st.session_state[context_data][i]})
    # Add the latest user prompt
    context.append({'role': 'user', 'content': str(prompt)})
    return context


# Storing the chat
if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'raw_generated' not in st.session_state:
    st.session_state['raw_generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

if 'cypher' not in st.session_state:
    st.session_state['cypher'] = []


def get_text():
    input_text = st.text_input(
        "Ask away", "", key="input")
    return input_text


# Define columns
col1, col2 = st.columns([2, 1])

with col2:
    another_placeholder = st.empty()
with col1:
    placeholder = st.empty()
user_input = get_text()


if user_input:
    cypher = generate_cypher(generate_context(user_input))
    # If not a valid Cypher statement
    if not "MATCH" in cypher:
        st.session_state.past.append(user_input)
        st.session_state.generated.append(
            cypher)
        st.session_state.cypher.append(
            "No Cypher statement was generated")
        st.session_state.raw_generated.append("")
    else:
        results = run_query(cypher, {'userId': USER_ID})
        # Harcode result limit to 10
        results = results[:10]
        answer = generate_response(generate_context(
            f"Question was {user_input} and the response should include only information that is given here: {str(results)}", 'raw_generated'))
        st.session_state.raw_generated.append(str(results))
        st.session_state.past.append(user_input)
        st.session_state.generated.append(answer),
        st.session_state.cypher.append(cypher)


# Message placeholder
with placeholder.container():
    if st.session_state['generated']:
        size = len(st.session_state['generated'])
        # Display only the last three exchanges
        for i in range(max(size-3, 0), size):
            message(st.session_state['past'][i],
                    is_user=True, key=str(i) + '_user')
            message(st.session_state["generated"][i], key=str(i))


# Generated Cypher statements
with another_placeholder.container():
    if st.session_state['cypher']:
        st.text_area("Latest generated Cypher statement",
                     st.session_state['cypher'][-1], height=240)
