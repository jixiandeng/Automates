# backend/automates_app/chatgpt_api.py

import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set your OpenAI API key
openai.api_key = os.getenv("CHAT_GPT_API_KEY")

class ChatGPTAPI():
    def generateDescription(self, description, audience, style, tone, hashtags):
        try:
            # Combine the parameters into one user prompt
            userprompt = f"Description: {description}\nAudience: {audience}\nStyle: {style}\nTone: {tone}\nHashtags: {hashtags}"
            
            # Generate the response from the GPT model
            response = openai.chat.completions.create(
                model="chatgpt-4o-latest",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a post creator for the platform LinkedIn. Using details provided input prompt, you will respond with everything in the output outline AND no less than 1,000 characters and no more than 3,000 characters in all 3 parts of the output outline. The output outline: 1. The humanized post description you generated, with emojis where logical. 2. A link to the repository provided. 3. Every hashtag provided. Notes about the outline: You need to provide every part of the outline (1,2,3), but do not list their number explicitaly."
                    },
                    {
                        "role": "user",
                        "content": userprompt
                    }
                ],
                max_tokens=1000
            )
            return response.choices[0].message['content'].strip()
        except Exception as e:
            return f"Error: {str(e)}"