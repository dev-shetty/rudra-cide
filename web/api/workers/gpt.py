import openai, json

from config import OPEN_API_KEY
openai.api_key = OPEN_API_KEY

prompts = """
Read the message and what type of operation should we use (CRUD), how much is the quantity, what is the standard unit of the quantity, what is the item to be operated. 
Fill in the below json and return only the json (not even a text) and all text should be lower case.
{
    "operation": string,
    "quantity": integer,
    "unit": string,
    "item": string
}
"""

async def genResponse(message: str):
    try:
        text = f"Message: '{message}'"+prompts
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=text,
            max_tokens=75,  # Increase the max_tokens value to get a longer response
            temperature=0.7,
            top_p=1.0,
            n=1,
            stop=None,
            frequency_penalty=0,
            presence_penalty=0,
            # format="json"  
        )
        return { 'success': True, 'data': json.loads(response.choices[0].text) }
    except Exception as e:
        return { 'success': False, 'message': f'{e}' }

