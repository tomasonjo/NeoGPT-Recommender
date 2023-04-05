import os
import openai

from training import examples

openai.api_key = os.environ.get('OPENAI_KEY')

system = f"""
You are an assistant with an ability to generate Cypher queries based off example Cypher queries.
Example Cypher queries are: \n {examples} \n
Do not response with any explanation or any other information except the Cypher query.
You do not ever apologize and strictly generate cypher statements based of the provided Cypher examples.
You need to update the database using an appropriate Cypher statement when a user mentions their likes or dislikes, or what they watched already.
"""


def generate_cypher(messages):
    messages = [
        {"role": "system", "content": system}
    ] + messages
    print(messages)
    # Make a request to OpenAI
    completions = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages,
        temperature=0.0
    )
    response = completions.choices[0].message.content
    print(response)
    # If the model apologized, remove the first line
    if "apologi" in response:
        response = " ".join(response.split("\n")[1:])
    # Sometime the model adds quotes around Cypher when it wants to explain stuff
    if "`" in response:
        response = response.split("```")[1].strip("`")
    print(response)
    return response


if __name__ == '__main__':
    print(generate_cypher([{'role': 'user', 'content': 'What are some good cartoon?'},
                           {'role': 'assistant', 'content': 'Shrek 3'},
                           {'role': 'user', 'content': 'Which actors appeared in it?'}
                           ]))