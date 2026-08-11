from llm import message


def send_to_AI(post):

    prompt = f"""
You are a LinkedIn engagement assistant.

Read the following LinkedIn post:

"{post}"

Generate a short, natural and genuine comment for this post.

Rules:
- Keep it professional
- Make it relevant to the post
- Do not sound robotic or AI-generated
- Do not overpraise
- Keep it between 10 and 25 words
- Do not use hashtags
- Do not use emojis
- Return only the comment
"""

    return message(prompt)