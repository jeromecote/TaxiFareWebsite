import streamlit as st
import datetime
import requests



today = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")

'''
# Fair Taxi
'''

st.markdown("""## When?""")

date_time = st.text_input('Date and Time', today)

st.markdown("""
## Where?
*Tips*: You can use [maps](https://www.google.ca/maps/@40.7395181,-73.9952386,13.55z) to copy the `Longitude, Latitude`
""")

pickup = st.text_input('Pickup longitude and latitude', '40.727285, -73.993568')
dropoff = st.text_input('Dropoff longitude and latitude', '40.753531, -73.980986')

st.markdown("""## Who?""")

passenger_count = st.selectbox('Passenger count', range(1, 11))



def get_response():
    params = {
        "key":datetime.datetime.now(),
        "pickup_datetime":date_time,
        "pickup_longitude":pickup_longitude,
        "pickup_latitude":pickup_latitude,
        "dropoff_longitude":dropoff_longitude,
        "dropoff_latitude":dropoff_latitude,
        "passenger_count":passenger_count
    }

    url = 'http://taxifare.lewagon.ai/predict_fare/'

    response = requests.get(url, params=params).json()
    return response



if st.button('Get Fare'):
    pickup_longitude, pickup_latitude = pickup.split(", ")
    dropoff_longitude, dropoff_latitude = dropoff.split(", ")

    fare = get_response()['prediction']

    st.write(f"Your ride will cost {round(fare, 2)}$")

else:
    st.write('Hit `Get Fare` and see the cost of your ride!!')









