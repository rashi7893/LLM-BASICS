from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client()  # reads GEMINI_API_KEY from the .env file

response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents="Explain what an API is in 2 sentences for a beginner.",
)
print(response.text)