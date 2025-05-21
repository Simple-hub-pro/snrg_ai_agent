# To run this code you need to install the following dependencies:
# pip install google-genai

import base64
import os
from google import genai
from google.genai import types


with open("main.json", "r") as f:
    data = f.read()


def generate(savol):
    client = genai.Client(
        api_key="AIzaSyDFp3QYNNMG-9c1jhhlv3IAMcsgKofmYOo",
    )

    model = "gemini-2.0-flash-lite"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=f"""{savol}"""),
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        response_mime_type="text/plain",
        system_instruction=[
            types.Part.from_text(text=f"""tasavvur qil sen sotuv menejerisan {data} - ma'lumotlaridan foydalan va savollarga javob ber. agar ushbu mavzuda qo'shimcha ma'lumot    bera olsang ma'lumotni faqat tanishish maqsadida taqdim 
            etishing mumkin."""),
        ]
    )

    javob = client.models.generate_content(
        model=model,
        contents=contents,
        config=generate_content_config,
    )
    return javob.text


if __name__ == "__main__":
    generate("synergy hub academyda qanday yo'nalishlar bor va ularni kelajagi bormi?")
