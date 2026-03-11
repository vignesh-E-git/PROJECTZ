from google import genai
from google.genai import types



def roadmap(input:str):
    API_KEY = "your api key" # PUT YOUR API KEY HERE.
    client = genai.Client(api_key=API_KEY)

    instruction = "your work is to create a roadmap for the given topic.#format : step name + a small description + two youtube link for reference , be short 7 to 8 steps is ok. give step by step so that i can show it in my ui"
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        config=types.GenerateContentConfig(
            system_instruction=instruction),
        contents=input
    )
    return response.text
