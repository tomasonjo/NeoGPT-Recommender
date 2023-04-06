import os
import openai

openai.api_key = os.environ.get('OPENAI_KEY')

system = f"""
You are an assistant that helps to generate text to form nice and human understandable answers based.
The latest prompt contains the information, and you need to generate a human readable response based on the given information.
Make it sound like the information are coming from an AI assistant, but don't add any information.
Do not add any additional information that is not explicitly provided in the latest prompt.
I repeat, do not add any information that is not explicitly given.
"""


def generate_response(messages):
    messages = [
        {"role": "system", "content": system}
    ] + messages
    print(messages)
    # Make a request to OpenAI
    completions = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.0
    )
    response = completions.choices[0].message.content
    print(response)
    # If the model apologized, remove the first line or sentence
    if "apologi" in response:
        if "\n" in response:
            response = " ".join(response.split("\n")[1:])
        else:
            response = " ".join(response.split(".")[1:])
    return response


if __name__ == '__main__':
    data = [{'actor': 'Sigourney Weaver', 'role': "Witch"}, {'actor': 'Holly Hunter', "role": "Assassin"}, {
        'actor': 'Dermot Mulroney'}, {'actor': 'William McNamara'}]
    print(generate_response([{'role': 'user', 'content': str(data)}]))
