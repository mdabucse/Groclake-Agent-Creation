from flask import Flask, request, jsonify
from groclake.modellake import ModelLake
import os
from dotenv import load_dotenv
load_dotenv()

GROCLAKE_API_KEY = os.getenv('GROCLAKE_API_KEY')
GROCLAKE_ACCOUNT_ID = os.getenv('GROCLAKE_ACCOUNT_ID')

if not GROCLAKE_API_KEY:
    raise ValueError("Missing Groclake API Key")

# Initialize ModelLake
model_lake = ModelLake()

def extract_details(user_input):
    """
    Extract date, source, and destination from user-provided text.
    """
    try:
        # user_input = request.json.get("user_input")
        if not user_input:
            return jsonify({"error": "User input is required"}), 400
        
        # Define the extraction prompt
        prompt = f"""
        You are a travel assistant. Extract the following information from the user's input:
        before going to the city names if any one of the city name wrongly entered to convert it to correctly *Eg* Channai -> Chennai Like this
        1. Date of travel (if provided). if the date given like this "tomorrow" or "next week" then convert it to the date. and also it give like this jan 1st then convert it to 01-01-2025. I need the date in this format "YYYY-MM-DD".
        2. Source location (where the travel starts).
        3. Destination location (where the travel ends).
        Respond in string format  date, source, and destination dont add any single or double quotes in the string  .

        User Input: "{user_input}"
        """
        
        # Prepare payload for ModelLake
        payload = {
            "messages": [
                {"role": "system", "content": "You are a travel assistant specializing in extracting travel details."},
                {"role": "user", "content": prompt}
            ]
        }

        # Get response from ModelLake
        response = model_lake.chat_complete(payload)
        extracted_details = response.get("answer")

        # Parse and return the extracted details
        if not extracted_details:
            return -1
        print(type(str(extracted_details)))
        return extracted_details

    except Exception as e:
        return jsonify({"error": str(e)}), 500