#Summarization of this code's output is written on Be an Archaeologist (archaeologist.html) page
import requests
from PIL import Image
import google.generativeai as genai
import os
API_KEY = "YOUR_MAPS_API_KEY"
API_KEY_1 = "YOUR_GEMINI_API_KEY"
genai.configure(api_key=API_KEY_1)

# Choose a model
model = genai.GenerativeModel()
latitudes = [--4,-4.5,-5]
longitudes = [-73,-73.5,-74]
latitudes1 = [11,11.5,12,12.5,13,13.5]
longitudes1 = [-71,-71.5,-72,-72.5,-73]
latitudes2 = [10,10.5,11,11.5,12,12.5,13]
longitudes2 = [-53,-53.5,-54,-54.5,-55,-55.5,-56]

images = []
images1 = []
images2 = []
useful = []
total_images = images+images1+images2
for lat in latitudes:
    for lon in longitudes:
        url = (
            f"https://maps.googleapis.com/maps/api/staticmap?center={lat},{lon}&zoom=10&size=640x640&maptype=satellite&key={API_KEY}"
        )
        filename = f"amazon_{lat}_{lon}.png"

        images.append(filename)
        response = requests.get(url)

        if response.status_code == 200:
            with open(filename, "wb") as f:
                f.write(response.content)
            print(f"Downloaded {filename}")
            img = Image.open(filename)
            response1 = model.generate_content([
                f"Do you think there is a archealogical site in this image. Answer in  only yes or no? If yes, tell that to which historical site does it relate the most? The coordinates from which image is generated is roughly around the Guiana Shield searching for a historical site and is at coordinates {lat} and {lon}",img])
            print(f"Output for {img}: ", response1.text)
            if "Yes" or "yes" or "YES" in response1.text:
                useful.append(img)
        else:
            print(f"Failed to download at {lat},{lon} - Status code: {response.status_code}")

for lat in latitudes1:
    for lon in longitudes1:
        url = (
            f"https://maps.googleapis.com/maps/api/staticmap?"
            f"center={lat},{lon}&zoom=10&size=640x640&maptype=satellite&key={API_KEY}"
        )
        filename = f"amazon_{lat}_{lon}.png"

        images1.append(filename)
        response = requests.get(url)

        if response.status_code == 200:
            with open(filename, "wb") as f:
                f.write(response.content)
            print(f"Downloaded {filename}")
            img = Image.open(filename)
            response1 = model.generate_content([
                f"Do you think there is a archealogical site in this image. Answer in  only yes or no? If yes, tell that to which historical site does it relate the most and give your best judgement for the historical site. The coordinates from which image is generated is roughly around the Guiana Shield searching for a historical site and is at coordinates {lat} and {lon}",
                img])
            print(f"Output for {img}: ", response1.text)
            if "Yes" or "yes" or "YES" in response1.text:
                useful.append(img)
        else:
            print(f"Failed to download at {lat},{lon} - Status code: {response.status_code}")

for lat in latitudes2:
    for lon in longitudes2:
        url = (
            f"https://maps.googleapis.com/maps/api/staticmap?"
            f"center={lat},{lon}&zoom=10&size=640x640&maptype=satellite&key={API_KEY}"
        )
        filename = f"amazon_{lat}_{lon}.png"

        images2.append(filename)
        response = requests.get(url)

        if response.status_code == 200:
            with open(filename, "wb") as f:
                f.write(response.content)
            print(f"Downloaded {filename}")
            img = Image.open(filename)
            response1 = model.generate_content([
                f"Do you think there is a archealogical site in this image. Answer in  only yes or no? If yes, tell that to which historical site does it relate the most? The coordinates from which image is generated is roughly around the Guiana Shield searching for a historical site and is at coordinates {lat} and {lon}",
                img])
            print(f"Output for {img}: ", response1.text)
            if "Yes" or "yes" or "YES" in response1.text:
                useful.append(img)
        else:
            print(f"Failed to download at {lat},{lon} - Status code: {response.status_code}")


for image in total_images:
    if image not in useful:
        os.remove(image)

for image in useful:
    filename = image.filename
    img = Image.open(filename)

    why = model.generate_content([
        f"Why do you think the location in '{filename}' might be a historical site? What historical site it can be?Give features too",
        img
    ])


