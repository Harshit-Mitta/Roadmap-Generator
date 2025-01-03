# import requests

# def make_api_call(content):
#     url = "https://chatgpt-api8.p.rapidapi.com/"
#     payload = [
#         {
#             "content": "Hello! I'm an AI assistant bot based on ChatGPT 3. How may I help you?",
#             "role": "system"
#         },
#         {
#             "content": content,
#             "role": "user"
#         }
#     ]
#     headers = {
#         "content-type": "application/json",
#         "X-RapidAPI-Key":"d50f129f04mshbf790f804f64106p171775jsne9f14b504087" ,
#         "X-RapidAPI-Host": "chatgpt-api8.p.rapidapi.com"
#     }
#     response = requests.post(url, json=payload, headers=headers)
#     return response.json()

import requests
def make_api_call(content):
    url = "https://chat-gpt26.p.rapidapi.com/"

    payload = [
	{
		"content": "Hello! I'm an AI assistant bot based on ChatGPT 3. How may I help you?",
		"role": "system"
	},
	{
		"content": content,
		"role": "user"
	}
    ]
    headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "466c546febmshf7f234f12a4fa1fp1ab173jsn7b406c5d4761",
	"X-RapidAPI-Host": "chat-gpt26.p.rapidapi.com"
    }

    response = requests.post(url, json=payload, headers=headers)

    return response.json()