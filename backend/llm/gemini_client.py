import os

from google import genai

class GeminiClient:

    def __init__(self):

        self.client = genai.Client(
            api_key=os.getenv(
                "api_key"
            )
        )

    def generate(
        self,
        prompt
    ):

        response = (
            self.client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )
        )

        return response.text