import streamlit as st
import requests
import os
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

arr = np.random.normal(1, 3, size=100)


a = sns.histplot(arr, bins=4)

st.pyplot(a)
