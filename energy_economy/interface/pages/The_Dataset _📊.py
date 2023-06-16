import os
import streamlit as st
import pandas as pd
import numpy as np
import streamlit as st

# Left menu logo
st.sidebar.image(os.getcwd() + "/energy_economy/interface/logo2.png", width=200)

url = 'https://raw.githubusercontent.com/up841068/energy-economic-growth/main/raw_data/df.csv'
#df = pd.read_csv(url, engine='url')

df = pd.read_csv(url)

countries = ('Afghanistan', 'Algeria', 'American Samoa', 'Angola',
       'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba',
       'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain',
       'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin',
       'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana',
       'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi',
       'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Cayman Islands',
       'Central African Republic', 'Chad', 'China', 'Colombia', 'Comoros',
       'Congo', 'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cuba',
       'Cyprus', 'Czechia', 'Democratic Republic of Congo', 'Denmark',
       'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt',
       'El Salvador', 'Equatorial Guinea', 'Estonia', 'Eswatini',
       'Ethiopia', 'Fiji', 'Finland', 'France', 'French Polynesia',
       'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Greece',
       'Greenland', 'Grenada', 'Guam', 'Guatemala', 'Guinea',
       'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hong Kong',
       'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq',
       'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan',
       'Kazakhstan', 'Kenya', 'Kiribati', 'Kuwait', 'Kyrgyzstan', 'Laos',
       'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Lithuania',
       'Luxembourg', 'Macao', 'Madagascar', 'Malawi', 'Malaysia',
       'Maldives', 'Mali', 'Malta', 'Mauritania', 'Mauritius', 'Mexico',
       'Moldova', 'Mongolia', 'Morocco', 'Mozambique', 'Myanmar',
       'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Zealand',
       'Nicaragua', 'Niger', 'Nigeria', 'North Macedonia', 'Norway',
       'Oman', 'Pakistan', 'Palestine', 'Panama', 'Papua New Guinea',
       'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal',
       'Puerto Rico', 'Qatar', 'Romania', 'Russia', 'Rwanda',
       'Saint Kitts and Nevis', 'Saint Lucia',
       'Saint Vincent and the Grenadines', 'Samoa',
       'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia',
       'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia',
       'Solomon Islands', 'South Africa', 'South Korea', 'Spain',
       'Sri Lanka', 'Sudan', 'Suriname', 'Sweden', 'Switzerland', 'Syria',
       'Tajikistan', 'Tanzania', 'Thailand', 'Togo', 'Tonga',
       'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan',
       'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom',
       'United States', 'United States Virgin Islands', 'Uruguay',
       'Uzbekistan', 'Vanuatu', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe')



######################################
# DATASET EXPLORATION
######################################
st.markdown('## **The Dataset**')


st.markdown("The Energy dataset is a collection of key metrics \
    maintained by 'Our World in Data'. It is updated regularly and includes data\
        on energy consumption (primary energy, per capita, and growth rates), \
            energy mix, electricity mix and other relevant metrics.")

st.markdown("Data Source: https://ourworldindata.org/energy")


country = st.selectbox(
    'Select the country from the list below', countries)

df_filtered = df[df.country == country][['country',
                                         'year',
                                         'coal_elec_per_capita',
                                         'oil_elec_per_capita',
                                         'nuclear_elec_per_capita',
                                         'gas_elec_per_capita',
                                         'solar_elec_per_capita',
                                         'wind_elec_per_capita',
                                         'hydro_elec_per_capita',
                                         'biofuel_elec_per_capita',
                                         'GDP_per_capita']]

# Show dataset
st.dataframe(df_filtered, use_container_width=False)
