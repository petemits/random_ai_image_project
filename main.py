import requests
import os
import random
from datetime import datetime

OUTPUT_FOLDER = "generated_images"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

TOPICS = [
    "Affordable condos in downtown Toronto",
    "Luxury homes near the CN Tower",
    "Future smart housing developments in GTA",
    "Urban skyline and condo investments in Mississauga",
    "Sustainable living apartments in Toronto"
]

def generate_image(prompt):
    print(f"🎨 Generating image for topic: {prompt}")

    # Replicate’s free demo endpoint (no API key needed for light use)
    url = "https://replicate.com/api/models/stability-ai/stable-diffusion/api/predict"

    payload = {
        "input": {
            "prompt": prompt,
            "image_dimensions": "512x512"
        }
    }

    response = requests.post(url, json=payload)

    if response.status_code == 200:
        data = response.json()
        image_url = data.get("output", [None])[0]
        if image_url:
            image_data = requests.get(image_url).content
            filename = os.path.join(
                OUTPUT_FOLDER,
                f"{prompt[:40].replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            )
            with open(filename, "wb") as f:
                f.write(image_data)
            print(f"✅ Image saved as: {filename}")
        else:
            print("⚠️ No image URL found in response.")
    else:
        print(f"❌ Image generation failed (status {response.status_code}): {response.text}")

def main():
    topic = random.choice(TOPICS)
    prompt = f"Create a detailed, photorealistic image of {topic}."
    generate_image(prompt)

if __name__ == "__main__":
    main()
