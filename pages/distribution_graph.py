import pandas as pd 
import math
import numpy as np
import requests
import matplotlib.pyplot as plt 
import seaborn as sns 
import json
import time


from geopy.geocoders import Nominatim
from geopy.point import Point
import geopandas as gpd
from pathlib import Path  



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
import schedule









# /**************************************  css streamlit **************************************/

st.markdown('<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.1/css/all.min.css" rel="stylesheet" >', 
            unsafe_allow_html=True)
with open('style/style.css') as css:
    st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html=True)




# create the dashboard


with st.container():
    st.image("images/mapysmile.png")
    
    link_to_home = 'http://localhost:8501/'
    link_to_live ='http://localhost:8501/check_on_live'
    link_to_plan ='http://localhost:8501/plan_your_trip'
    link_to_correlation ='http://localhost:8501/distribution_graph'

    st.markdown(f"<div class='menu_div'>\
                    <a target='_self' href='{link_to_home}' class='menu_link'><div class='button_div'> Accueil</div></a>\
                    <a target='_self' href='{link_to_live}' class='menu_link live_transport  '><div class='button_div'>Live Transport</div></a>\
                    <a target='_self' href='{link_to_plan}' class='menu_link planning_transport '><div class='button_div'>Palnning a trip</div></a>\
                    <a target='_self' href='{link_to_correlation}' class='menu_link correlation selected_menu'><div class='button_div'>Distribution</div></a>\
                </div>",
                unsafe_allow_html=True)





 
st.title("")
st.subheader('map and bar graphs showing the distribution of transport, Vcub disponibility and trafic situation ')



st.markdown('----------------')






# /*************************************** 1- draw  a chloropleth map , divided by region  *****************************************************************/
# /*************************************** i'm just adding this code  for info, since i 'll use the csv file  at the end of this section   *****************************************************************/

# # 1.1 get first all data after tidyed and grouped
#  all_dfs_after_grouping = calling_filtering_func(True,False,False,False)




# # 1.2 read the gojson file for extracting the insee code
# bordeaux_geo = 'communes bordeaux.geojson'

# df = gpd.read_file(bordeaux_geo)
# insee_code = df[['insee','nom']].reset_index()
# insee_code['insee'] = insee_code['insee'].astype(np.int64)



# # get all data after filtering
# all_dfs_after_grouping = calling_filtering_func(True,False,False,False)


# # 7.2.1 merge first the dataframe with the insee series
# def merge_vcub_with_insee_code_func(dataframe):
#     vcub_pstCode_chplIndex = dataframe['vcub'][['quartier','post_code','chloropleth_index','day']]

#     vcub_insee_df = pd.merge(vcub_pstCode_chplIndex,insee_code, left_on='post_code', right_on='insee', how='inner')
#     return vcub_insee_df



# # 1.3 merge second the dataframe with the insee series
# def merge_trafic_with_insee_code_func(dataframe):
#     trafic_pstCode_chplIndex = dataframe['trafic'][['city','postal_code','chloropleth_index','day']]
#     trafic_pstCode_chplIndex.sort_values(by='city', ascending=True)

#     trafic_insee_df = pd.merge(trafic_pstCode_chplIndex,insee_code, left_on='postal_code', right_on='insee', how='inner')
#     return trafic_insee_df

# # 1.4 merge second the dataframe with the insee series
# def merge_trafic_with_insee_code_func(dataframe):
#     trafic_pstCode_chplIndex = dataframe['trafic'][['city','postal_code','chloropleth_index','day']]
#     trafic_pstCode_chplIndex.sort_values(by='city', ascending=True)

#     trafic_insee_df = pd.merge(trafic_pstCode_chplIndex,insee_code, left_on='postal_code', right_on='insee', how='inner')
#     return trafic_insee_df






# # 1.5 merge third the dataframe with the insee series


# # initialize Nominatim API
# geolocator = Nominatim(user_agent="geoapiExercises")


# # Latitude & Longitude input
# # Latitude = "44.905497"		
# # Longitude = "-0.714831"
# # find_city = Latitude+","+Longitude

# # location = geolocator.reverse(find_city)

# # # Display city = address.get('city','')
# # address = location.raw['address']
# # postcode =address.get('postcode','')
# # address['postcode']

# # create function to find the post code

# def finding_post_code(lat,lon):
#     latitude = str(lat)
#     longitude = str(lon)
#     find_city = latitude+","+longitude
#     location = geolocator.reverse(find_city)
#     address = location.raw['address']
#     postcode =address.get('postcode','')
#     return postcode


# def merge_transport_with_insee_code_func(dataframe):
#     # first get postcode for all bus station 
#     transport_pstCode_chplIndex = dataframe['transport']
#     transport_pstCode_chplIndex
#     # apply_function 
#     # transport_pstCode_chplIndex = transport_pstCode_chplIndex.assign(post_code = lambda x: finding_post_code(x['lat'], x['lon']))
#     transport_pstCode_chplIndex['post_code'] = np.vectorize(finding_post_code)(transport_pstCode_chplIndex['lat'],transport_pstCode_chplIndex['lon'])

#     # 7.2.4 drop all empty post_code raws
#     transport_pstCode_chplIndex[transport_pstCode_chplIndex['post_code'] == ''].index.to_list()
#     transport_pstCode_chplIndex.drop(index= transport_pstCode_chplIndex[transport_pstCode_chplIndex['post_code'] == ''].index.to_list(), inplace=True )

#     # convert objct type into int
#     transport_pstCode_chplIndex['post_code'] = transport_pstCode_chplIndex['post_code'].astype(np.int64)

#     # we can merge the two dfs throught postcode
#     transport_insee  =  pd.merge(transport_pstCode_chplIndex, insee_code, left_on='post_code',right_on='insee', how='inner')
#     # i need lat, lon , and post_code not already created, cause i'm droping here and not call only the few i need over [['lat'....]]
#     transport_insee.drop(columns=['gid','lat','lon','terminus','status','symbole','vehicule','status_color','index'],inplace=True)
#     return transport_insee


# # call the function for tidying and merging with the insee code df
# if 'vcub' in all_dfs_after_grouping.keys():
#     vcub_insee_df = merge_vcub_with_insee_code_func(all_dfs_after_grouping)
    
# if 'trafic' in all_dfs_after_grouping.keys():
#     trafic_insee_df= merge_trafic_with_insee_code_func(all_dfs_after_grouping)

# if 'transport' in all_dfs_after_grouping.keys():
#     transport_insee_df = merge_transport_with_insee_code_func(all_dfs_after_grouping)
    
    
    
    
# # 1.6 grouping the df_with_insee_code for all transport /vcub / trafic

# grouped_vcub_with_insee = vcub_insee_df.groupby(['insee'], as_index=False).agg(chloropleth_vcub_index = ('chloropleth_index',lambda x : x.mode()[0]),
#                                                                                commune_name = ('nom','first'))
# grouped_trafic_with_insee = trafic_insee_df.groupby(['insee'], as_index=False).agg(chloropleth_trafic_index = ('chloropleth_index',lambda x : x.mode()[0]))
# grouped_transport_with_insee = transport_insee_df.groupby(['insee'], as_index=False).agg(chloropleth_transport_index = ('chloropleth_index',lambda x : x.mode()[0]))

# # 1.7 merge all dfs
# merged_dfs_for_chloropleth_map = pd.merge(pd.merge(grouped_vcub_with_insee,grouped_trafic_with_insee, on='insee', how='outer'),grouped_transport_with_insee, on='insee', how='outer')
# merged_dfs_for_chloropleth_map['sum_for_chloropleth_map'] = merged_dfs_for_chloropleth_map[['chloropleth_vcub_index','chloropleth_trafic_index','chloropleth_transport_index']].sum(axis=1,skipna=True)
# # convert the insee key into str, for matching with str isee_key in geojson 
# merged_dfs_for_chloropleth_map['insee'] = merged_dfs_for_chloropleth_map['insee'].astype(str)


# merged_dfs_for_chloropleth_map.fillna(value=0, inplace=True)
# merged_dfs_for_chloropleth_map = merged_dfs_for_chloropleth_map[['insee','commune_name','chloropleth_vcub_index','chloropleth_trafic_index','chloropleth_transport_index','sum_for_chloropleth_map']]

# merged_dfs_for_chloropleth_map

# here i save  my result into csv file, in order to get the info more easier

# filepath = Path('csv_geojson/df_for_chloropleth_map.csv')  
# filepath.parent.mkdir(parents=True, exist_ok=True)  
# merged_dfs_for_chloropleth_map.to_csv(filepath)  




# /********************    2 draw  a chloropleth map with region dilimitation       *******************************/

tab1,tab2,tab3,tab4 = st.tabs(['Regional View', 'Vcub', 'Trafic','Transport'])



city_from_csv = pd.read_csv('csv_files/df_for_chloropleth_map.csv',sep=',')
city_from_csv.drop(columns=['Unnamed: 0'], inplace= True)
city_from_csv['insee'] = city_from_csv['insee'].astype(str)


# chloroplèthe map
bordeaux_geo = 'csv_files/communes_bordeaux.geojson'

my_geo_map = folium.Map(location=[44.837789,-0.57918],
                        zoom_start=10,
                        width=700,
                        height=700)



chloropleth_map = folium.Choropleth(geo_data=bordeaux_geo,
                                    name="choropleth",
                                    data=city_from_csv,
                                    columns=["insee", "sum_for_chloropleth_map"],
                                    key_on="feature.properties.insee",
                                    fill_color="BuPu",
                                    fill_opacity=0.7,
                                    line_opacity=0.2,
                                    legend_name="availabness of vehicle",
                  )
                    
chloropleth_map.geojson.add_child(
    folium.features.GeoJsonTooltip(['nom'])
)
chloropleth_map.add_to(my_geo_map)

with tab1: 
    st.write('map showing the region where the traffic / transport and Vcub stations are more affected (jam traffic, late transport, less vcub disponible)') 
    st_folium(my_geo_map,width= 700, height=500)

    st.markdown("<div class='explanation_example_div'>\
                    <p><b>explanation: </b></p>\
                    <p>after the analysis of the 3 datasets got from APIs, i could affect a score for each transport conveyance, then calculate the distribution throught regions in Bordeaux </p>\
                    <ul>\
                        <li>with this basis, we notice that most of region has no perturbation neither in traffic nor in Vcub </li>\
                        <li>but in le Haillan, like we see, has the big score: we can deduce that the business area is located there and more persons use this road and go in this direction.</li>\
                        <li>the consequence is that Vcub are less available there, traffic is frequently in jam status and buses are late. </li>\
                    </ul>\
                </div>", unsafe_allow_html=True)


#  /********************************************************************************************************************************/
# /************************************  draw bar graph for the third dfs trafic / transport / vcub **************************************************/


#  get direct the data from csv, not from database
station_status = pd.read_csv('csv_files/df_stations_info.csv')
vcub_status = pd.read_csv('csv_files/df_stations_status_29_11_2022.csv')
trafic_status = pd.read_csv('csv_files/table_trafic_avec_wknd.csv')
transport_status = pd.read_csv('csv_files/table_transport_avec_wknd.csv')



def tidying_all_dfs(station_status,vcub_status,trafic_status,transport_status):
    vcub_data = pd.merge(station_status,vcub_status, how='inner', on='station_id')
    vcub_data.drop(columns=['index'], inplace=True)
    vcub_data['station_id'] = vcub_data['station_id'].astype(np.int64)
    vcub_data['post_code'] = vcub_data['post_code'].astype(np.int64)
    vcub_data['last_reported'] = pd.to_datetime(vcub_data['last_reported'])
    vcub_data['date'] = vcub_data['last_reported'].dt.date
    vcub_data['day'] = vcub_data['last_reported'].dt.day_name()
    vcub_data['hour'] = vcub_data['last_reported'].dt.hour


    trafic_status.drop(columns=['index','fields.cdate','fields.mdate'], inplace=True )
    trafic_status.rename(columns= {
                                    'record_timestamp' : 'date',
                                    'fields.typevoie' : 'road',
                                    'fields.etat': 'status'	,
                                    'fields.code_commune' :'postal_code',
                                    'fields.commune' : 'city',
                                    'fields.gid' : 'gid',
                                    'lat' : 'lat',
                                    'lon' :'lon',
                                    1 : 'lat_for_road',
                                    0 : 'lon_for_road',
                                },inplace=True)

    # 2.2.2 change type & add day and hour columns 
    trafic_status['status'] = trafic_status['status'].astype('category')
    trafic_status['postal_code'] = trafic_status['postal_code'].astype(np.int64)
    trafic_status['gid'] = trafic_status['gid'].astype(np.int64)
    trafic_status['date'] = pd.to_datetime(trafic_status['date'], format='%Y-%m-%d %H:%M:%S')

    trafic_status['day'] = trafic_status['date'].dt.day_name()
    trafic_status['date_day'] = trafic_status['date'].dt.date
    trafic_status['hour'] = trafic_status['date'].dt.hour



    transport_status.drop(columns=['fields.cdate','fields.mdate','fields.statut','fields.rs_sv_ligne_a','fields.arret','index'], inplace=True)

    # 2.3.2 rename columns and change the type
    transport_status.rename(columns={
                            'index' : 'index',             
                            'record_timestamp' :'date',
                            'fields.etat' : 'status',
                            'fields.vehicule' : 'vehicule',
                            'fields.gid' : 'gid',
                            'fields.retard' : 'late_status',
                            'fields.terminus' : 'terminus',
                            'fields.sens' :'direction',
                            'lat' : 'lat',
                            'lon' :'lon'
                        }, inplace=True)



    transport_status['status'] = transport_status['status'].astype('category') 
    transport_status['vehicule'] = transport_status['vehicule'].astype('category') 
    transport_status['late_status'] = transport_status['late_status'].astype('category') 
    transport_status['date'] = pd.to_datetime(transport_status['date'])
    transport_status['day'] = transport_status['date'].dt.day_name()
    transport_status['hour'] = transport_status['date'].dt.hour
    transport_status['date_day'] = transport_status['date'].dt.date
    transport_status['symbole'] = transport_status['vehicule'].apply(lambda x: 'bus' if (x =='BUS') else 'train' if (x=='TRAM_LONG' or x =='TRAM_COURT') else 'ship')

    return vcub_data,trafic_status,transport_status



vcub_trafic_trasnport_dfs = tidying_all_dfs(station_status,vcub_status,trafic_status,transport_status)



# get one  by pne df after tidyed
vcub_for_graph = vcub_trafic_trasnport_dfs[0]
trafic_for_graph = vcub_trafic_trasnport_dfs[1]
transport_for_graph = vcub_trafic_trasnport_dfs[2]

# 3 group all dfs by station_id
grouped_vcub = vcub_for_graph.groupby(['post_code','day'], as_index=False).agg(lat = ('lat','first'),
                                                          lon = ('lon', 'first'),
                                                          capacity = ('capacity','first'),
                                                          name = ('name','first'),
                                                         
                                                          num_bikes_available = ('num_bikes_available','mean'),
                                                          num_docks_available = ('num_docks_available','mean'),
                                                          taux_remplissage = ('taux_remplissage_%','mean'),
                                                          taux_utilisation = ('taux_utilisation_%','mean'),
                                                          )
grouped_trafic = trafic_for_graph.groupby(['gid','day'], as_index=False).agg(lat = ('lat','first'),
                                                          lon = ('lon', 'first'),
                                                          city = ('city','first'),
                                                          status = ('status', lambda x : x.mode()[0]),
                                                          )
grouped_transport= transport_for_graph.groupby(['gid','day'], as_index=False).agg(lat = ('lat','first'),
                                                          lon = ('lon', 'first'),
                                                          symbole = ('symbole','first'),                                               
                                                          status = ('status', lambda x : x.mode()[0]),
                                                          )




# gat the city name from geojson and merge it  with vcub df
city_from_csv['insee'] = city_from_csv['insee'].astype(np.int64)

vcub_and_cities = pd.merge(city_from_csv, grouped_vcub , left_on='insee', right_on='post_code', how='inner')





# make a scatter mapbox to draw the vcub filling rate
vcub_bar_plot= px.bar(vcub_and_cities,
                                x='commune_name',
                                y='capacity', 
                            )
vcub_bar_plot.update_layout(title_text='bar plot showing the distribution of the vcub bikes throught regions', title_x=0.5)
vcub_bar_plot.update_layout(xaxis_title='regions')
with tab2:  
    st.plotly_chart(vcub_bar_plot)
    st.markdown("<div class='explanation_example_div'>\
                    <p><b>explanation: </b></p>\
                    <p>In this graph we can esealy resume, with help of the region map, that the diustribution of Vcubs are not effiecently distribued</p>\
                    <ul>\
                        <li>In le Haillan, for exemple , the average capacity is up to 16 bikes</li>\
                        <li>In other side Talence and Cenon have more than 30 bikes in average</li>\
                        <li>the city of Bordeaux should take mesurements and find solution to upgrade the capacity in this region , and unclog the traffic</li>\
                    </ul>\
                </div>", unsafe_allow_html=True)



# bar plot for the grouped_trafic dataframe
trafic_bar_plot = px.bar(grouped_trafic, 
                  x='status',
                  color='status',
                  )
trafic_bar_plot.update_layout(title_text='bar plot showing the number of time the traffic are jam, thick or free flowing', title_x=0.5)
trafic_bar_plot.update_layout(yaxis_title='occurence number')


with tab3:  
    st.plotly_chart(trafic_bar_plot)
    st.markdown("<div class='explanation_example_div'>\
                    <p><b>explanation: </b></p>\
                    <p>globaly the traffic in Bordeaux and its surroundings are free flowing,  despite that captors send an 'unknown' status frequently.</p>\
                    <p>the little time we receive a jam or thicky status from the captor, happens mostly at peak hour </p>\
                </div>", unsafe_allow_html=True)






# bar plot for the transport dataframe
transport_bar_plot = px.bar(grouped_transport, 
                  x='status',
                  color='symbole',
                  
                  )
transport_bar_plot.update_layout(title_text='bar plot showing the number  of time the transport are on time, late or even ahead of time', title_x=0.5)
transport_bar_plot.update_layout(yaxis_title='occurence number')



with tab4:  
    st.plotly_chart(transport_bar_plot)
    st.markdown("<div class='explanation_example_div'>\
                    <p><b>explanation: </b></p>\
                    <p>mostly the transport are fast always on time.</p>\
                    <p>the bus are more likely to be late since train are on rail and not depending of traffic situation</p>\
                </div>", unsafe_allow_html=True)


