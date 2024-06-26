Place your OpenAI API key in Streamlit secrets -> .streamlit/secrets.tomlt

You can create an API-Key at : https://platform.openai.com/settings/profile?tab=api-keys (min. credit are $5)

Start text.bat for text generation via the GPT API

Start image.bat for image generation via DALL-E

Start assistant.bat to use an GPT assistant. 

Change following code in assistant.py to create your own assistant:

name="Math Solver",

instructions="You are a personal math tutor. Write and run code to answer math questions.",
