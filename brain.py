

import re

import os
from lexica import Client
from lexica.constants import languageModels

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

    response = client.ChatCompletion(prompt,languageModels.bard)

    response = str(response['content'])

    if "Bard" in response or "Google" in response or  "بارد" in response or ("Bard" and "Google" in response):
        response = response.replace("بارد", "Elliot")

        response = response.replace("Bard", "Elliot")
        response = response.replace("Google", "Sparkl Downfall")
        response = '<p class="botText" id="botText"><span>'+response+'</pre></code></span></p> '
        response = markdown.markdown(response, extensions=["fenced_code"])
        response = detect_code_blocks(response)

        response = fixthebug(response)


        return response

    else:
        response = '<p class="botText" id="botText"><span>'+response+'</pre></code></span></p> '
        response = markdown(response, extensions=["fenced_code"])
        response = detect_code_blocks(response)
        response = fixthebug(response)


        return response

