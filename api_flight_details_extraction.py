import json

# Extract airline, airline_logo, and flight_number
def extract_flight_details(api_link):
    result = []
    for entry in api_link:
        for flight in entry.get("flights", []):
            result.append({
                "airline": flight.get("airline"),
                "airline_logo": flight.get("airline_logo"),
                "flight_number": flight.get("flight_number")
            })
    return result

# Call the function and print the result
# flight_details = extract_flight_details(json_data)
# print(flight_details)

