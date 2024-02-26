from openai import OpenAI
import os
from dotenv import load_dotenv


load_dotenv()

YOUR_API_KEY = os.environ.get("PPLX_API_KEY")
messages = [
    {
        "role": "system",
        "content": (
            "You are an artificial intelligence assistant and you will to "
            "take this conversation, understand the important points "
            "and provide helpful, detailed, information to help the user "
            "to continue the conversation by pointing out the most relevant "
            "related information."
        ),
    },
    {
        "role": "user",
        "content": (
            "what is RAG (retrieval augmented generation) in the context of Generative AI?"
        ),
    },
]

client = OpenAI(api_key=YOUR_API_KEY, base_url="https://api.perplexity.ai")

# chat completion without streaming
response = client.chat.completions.create(
    model="mistral-7b-instruct",
    messages=messages,
)
print('------------------------------------------------------')
print(response.choices[0].message.content)
print('------------------------------------------------------')
#print(response)


notepad = open("notepad.txt", "w")
# chat completion with streaming
stream = client.chat.completions.create(
    model="mistral-7b-instruct",
    messages=messages,
    stream=False,
)

#for chunk in stream:
#    if chunk.choices[0].delta.content is not None:
#        print(chunk.choices[0].delta.content, end="")