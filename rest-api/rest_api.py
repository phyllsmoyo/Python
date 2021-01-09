import requests
import json

response = requests.get(
    "https://api.stackexchange.com/2.2/questions?order=desc&sort=activity&site=stackoverflow"
)

for question in response.json()["items"]:
    if question["answer_count"] == 0:
        print(f'Title: {question["title"]}')
        print(f'Link: {question["link"]}')

    else:
        print("skipped")

    print()
