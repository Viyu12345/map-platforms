import google.generativeai as genai

# Set up your API key
genai.configure(api_key="YOUR_GEMINI_API_KEY")

# Choose a model
model = genai.GenerativeModel()

# Send a prompt to the model
response = model.generate_content("Give me a short history of Amazon rainforest and its myths about places that may have existed give me the approximate locations of the places along with the location name.")
print(response.text)
# Print the response
locations = model.generate_content(f"From the following text: {response.text} extract all the regions in wihich the cities could possibly be there and give me the regional descriptions along with approximate bounding boxes for such areas(take references from articles,books,etc if needed)")
print(locations.text)


'''Summarization of the answer I got:-
# Lost Cities of the Amazon: Myths, History & Locations
The **Amazon Rainforest**, the world's largest tropical forest, has long been seen as wild and untouched. However, new research suggests it once hosted **sophisticated pre-Columbian civilizations**, complete with roads, canals, and settlements.
Over time, explorers and indigenous oral traditions have described mysterious **lost cities** deep within the Amazon. Below are the most famous myths and their **approximate real-world locations**.

## 1. Ciudad de Z
- **Legend**: A grand lost city sought by British explorer *Percy Fawcett* in the 1920s.
- **Modern Evidence**: LIDAR and archaeological discoveries have revealed vast urban-like earthworks in the region, supporting the idea of advanced settlements.
- **Location**: *Xingu River Basin, Mato Grosso, Brazil*
- **Coordinates**: 10°–13°S, 53°–56°W

## 2. Paititi
- **Legend**: A hidden Inca city of gold, believed to be a refuge after the Spanish conquest.
- **Modern Evidence**: Indigenous stories, ancient trails, and satellite imagery suggest unusual patterns near the Andes foothills.
- **Location**: *Pantiacolla Plateau, Peru-Bolivia border*
- **Coordinates**: `~11°–13.5°S, 71°–73°W`

## 3. El Dorado
- **Legend**: A city of gold linked to a tribal chief who covered himself in gold dust and bathed in a sacred lake.
- **Modern Evidence**: The story is based on Muisca rituals, not a literal golden city.
- **Location**: *Lake Guatavita, near Bogotá, Colombia*
- **Coordinates**: `~4-5°N, 73-74°W`

Conclusion
Modern science confirms that the Amazon once hosted **complex civilizations**, likely inspiring these legends.  
The **Xingu Basin (Ciudad de Z region)** is currently the most promising for real archaeological discoveries.'''

