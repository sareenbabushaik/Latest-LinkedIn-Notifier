import ollama
import requests


modelName = "phi3:mini"

ACCESS_TOKEN = "YOUR_LINKEDIN_ACCESS_TOKEN"


def get_person_id(profileLink):

    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Linkedin-Version": "202608",
        "X-Restli-Protocol-Version": "2.0.0"
    }

    # Extract vanity name from profile URL
    vanity_name = profileLink.rstrip("/").split("/")[-1]

    response = requests.get(
        "https://api.linkedin.com/v2/people",
        headers=headers,
        params={
            "q": "vanityName",
            "vanityName": vanity_name
        }
    )

    if response.status_code != 200:

        print("Error finding profile:")
        print(response.text)

        return None

    data = response.json()

    if not data.get("elements"):

        print("Profile not found:", vanity_name)

        return None

    return data["elements"][0]["id"]


def get_posts(profileLink):

    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Linkedin-Version": "202608",
        "X-Restli-Protocol-Version": "2.0.0"
    }

    # Get Person ID from profile URL
    member_id = get_person_id(profileLink)

    if member_id is None:
        return None

    person_urn = f"urn:li:person:{member_id}"

    # Get latest post
    response = requests.get(
        "https://api.linkedin.com/rest/posts",
        headers=headers,
        params={
            "author": person_urn,
            "count": 1,
            "sortBy": "CREATED"
        }
    )

    if response.status_code != 200:

        print("Error getting posts:")
        print(response.text)

        return None

    data = response.json()

    if not data.get("elements"):

        return None

    post = data["elements"][0]

    post_id = post.get("id")

    if not post_id:
        return None

    return {
        "caption": post.get("commentary", ""),
        "post_id": post_id,
        "url": "https://www.linkedin.com/feed/update/" + post_id + "/"
    }


def message(prompt):

    response = ollama.chat(
        model=modelName,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]