from openai import OpenAI
import os
from IPython.display import display, Image, Audio
import sounddevice as sd
import numpy as np
import requests

os.environ[
    'OPENAI_API_KEY'] = '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'

client = OpenAI()
#print(dir(client))

response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    input="Hello There! This is not a streaming test. My name is Oluwapelumi Dada The name Oluwapelumi is of Yoruba origin, a language spoken in Nigeria and other parts of West Africa. In Yoruba, Oluwa means God or Lord, and it is a common prefix in names to denote God's ownership or blessing. The rest of the name, pelumi, could be interpreted in various ways depending on the specific context or additional components in the name.",
    stream = True
)

print(dir(response))

audio = b""
for chunk in response.iter_content(chunk_size=1024 * 1024):
    audio += chunk
Audio(audio)
