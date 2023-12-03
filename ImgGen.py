import requests
import re
import os

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

