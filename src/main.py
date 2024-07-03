import requests
from dotenv import load_dotenv

from utils.config import get_config

load_dotenv()


def main():
    config = get_config()
    url = f"{config.backend.host}/api/v1/ask"

    input_text = input(">>> ")
    while input_text.lower() != "bye2":
        data = {"query": input_text.lower()}
        response = requests.post(url=url, json=data, headers={"Content-Type": "application/json"})
        contents = response.text.split("\\n")
        for content in contents:
            print(content)
        input_text = input(">>> ")


if __name__ == "__main__":
    main()
