import streamlit as st
import traceback
from llm import extract_details  # Assuming this extracts details from user input
from flight import flights_finder
from api_flight_details_extraction import extract_flight_details
import json
# Mapping of city names to IATA codes
IATA_CODES = {
    "Agartala": "IXA",
    "Agatti": "AGX",
    "Agra": "AGR",
    "Ahmedabad": "AMD",
    "Aizawl": "AJL",
    "Amritsar": "ATQ",
    "Aurangabad": "IXU",
    "Ayodhya": "AYJ",
    "Bagdogra": "IXB",
    "Bareilly": "BEK",
    "Belagavi": "IXG",
    "Bengaluru": "BLR",
    "Bhopal": "BHO",
    "Bhubaneswar": "BBI",
    "Chandigarh": "IXC",
    "Chennai": "MAA",
    "Coimbatore": "CJB",
    "Darbhanga": "DBR",
    "Dehradun": "DED",
    "Delhi": "DEL",
    "Deoghar": "DGH",
    "Dharamshala": "DHM",
    "Dibrugarh": "DIB",
    "Dimapur": "DMU",
    "Diu": "DIU",
    "Durgapur": "RDP",
    "Gaya": "GAY",
    "Goa": "GOI",
    "Gondia": "GDB",
    "Gorakhpur": "GOP",
    "Guwahati": "GAU",
    "Gwalior": "GWL",
    "Hirasar": "HSR",
    "Hubli": "HBX",
    "Hyderabad": "HYD",
    "Imphal": "IMF",
    "Indore": "IDR",
    "Itanagar": "HGI",
    "Jabalpur": "JLR",
    "Jagdalpur": "JGB",
    "Jaipur": "JAI",
    "Jaisalmer": "JSA",
    "Jammu": "IXJ",
    "Jharsuguda": "JRG",
    "Jodhpur": "JDH",
    "Jorhat": "JRH",
    "Kadapa": "CDP",
    "Kannur": "CNN",
    "Kanpur": "KNU",
    "Khajuraho": "HJR",
    "Kochi": "COK",
    "Kolhapur": "KLH",
    "Kolkata": "CCU",
    "Kozhikode": "CCJ",
    "Kurnool": "KJB",
    "Leh": "IXL",
    "Lucknow": "LKO",
    "Madurai": "IXM",
    "Mangaluru": "IXE",
    "Mumbai": "BOM",
    "Mysuru": "MYQ",
    "Nagpur": "NAG",
    "Nashik": "ISK",
    "North Goa": "GOX",
    "Pantnagar": "PGH",
    "Patna": "PAT",
    "Port Blair": "IXZ",
    "Prayagraj": "IXD",
    "Pune": "PNQ",
    "Raipur": "RPR",
    "Rajahmundry": "RJA",
    "Rajkot": "RAJ",
    "Ranchi": "IXR",
    "Salem": "SXV",
    "Shillong": "SHL",
    "Shirdi": "SAG",
    "Shivamogga": "RQY",
    "Silchar": "IXS",
    "Srinagar": "SXR",
    "Surat": "STV",
    "Thiruvananthapuram": "TRV",
    "Tiruchirappalli": "TRZ",
    "Tirupati": "TIR",
    "Tuticorin": "TCR",
    "Udaipur": "UDR",
    "Vadodara": "BDQ",
    "Varanasi": "VNS",
    "Vijayawada": "VGA",
    "Visakhapatnam": "VTZ"
}

# Title and Description
st.title("Flight Ticket Booking")
st.markdown("""
### Effortlessly book tickets and manage your travel history

Provide your travel details to book a ticket or manage your travel history.
""")

# Sidebar for navigation
page = st.sidebar.radio("Select a page:", ("Ticket Booking", "Travel History Management"))

try:
    if page == "Ticket Booking":
        # Section: Ticket Booking
        st.subheader("Ticket Booking")
        travel_details = st.text_area("Travel Details", placeholder="Enter your travel details (e.g., Departure City, Destination City, Travel Date, Number of Passengers)")

        if st.button("Submit", key="submit_booking"):
            if not travel_details.strip():
                st.error("Please provide your travel details before submitting.")
            else:
                # Extract details using LLM
                llm_response = extract_details(travel_details)
                # st.write(type(llm_response))
                # Convert city names to IATA codes
                llm_response = llm_response.split(',')
                source_city = llm_response[1].strip()
                destination_city = llm_response[2].strip()
                travel_date = llm_response[0].strip()
                
                source_iata = IATA_CODES.get(source_city, "Unknown")
                destination_iata = IATA_CODES.get(destination_city, "Unknown")
                api = flights_finder(source_iata,destination_iata,travel_date)
                output_file = r'A:\Projects\Flight-Ticket\try\data\airport_data.json'
                # with open(output_file, 'w') as file:
                #     json.dump(json_data, file, indent=4)
                # st.write(api)
                summa_result = extract_flight_details(api)
                st.write("This is Suma Result",summa_result)
                st.success(f"Booking Details:\n- Source: {source_city} ({source_iata})\n- Destination: {destination_city} ({destination_iata})\n- Date: {travel_date}")

    elif page == "Travel History Management":
        # Section: Travel History Management
        st.subheader("Travel History Management")
        st.markdown("""
        **Manage and inquire about your travel history:**
        
        Use the text box below to ask questions about your past travels, and our AI will assist you.
        """)
        travel_history_query = st.text_input("Enter your query about travel history", key="history_query")

        if st.button("Get Travel History", key="submit_history"):
            if not travel_history_query.strip():
                st.error("Please enter a query to get travel history.")
            else:
                # Simulated response
                st.success(f"Here's the information related to your query: \n{travel_history_query}")
except Exception as e:
    st.error("An error occurred while processing your request. Please try again.")
    st.text("Error details:")
    st.text(traceback.format_exc())

# Footer
st.write("---")
st.markdown("Made with ❤️ using Streamlit.")
