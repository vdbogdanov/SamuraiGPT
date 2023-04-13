"""
Classes for using the API of various openai products
"""
import openai


class ChatGPT:
    """
    Class for using ChatGPT api features
    """

    def __init__(self, api_key):
        openai.api_key = api_key

    def request(self, prompt):
        """
        Send prompt request to ChatGPT
        """
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )
        return completion.choices[0].message.content
