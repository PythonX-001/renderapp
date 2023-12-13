

import re
import requests

import os
from lexica import Client
from lexica.constants import languageModels
from bardapi import BardCookies

from markdown import markdown

client = Client()


def convert_markdown_code(text):
  """
  Converts text blocks enclosed in ``` to be formatted as HTML code blocks.
  """
  return markdown(text, extensions=["fenced_code"])

# Example usage



#re.sub(r"```", "", texti)
def fix_code_blocks(text):
    text = re.sub(r"(```.*?```)", r"<pre><code>\1</code></pre>", text, flags=re.DOTALL)
    text = re.sub(r"```", "<pre><code>", text)



def detect_code_blocks(text):
    code_blocks = re.findall(r"`{3}(.*?)`{3}", text, flags=re.DOTALL)
    for block in code_blocks:
        text = text.replace(block, f"<pre><code>{block}</code></pre>")
    return text



def detect_code_blocks_first(text):
    code_blocks = re.findall(r"^`(.*?)`", text, flags=re.DOTALL | re.MULTILINE)
    for block in code_blocks:
        text = text.replace(block, f'<pre><code>{block}</code>  <span class="copy-button"><i class="fa-light fa-copy" style="color: #e8eaed;"></i></span></pre>')
    return text

def fixthebug(data):

    text = data.replace('</code></pre>', '</code><button id="copy-button"onclick="copyto()"><i class="fa fa-light fa-copy" style="color: #e8eaed;"></i></button></pre>')
    return text

def who_created_me(prompt):

    #TODO:response = client.ChatCompletion(prompt,languageModels.bard)

    #TODO:response = str(response['content'])

    response = client.ChatCompletion(prompt,languageModels.bard)['content']




    if "Bard" in response or "Google" in response or  "بارد" in response or ("Bard" and "Google" in response):
        response = response.replace("بارد", "Elliot")

        response = response.replace("Bard", "Elliot")
        response = response.replace("Google", "Sparkl Downfall")
        response = '<p class="botText" id="botText"><span>'+response+'</pre></code></span></p> '
        response = markdown(response, extensions=["fenced_code"])
        response = detect_code_blocks(response)

        response = fixthebug(response)


        return response

    else:
        response = '<p class="botText" id="botText"><span>'+response+'</pre></code></span></p> '
        response = markdown(response, extensions=["fenced_code"])
        response = detect_code_blocks(response)
        response = fixthebug(response)


        return response



#*PHASE: image Generation----------------------------------


def generate_image(prompt):

    api_url = "https://visioncraftapi--vladalek05.repl.co"

    #! Obtain your API key
    api_key = "546197d1-5b74-4f3e-abf1-46210d603801"


    # Set up the data to send in the request
    data = {
    "prompt": prompt,
    "image_count": 2,
    "token": api_key,
    "width": 1024,
    "height": 768
  }

  # Send the request to generate images
    response = requests.post(f"{api_url}/beta/sdxl-turbo", json=data, verify=False)

    # Extract the image URLs from the response
    image_urls = response.json()['images']
    return image_urls

