import webbrowser

from data_extractor import data_extractor_func
from caption_generator import send_to_AI
from llm import get_posts


dataBase = data_extractor_func()

for data in dataBase:

    name = data[0]
    profileLink = data[1]

    post = get_posts(profileLink)

    if post is not None:

        print(f"\nNew post found from {name}")

        caption = send_to_AI(post["caption"])

        print("Generated comment:")
        print(caption)

        webbrowser.open(post["url"])