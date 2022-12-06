# %%
import pandas as pd 
import math
import numpy as np
import requests
import matplotlib.pyplot as plt 
import seaborn as sns 
import json
import time

import folium
from folium  import plugins
from folium import features
from streamlit_folium import st_folium 
from streamlit_option_menu import option_menu
# from folium.plugins import MarkerCluster
# from folium.plugins import HeatMap

import plotly.express as px 
# import pymysql
# from sqlalchemy import create_engine
# import mysql.connector


import streamlit as st 
import streamlit.components.v1 as components

# %%




# /**************************************  css streamlit **************************************/
st.markdown('<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.1/css/all.min.css" rel="stylesheet" >', 
            unsafe_allow_html=True)
with open('style/style.css') as css:
    st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html=True)



# create the menu container

with st.container():
    st.image("images/mappysmile.png")
    
    
    
    link_to_home = 'https://karimdevweb-mappysmile-bord-eau-accueil-mt8rru.streamlit.app/accueil'
    link_to_live ='https://karimdevweb-mappysmile-bord-eau-accueil-mt8rru.streamlit.app/check_on_live'
    link_to_plan ='https://karimdevweb-mappysmile-bord-eau-accueil-mt8rru.streamlit.app/plan_your_trip'
    link_to_correlation ='https://karimdevweb-mappysmile-bord-eau-accueil-mt8rru.streamlit.app/distribution_graph'

    st.markdown(f"<div class='menu_div'>\
                    <a target='_self' href='{link_to_home}' class='menu_link selected_menu'><div class='button_div'> Accueil</div></a>\
                    <a target='_self' href='{link_to_live}' class='menu_link live_transport'><div class='button_div'>Live Transport</div></a>\
                    <a target='_self' href='{link_to_plan}' class='menu_link planning_transport'><div class='button_div'>Palnning a trip</div></a>\
                    <a target='_self' href='{link_to_correlation}' class='menu_link correlation'><div class='button_div'>Distribution</div></a>\
                </div>",
                unsafe_allow_html=True)








    
        
st.image('images/bordeaux.gif')



st.subheader('description of this app')

st.markdown("<div class='plan_example_div'>\
                <p><b>this application show the trafic situation in Bordeau (France): </b></p>\
                <p> It showing Vcub / Bus & Ship / Trafic tendance on live , it could help you to plan your future trip if you check the status at the given address at the given time and day of the week: </p>\
                <ul>\
                    <li>for a  given address</li>\
                    <li>you can choose to check Friday for exemple</li>\
                    <li>the trafic from 10 to 12 AM</li>\
                    <li>only for bikes  or/and bus ...</li>\
                </ul>\
                <p>data collecting process:</p>\
                <ul>\
                    <li>14 days 24/24 of calling the 3 APIs every 10mn</li>\
                    <li>tidyng the data, then store after every call into a sql database</li>\
                    <li>1 database, 5 db.tables, 1.000.000 rows</li>\
                    <li>tidying the data(drop, merge, converting type...)</li>\
                    <li>programming a code  to calculate the tendance & status for the 3 transport conveyance </li>\
                    <li>expolte the result  either  in maps or in plotly graph </li>\
                </ul>\
            </div>", unsafe_allow_html=True)

st.markdown('----------------')
            


 


 
 
