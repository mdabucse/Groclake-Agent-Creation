from typing import Optional
import serpapi
from langchain_core.tools import tool
from pydantic import BaseModel, Field

def flights_finder(dept,arr,date):

    params_dict = {
        'api_key': '4fc240867ea244ee14dc5be37426882698acf6e27aedfd09a7f04ed9ca859a44',
        'engine': 'google_flights',
        'type': '2',
        'hl': 'en',
        'gl': 'us',
        'departure_id': dept,
        'arrival_id': arr,
        'outbound_date': date
    }

    try:
        search = serpapi.search(params_dict)
        results = search.data['best_flights']
    except Exception as e:
        results = str(e)
    return results

# # # Setting up the example input

# dep="JFK",    # Departure airport: John F. Kennedy International Airport, New York
# arr="LAX",      # Arrival airport: Los Angeles International Airport
# date="2025-02-01"           # Infants on lap


# # Using the invoke method to call the function
# result = flights_finder(dep,arr,date)
# print(result)