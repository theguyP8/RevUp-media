import json
import os
import requests
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_content_copy():
    prompt = """
    You are an aggressive, direct B2B marketing strategist for an agency. 
    Write a 30-second short-form video script breaking down one specific business growth mistake.
    Output ONLY valid JSON with the following keys:
    {
      "hook": "The first 3-second hook text on screen",
      "voiceover_script": "Full script for TTS without any brackets or stage directions",
      "caption": "Punchy Instagram/TikTok caption with call to action",
      "hashtags": ["#b2b", "#marketing", "#agency"]
    }
    """
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        response_format={"type": "json_object"}
    )
    return json.loads(response.choices[0].message.content)
