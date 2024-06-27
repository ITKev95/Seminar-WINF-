**Instructions**

Place your OpenAI API key in Streamlit secrets -> .streamlit/secrets.tomlt

You can create an API-Key at : https://platform.openai.com/settings/profile?tab=api-keys (min. credit are $5)

Start text.bat for text generation via the GPT API

Start image.bat for image generation via DALL-E

Start assistant.bat to use the GPT assistant

Change following code in assistant.py to create your own assistant:

    name="Math Solver", #type here the name of your assistant

    instructions="You are a personal math tutor. Write and run code to answer math questions.", #describe what the purpose of the assinstant is

    tools=[{"type": "code_interpreter"}], #File Search or Code Interpreter  

    model="gpt-4o" #version of modle like gpt-3.5-turbo ect.


**Used Python libraries**

The following libraries need to be installed:

https://github.com/openai/openai-python

https://github.com/streamlit/streamlit




