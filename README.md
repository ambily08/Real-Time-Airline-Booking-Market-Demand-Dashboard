# Real-Time-Airline-Booking-Market-Demand-Dashboard

 Project Overview

This project is a real-time web dashboard built using Streamlit, designed to visualize and analyze market demand in the airline booking industry. It leverages the Aviationstack API to fetch live flight data and displays interactive visualizations that help understand trends such as:

* Most popular routes

* Frequently used airlines

* Busiest departure airports

* Flight status distribution (Scheduled, Active, Delayed, Cancelled)

Project Structure

Real-Time-Airline-Booking-Market-Demand-Dashboard/

├── app.py                     
├── aviationstack_api.py       
├── utils.py                   
├── requirements.txt           
├── README.md   

 Setup Instructions

1. Clone the repository
    git clone https://github.com/ambily08/Real-Time-Airline-Booking-Market-Demand-Dashboard.git
   
    cd Real-Time-Airline-Booking-Market-Demand-Dashboard

3. Install dependencies
    pip install -r requirements.txt

4. Add your Aviationstack API key
    In aviationstack_api.py, replace 'YOUR_API_KEY_HERE' with your actual API key from https://aviationstack.com.

5. Run the app
    streamlit run app.py
   
 Requirements

    streamlit
    pandas
    altair
    requests
