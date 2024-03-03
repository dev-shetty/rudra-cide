import requests, json
from config import OPEN_API_KEY

def complete_chat(message, api_key):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "user", "content": message}
        ]
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()

data=""
pretext="""i will give you a html code and you have to find out the person who is selling the illegal content from the html with alias name give the result and also the context can be grouped like drugs arms etc in the in this format strictly <aliasname:content> only
here is the html"""

with open("testdata.txt",'r',encoding="utf-8") as file:

        data=file.read()
        data=f"""{data}"""
user_message = pretext+data
response = complete_chat(user_message, OPEN_API_KEY)
print("Response:", response)
