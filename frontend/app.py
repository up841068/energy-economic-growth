import streamlit as st
import requests
import os

primaryColor="#F63366"

url = os.getenv("API_URL")


response = requests.get(url)


st.header('The Relationship Between Renewable Energy Adoption and Economic Growth')


st.markdown('''
            This is the first version os the UI''')

option = st.selectbox(
    'real GDP prediction 2050',
    ('Select the country from this list', 'Canada', 'South Korea', 'USA'))

st.write('You selected:', option)

year = st.selectbox(
    'The prediction up to which year?',
    ('2030', '2040', '2050'))

st.write('You selected:', option)


prediction = f'https://my-api-svzr7rwnfa-ew.a.run.app/predict?day_of_week={year}'

prediction_ok = requests.get(prediction)

st.write(f'The prediction for the year {year} is:', prediction_ok.json()['wait'])


# Check if the request was successful
if response.ok:
    # Display the JSON response using the st.write() function
    st.write(response.json())
else:
    # Display an error message if the request failed
    st.error('Opssss...failed to retrieve data from API. Have a coffee and sort it :D')
