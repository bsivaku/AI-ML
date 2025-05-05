
# question2_translation.py

import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Initialize OpenAI client with your API key
client = OpenAI(api_key=os.getenv("OPEN_API_KEY"))  # ✅ Matches your .env key

# Prompt the user to choose a model
model_choice = input("Choose a model (options: 'gpt-4', 'gpt-3.5-turbo'): ").strip().lower()

# Validate user input for model selection
if model_choice not in ['gpt-4', 'gpt-3.5-turbo']:
    print("Invalid model choice. Defaulting to 'gpt-4'.")
    model_choice = "gpt-4"

# Paragraph about AI advancements
paragraph = """
Artificial Intelligence (AI) has undergone remarkable advancements in recent years, transforming industries across the globe. 
Initially focused on basic machine learning algorithms and data processing, AI now encompasses complex neural networks, 
deep learning, and natural language processing technologies. These advancements have enabled AI systems to perform tasks once 
considered exclusive to humans, such as language translation, image recognition, and decision-making in real-time. 
In particular, AI's ability to learn from vast amounts of data has led to breakthroughs in areas like healthcare, finance, 
and autonomous vehicles. Furthermore, the integration of AI with other cutting-edge technologies like blockchain and quantum 
computing promises to unlock even more potential, pushing the boundaries of innovation and efficiency. 
As AI continues to evolve, its impact on society and the economy will be profound, making it one of the most transformative 
technologies of our time.
"""

# Define the system and user messages for translation
messages = [
    {
        "role": "system",
        "content": (
            "You are a professional technical translator fluent in both English and Spanish. "
            "You specialize in translating content related to AI and technological advancements."
        )
    },
    {
        "role": "user",
        "content": (
            "Translate the following English paragraph into Spanish. "
            "The content describes the advancements in Artificial Intelligence (AI). "
            "Ensure that the translation maintains technical accuracy, clearly conveys scientific terminology, "
            "and uses professional language suitable for readers in the tech sector.\n\n"
            f"{paragraph}"
        )
    }
]

# Send the request to OpenAI API with the selected model
response = client.chat.completions.create(
    model=model_choice,  # Use the selected model
    messages=messages,
    temperature=0
)

# Output the translated result
print("\n🌐 Translated Paragraph (Spanish):\n")
print(response.choices[0].message.content.strip())
