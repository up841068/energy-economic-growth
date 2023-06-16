import streamlit as st
import requests
import pandas as pd
import numpy as np
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

# Left menu logo
st.sidebar.image("logo2.png", width=200)




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
# Title and text
######################################

st.markdown(f"""
<div style="text-align: center;font-size:42px;font-weight:bold;">
    🔍 Dataset Exploration 🕵️‍♀️
</div>
""", unsafe_allow_html=True)
st.write('---')

st.markdown(f"""
<div style="text-align: center;font-size:23px;font-weight:bold;">
    Explore the energy dataset. Visualize data points 📊, plot energy adoption over time 📈, \
        compare countries and energy sources, and gain insights 💡 <br>
</div>
""", unsafe_allow_html=True)
st.write('---')


######################################################
# Evolution of the Energy Source Adoption per country
######################################################


st.markdown(f"""
<div style="text-align: center;font-size:28px;font-weight:bold;">
    Select the countries 🌎 you want to explore
</div> <br>
""", unsafe_allow_html=True)




col1, col2, col3 = st.columns(3)

with col1:
    country1 = st.selectbox(
        'Country 1', countries, index=23)

with col1:
    country4 = st.selectbox(
        'Country 4', countries, index=30)

with col2:
    country2 = st.selectbox(
       'Country 2', countries, index=8)

with col2:
    country5 = st.selectbox(
        'Country 5', countries, index=35)

with col3:
    country3 = st.selectbox(
        'Country 3', countries, index=177)

with col3:
    country6 = st.selectbox(
        'Country 6', countries, index=176)

st.write('  ')

countries = [country1, country2, country3, country4, country5, country6]

st.markdown(f"""
<div style="text-align: center;font-size:28px;font-weight:bold;">
    Next, choose the energy source and visualize 🔍 the results below
</div>
""", unsafe_allow_html=True)


energy_list = ('Coal', 'Oil',
       'Gas', 'Hydro',
       'Nuclear', 'Biofuel',
       'Solar', 'Wind')

energy_type = st.selectbox(
    ' ', energy_list)

if energy_type == 'Coal':
    energy_type = 'coal_elec_per_capita'
elif energy_type == 'Oil':
    energy_type = 'oil_elec_per_capita'
elif energy_type == 'Gas':
    energy_type = 'gas_elec_per_capita'
elif energy_type == 'Hydro':
    energy_type = 'hydro_elec_per_capita'
elif energy_type == 'Nuclear':
    energy_type = 'nuclear_elec_per_capita'
elif energy_type == 'Biofuel':
    energy_type = 'biofuel_elec_per_capita'
elif energy_type == 'Solar':
    energy_type = 'solar_elec_per_capita'
else:
    energy_type = 'wind_elec_per_capita'


import seaborn as sns

sns.set_style("darkgrid")

plt.figure(figsize=(10,6))

for country in countries:

   country_data = df[df['country'] == country]
   melted_df = country_data.melt(id_vars='year', value_vars=energy_type)

   sns.lineplot(data=melted_df, x='year', y='value', label=country,
                ci=None, linestyle='-') # Remove CI and solid line


# Add title and axis labels
plt.title(f"{energy_type.split('_')[0].capitalize()} Electricity production per Capita",
          fontsize=18, fontweight='bold',
          pad=20)


# Axis, labels (x and y)
plt.xlabel('Year', fontsize=14, fontweight='bold')
plt.ylabel('Production per Capita in kWh', fontsize=14, fontweight='bold')
plt.xlim(2000,2021)
plt.xticks(range(2000,2022, 3))# Format years
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

# Show legend
# Show legend
legend = plt.legend(loc='upper center',
                    ncol=len(countries), # Number of columns
                     fontsize=10) # Set font size

legend.get_frame().set_facecolor('white') # White background
legend.get_frame().set_edgecolor('black') # Black border

st.pyplot(plt)





















######################################
# GDP EXPLORATION
######################################


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
st.write('---')

st.markdown(f"""
<div style="text-align: center;font-size:28px;font-weight:bold;">
    Exploring the 'Real GDP per Capita' 💸/😎 evolution
</div> <br>
""", unsafe_allow_html=True)



st.markdown(f"""
<div style="text-align: center;font-size:20px;">
    Feel free 🙃 to change the countries below and check the results
</div> <br>
""", unsafe_allow_html=True)

col4, col5, col6 = st.columns(3)

with col4:
    country1 = st.selectbox(
        ' ', countries, index=9)

with col4:
    country4 = st.selectbox(
        ' ', countries, index=16)

with col5:
    country2 = st.selectbox(
       ' ', countries, index=42)

with col5:
    country5 = st.selectbox(
        ' ', countries, index=58)

with col6:
    country3 = st.selectbox(
        ' ', countries, index=57)

with col6:
    country6 = st.selectbox(
        ' ', countries, index=65)

st.write(' ')
st.write(' ')

countries = [country1, country2, country3, country4, country5, country6]


sns.set_style("darkgrid")

plt.figure(figsize=(10,6))

for country in countries:

   country_data = df[df['country'] == country]
   melted_df = country_data.melt(id_vars='year', value_vars='GDP_per_capita')

   sns.lineplot(data=melted_df, x='year', y='value', label=country,
                ci=None, linestyle='-') # Remove CI and solid line

# Title
plt.title("Evolution of the Real GDP per Capita",
          fontsize=18, fontweight='bold',
          pad=20)


# Axis, labels (x and y)
plt.xlabel('Year', fontsize=14, fontweight='bold')
plt.ylabel('Real GDP per Capita in USD', fontsize=14, fontweight='bold')
plt.xlim(2000,2021)
plt.xticks(range(2000,2022, 3))# Format years
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

# Show legend
# Show legend
legend = plt.legend(loc='upper center',
                    ncol=len(countries), # Number of columns
                     fontsize=10) # Set font size

legend.get_frame().set_facecolor('white') # White background
legend.get_frame().set_edgecolor('black') # Black border

st.pyplot(plt)



# Clear figure
plt.clf()

















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

st.write('---')

st.markdown(f"""
<div style="text-align: center;font-size:28px;font-weight:bold;">
    Top Renewable 😁 Electricity production per Capita
</div> <br>
""", unsafe_allow_html=True)


years = tuple(range(2000, 2022))

year = st.selectbox(' ', years, index=21)

df['Renewable Energy'] = df['biofuel_elec_per_capita'] + df['hydro_elec_per_capita'] + df['solar_elec_per_capita'] + df['wind_elec_per_capita']
top_20 = df[df.year == year][['country', 'Renewable Energy']].sort_values(by='Renewable Energy', ascending=False).head(20)

import seaborn as sns
sns.barplot(y='country', x='Renewable Energy', data=top_20)


plt.xlabel("Total kWh in Renewable Electricity Production per Capita", fontsize=14, fontweight='bold')
plt.ylabel('Country', fontsize=14, fontweight='bold')
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

plt.title(f"Top 20 countries in Renewable Electricity production per Capita in {year}", fontsize=18, fontweight='bold')


st.pyplot(plt)







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

plt.clf()
st.write('---')

st.markdown(f"""
<div style="text-align: center;font-size:28px;font-weight:bold;">
    Top Non-Renewable 😞 Electricity production
</div> <br>
""", unsafe_allow_html=True)

years = tuple(range(2000, 2022))

year = st.selectbox(' ', years, index=20)

df['Non Renewable Energy'] = df['coal_elec_per_capita'] + df['gas_elec_per_capita'] + df['nuclear_elec_per_capita'] + df['oil_elec_per_capita']
top_20_non = df[df.year == year ][['country', 'Non Renewable Energy']].sort_values(by='Non Renewable Energy', ascending=False).head(20)

sns.barplot(y='country', x='Non Renewable Energy', data=top_20_non)


plt.xlabel("Total kWh in Non-Renewable Electricity Production per Capita", fontsize=14, fontweight='bold')
plt.ylabel('Country', fontsize=14)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

plt.title("Top 20 countries in Non-Renewable Electricity production per Capita.", fontsize=18, fontweight='bold')

st.pyplot(plt)
