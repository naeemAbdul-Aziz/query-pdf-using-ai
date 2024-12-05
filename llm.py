import requests
import json
from pdfminer.high_level import extract_text

#query and get response from the api
def get_input_from_user(user_input):
    response = requests.post(
        url="https://api.aimlapi.com/chat/completions",
        headers={
            "Authorization": "Bearer cf1079154538485b93f7ee48d919f000",
            "Content-Type": "application/json",
        },
        data=json.dumps(
            {
                "model": "gpt-4o",
                "messages": [
                    {
                        "role": "user",
                        "content": prompt,
                    },
                ],
                "max_tokens": 512,
                "stream": False,
            }
        ),
    )
    response.raise_for_status()
    response_data = response.json()
    print(response_data['choices'][0]['message']['content'])


user_message = input("type your question: ")
api_response = get_input_from_user(user_message)

# extract text from PDF using pdfminer.six
def read_pdf_to_string(file: str) -> str:
    return extract_text(file)
pdf_as_string = read_pdf_to_string('ainsmq.pdf')

#prompting template 
prompt = f"""
You are a helpful assistant that answers questions using information from a book. Do not hallucinate. If you do not find the information in the book content, say you did not find the information in the book content. I will ask a question, answer with information from book content.

question: {user_message}

book content:
{pdf_as_string}
"""
