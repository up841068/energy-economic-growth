import streamlit as st
import requests
import os
import pandas as pd


st.sidebar.image(os.getcwd() + "/energy_economy/interface/logo2.png", width=200)

# Title of the page with emojis
st.markdown(f"""
<div style="text-align: center;font-size:42px;font-weight:bold;">
     💡📈 Scenario Comparison 🔬💡
</div>
""", unsafe_allow_html=True)
st.write('---')

# Description with emojis
st.markdown(f"""
<div style="text-align: center;font-size:23px;font-weight:bold;">
    In this hypothetical scenario, you can compare the impact of each \
    energy source on GDP as a percentage difference. To conduct the comparison,\
        ensure that each scenario adds up to 💯%, and make subtle
        changes to observe their effect on the final result. <br>
</div>
""", unsafe_allow_html=True)

# Phrase below the title
# Define the chart HTML string
chart_html = """
<div id="viz1594170887248" style="position: relative; width: 100%; height: 0; padding-bottom: 66.67%;">
  <iframe src="https://ourworldindata.org/grapher/per-capita-electricity-generation?tab=map&stackMode=absolute&time=1965..2020&country=OWID_WRL" style="position: absolute; left: 0; top: 0; width: 100%; height: 100%;"></iframe>
</div>
"""
st.write('---')

st.markdown(f"""
<div style="text-align: center;font-size:20px;font-weight:bold;">
    Select the total amount of electricity (kWh) a country produces in one year. Use the global chart below as a reference ⚙️.
</div>
""", unsafe_allow_html=True)


energy_style = """
    font-size: 24px;
    font-weight: bold;
    color: #15753a;
"""

# Get the energy production value from the user
energy_production = st.slider(' ', 0, 42000, 3500)

# Display the energy production text with the custom style
st.write(f'<div style="{energy_style}">You selected total energy production per capita of: {energy_production}</div>', unsafe_allow_html=True)

st.write(' ')
st.write(' ')



# Display only the chart
st.components.v1.html(chart_html, height=600, width=780)

###################################
# Scenario Comparison
###################################

### SELECT THE % DISTRIBUTION PER ENERGY SOURCE
st.write('---')
st.markdown(f"""
<div style="text-align: center;font-size:23px;font-weight:bold;">
    Selecting percentage of production per energy source 🔋⚡️💡
</div>
""", unsafe_allow_html=True)


st.text(' ')

# Add titles for inputs
col1, col2, col3 = st.columns(3)
col1.markdown(f"""
<div style="text-align: center;font-size:23px;font-weight:bold;">
    Energy source ⚡️
</div>
""", unsafe_allow_html=True)
col2.markdown(f"""
<div style="text-align: center;font-size:23px;font-weight:bold;">
    Scenario 1 📃
</div>
""", unsafe_allow_html=True)
col3.markdown(f"""
<div style="text-align: center;font-size:23px;font-weight:bold;">
    Scenario 2 📃
</div>
""", unsafe_allow_html=True)

st.text(' ')

# val = st.slider('Percentage Input',min_value=0, max_value=100, key='val')

# val2 = st.slider('Percentage Input',min_value=0, max_value=100, key='val2')


# Add Coal inputs
col1_coal, col2_coal, col3_coal = st.columns(3)

col1_coal.markdown(f"""
<div style="text-align: center;font-size:23px;font-weight:bold;">
    <br> Coal 🪨
</div>
""", unsafe_allow_html=True)

coal_sc1 = col2_coal.number_input('', value=10.0, step=1.0, format='%.2d', key='coal_sc1')/100
coal_sc2 = col3_coal.number_input('', value=10.0, step=1.0, format='%.2d', key='coal_sc2')/100


# Add Oil inputs
col1_oil, col2_oil, col3_oil = st.columns(3)
col1_oil.markdown(f"""
<div style="text-align: center;font-size:23px;font-weight:bold;">
    <br> Oil 🛢️
</div>
""", unsafe_allow_html=True)
oil_sc1 = col2_oil.number_input('', value=20.0, step=1.0, format='%.2d', key='oil_sc1')/100
oil_sc2 = col3_oil.number_input('', value=20.0, step=1.0, format='%.2d', key='oil_sc2')/100


# Add Gas inputs
col1_gas, col2_gas, col3_gas = st.columns(3)
col1_gas.markdown(f"""
<div style="text-align: center;font-size:23px;font-weight:bold;">
    <br> Gas 💨
</div>
""", unsafe_allow_html=True)
gas_sc1 = col2_gas.number_input('', value=10.0, step=1.0, format='%.2d', key='gas_sc1')/100
gas_sc2 = col3_gas.number_input('', value=10.0, step=1.0, format='%.2d', key='gas_sc2')/100


# Add Nuclear inputs
col1_nuc, col2_nuc, col3_nuc = st.columns(3)
col1_nuc.markdown(f"""
<div style="text-align: center;font-size:23px;font-weight:bold;">
    <br> Nuclear ☢️
</div>
""", unsafe_allow_html=True)
nuc_sc1 = col2_nuc.number_input('', value=10.0, step=1.0, format='%.2d', key='nuc_sc1')/100
nuc_sc2 = col3_nuc.number_input('', value=10.0, step=1.0, format='%.2d', key='nuc_sc2')/100


# Add Biofuel inputs
col1_bio, col2_bio, col3_bio = st.columns(3)
col1_bio.markdown(f"""
<div style="text-align: center;font-size:23px;font-weight:bold;">
    <br> Biofuel 🌽
</div>
""", unsafe_allow_html=True)
bio_sc1 = col2_bio.number_input('', value=10.0, step=1.0, format='%.2d', key='bio_sc1')/100
bio_sc2 = col3_bio.number_input('', value=10.0, step=1.0, format='%.2d', key='bio_sc2')/100

# Add Hydro inputs
col1_hyd, col2_hyd, col3_hyd = st.columns(3)
col1_hyd.markdown(f"""
<div style="text-align: center;font-size:23px;font-weight:bold;">
    <br> Hydro 💧
</div>
""", unsafe_allow_html=True)
hyd_sc1 = col2_hyd.number_input('', value=20.0, step=1.0, format='%.2d', key='hyd_sc1')/100
hyd_sc2 = col3_hyd.number_input('', value=20.0, step=1.0, format='%.2d', key='hyd_sc2')/100

# Add Solar inputs
col1_sol, col2_sol, col3_sol = st.columns(3)
col1_sol.markdown(f"""
<div style="text-align: center;font-size:23px;font-weight:bold;">
    <br> Solar ☀️
</div>
""", unsafe_allow_html=True)
sol_sc1 = col2_sol.number_input('', value=10.0, step=1.0, format='%.2d', key='sol_sc1')/100
sol_sc2 = col3_sol.number_input('', value=10.0, step=1.0, format='%.2d', key='sol_sc2')/100


# Add Wind inputs
col1_win, col2_win, col3_win = st.columns(3)
col1_win.markdown(f"""
<div style="text-align: center;font-size:23px;font-weight:bold;">
    <br> Wind 🌬️
</div>
""", unsafe_allow_html=True)
win_sc1 = col2_win.number_input('', value=10.0, step=1.0, format='%.2d', key='win_sc1')/100
win_sc2 = col3_win.number_input('', value=10.0, step=1.0, format='%.2d', key='win_sc2')/100


total_sc1 = round((coal_sc1 + gas_sc1 + oil_sc1 + nuc_sc1 + bio_sc1 + win_sc1 + sol_sc1 + hyd_sc1)*100)
total_sc2 = round((coal_sc2 + gas_sc2 + oil_sc2 + nuc_sc2 + bio_sc2 + win_sc2 + sol_sc2 + hyd_sc2)*100)



col1, col2, col3 = st.columns(3)
col1.write(' ')
if total_sc1 == 100:
    col2.write(f'**✅ You have selected {total_sc1}%**')
else:
    col2.write(f'**❌ You have selected {total_sc1}%, please adjust to 100%**')
if total_sc2 == 100:
    col3.write(f'**✅ You have selected {total_sc2}%**')
else:
    col3.write(f'**❌ You have selected {total_sc2}%, please adjust to 100%**')
st.text(' ')



### GET THE PREDICTION VALUE FROM THE API USING THE INPUTS

coal_sc1_abs = coal_sc1*energy_production
oil_sc1_abs = oil_sc1*energy_production
gas_sc1_abs = gas_sc1*energy_production
hyd_sc1_abs = hyd_sc1*energy_production
nuc_sc1_abs = nuc_sc1*energy_production
bio_sc1_abs = bio_sc1*energy_production
sol_sc1_abs = sol_sc1*energy_production
win_sc1_abs = win_sc1*energy_production

coal_sc2_abs = coal_sc2*energy_production
oil_sc2_abs = oil_sc2*energy_production
gas_sc2_abs = gas_sc2*energy_production
hyd_sc2_abs = hyd_sc2*energy_production
nuc_sc2_abs = nuc_sc2*energy_production
bio_sc2_abs = bio_sc2*energy_production
sol_sc2_abs = sol_sc2*energy_production
win_sc2_abs = win_sc2*energy_production

prediction_sc1 = requests.get(f'https://my-api-ribizrrcua-ew.a.run.app/predict?coal_elec_per_capita={coal_sc1_abs}&oil_elec_per_capita={oil_sc1_abs}&gas_elec_per_capita={gas_sc1_abs}&hydro_elec_per_capita={hyd_sc1_abs}&nuclear_elec_per_capita={nuc_sc1_abs}&biofuel_elec_per_capita={bio_sc1_abs}&solar_elec_per_capita={sol_sc1_abs}&wind_elec_per_capita={win_sc1_abs}')

prediction_sc2 = requests.get(f'https://my-api-ribizrrcua-ew.a.run.app/predict?coal_elec_per_capita={coal_sc2_abs}&oil_elec_per_capita={oil_sc2_abs}&gas_elec_per_capita={gas_sc2_abs}&hydro_elec_per_capita={hyd_sc2_abs}&nuclear_elec_per_capita={nuc_sc2_abs}&biofuel_elec_per_capita={bio_sc2_abs}&solar_elec_per_capita={sol_sc2_abs}&wind_elec_per_capita={win_sc2_abs}')

st.write('---')

import streamlit as st

# COMPARES THE SCENARIOS AND OUTPUTS THE ANSWER TO THE USER
if prediction_sc1.json()['result'] > prediction_sc2.json()['result']:
    per_diff = (prediction_sc1.json()['result']/prediction_sc2.json()['result'] - 1)*100
    st.markdown(f"""
        <div style="text-align:center;font-size:28px;">
            Based on the allocation of energy sources for total production, the <b>first scenario</b> would represent a GDP per capita <b>{round(per_diff, 2)}%</b> greater than the <b>second scenario</b> 🚀👍
        </div>
    """, unsafe_allow_html=True)

elif prediction_sc2.json()['result'] > prediction_sc1.json()['result']:
    per_diff = (prediction_sc2.json()['result']/prediction_sc1.json()['result'] - 1)*100
    st.markdown(f"""
        <div style="text-align:center;font-size:28px;">
            Based on the allocation of energy sources for total production, the <b>second scenario</b> would represent a GDP per capita <b>{round(per_diff, 2)}%</b> greater than the <b>first scenario</b> 🚀👍
        </div>
    """, unsafe_allow_html=True)

else:
    st.markdown(f"""
        <div style="text-align:center;font-size:28px;">
            Both scenarios are equal! 🤝
        </div>
    """, unsafe_allow_html=True)

# Add a space line
st.text(' ')
st.text(' ')
st.text(' ')









# year = st.selectbox(
#     'The prediction up to which year?',
#     ('2030', '2040', '2050'))


# prediction = f'https://my-api-svzr7rwnfa-ew.a.run.app/predict?day_of_week={year}'

# prediction_ok = requests.get(prediction)

# st.write(f'The prediction for the year {year} is:', prediction_ok.json()['wait'])


# # Check if the request was successful
# if response.ok:
#     # Display the JSON response using the st.write() function
#     st.write(response.json())
# else:
#     # Display an error message if the request failed
#     st.error('Opssss...failed to retrieve data from API. Have a coffee and sort it :D')
