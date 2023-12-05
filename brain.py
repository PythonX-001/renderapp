

import re
import requests

import os
from lexica import Client
from lexica.constants import languageModels
from bardapi import BardCookies

from markdown import markdown

client = Client()
cookie_dict = {
    "__Secure-1PSID": "dwhX9kTyfw5Ubv7hjzx39inpezs6fIMOsef7NusVvdjVhqUxAa5uNoIHkwiYmnzTg5PjGg.",
    "__Secure-1PSIDTS": "sidts-CjEBPVxjSovSnC63IRVKpkgeFpBWjcNCmC3fGp2VgeUJ9k0kCkhaXth5YDhgk0p07J-SEAA",
    "__Secure-1PSIDCC": "ACA-OxNW3GOwiGBV_FH-PHiV3Rs2cxO-OoU9I1OVTZiTW8-MxA286OxKHuPz6jGJqOcoA0g14rE",
    # Any cookie values you want to pass session object.
}




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

import re

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

    bard = BardCookies(cookie_dict=cookie_dict)
    response = bard.get_answer(prompt)["content"]



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

    print("heelo world")
    #* Get image URLs from API response
    api_url = "https://visioncraftapi--vladalek05.repl.co"

    #! Obtain your API key
    api_key = "546197d1-5b74-4f3e-abf1-46210d603801"

  # Generate images using a specific model
    model = "ICantBelieveItsNotPhotography_seco"
    sampler = "Euler"
    image_count = 3
    cfg_scale = 8
    steps = 30

    # Set up the data to send in the request
    data = {
        "model": model,
        "sampler": sampler,
        "prompt": prompt,
        "negative_prompt": "canvas frame, ((disfigured)), ((bad art)), ((deformed)),((extra limbs)),((close up)),((b&w)), weird colors, blurry, (((duplicate))), ((morbid)), ((mutilated)), [out of frame], extra fingers, mutated hands, ((poorly drawn hands)), ((poorly drawn face)), (((mutation))), (((deformed))), ((ugly)), blurry, ((bad anatomy)), (((bad proportions))), ((extra limbs)), cloned face, (((disfigured))), out of frame, ugly, extra limbs, (bad anatomy), gross proportions, (malformed limbs), ((missing arms)), ((missing legs)), (((extra arms))), (((extra legs))), mutated hands, (fused fingers), (too many fingers), (((long neck))), Photoshop, video game, ugly, tiling, poorly drawn hands, poorly drawn feet, poorly drawn face, out of frame, mutation, mutated, extra limbs, extra legs, extra arms, disfigured, deformed, cross-eye, body out of frame, blurry, bad art, bad anatomy, 3d render",
        "image_count": image_count,
        "token": api_key,
        "cfg_scale": cfg_scale,
        "steps": steps
    }

    # Send the request to generate images
    response = requests.post(f"{api_url}/generate", json=data, verify=False)

    # Extract the image URLs from the response
    image_urls = response.json()["images"]
    print(image_urls)
    return  image_urls
