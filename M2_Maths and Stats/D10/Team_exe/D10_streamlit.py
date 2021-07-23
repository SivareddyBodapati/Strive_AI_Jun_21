import pandas as pd
import numpy as np
import pydeck as pdk
import streamlit as st
import streamlit.components.v1 as components
# import matplotlib.pyplot as plt
import plotly.express as px

st.set_option('deprecation.showPyplotGlobalUse', False)

st.title("Investment opportunities in Amsterdam post Covid-19")

# df = pd.read_csv(r"Public_Facing_Costumers_Data.csv", usecols=['latitude', 'longitude'], encoding="utf-8").dropna()
df = pd.read_csv(r"Public_Facing_Costumers_Data.csv", encoding="utf-8")
dfp = df[['longitude', 'latitude']].dropna()

# st.pydeck_chart(pdk.Deck(
#     map_style='mapbox://styles/mapbox/dark-v9',
#     initial_view_state=pdk.ViewState(
#         longitude=4.877781,
#         latitude=52.3665828,
#         zoom=11,
#         pitch=50,
#     ),
#     layers=[
#         pdk.Layer(
#             'HexagonLayer',
#             data=dfp,
#             get_position='[longitude, latitude]',
#             radius=200,
#             elevation_scale=1.5,
#             elevation_range=[0, 4000],
#             pickable=False,
#             extruded=True,
#             coverage=0.5
#         ),
#         pdk.Layer(
#             'ScatterplotLayer',
#             data=dfp,
#             get_position='[longitude, latitude]',
#             get_color='[200, 30, 0, 160]',
#             get_radius=150,
#         ),
#     ],
# ))

filter_list = st.multiselect(
    '', 
    ['Bar',
    'Club',
    'Coffee shop',
    'Hotel',
    'Museum',
    'Park',
    'Pub',
    'Restaurant',
    'Shopping'],
    default=['Bar', 'Club', 'Coffee shop', 'Hotel', 'Museum', 'Park', 'Pub', 'Restaurant', 'Shopping']
)

dfp = dfp[df['category'].isin(filter_list)]

st.pydeck_chart(pdk.Deck(
    map_style='mapbox://styles/mapbox/dark-v9',
    initial_view_state=pdk.ViewState(
        longitude=4.877781,
        latitude=52.3665828,
        zoom=11,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
            'HexagonLayer',
            data=dfp,
            get_position='[longitude, latitude]',
            radius=200,
            elevation_scale=1.5,
            elevation_range=[0, 4000],
            pickable=False,
            extruded=True,
            coverage=0.5
        ),
        pdk.Layer(
            'ScatterplotLayer',
            data=dfp,
            get_position='[longitude, latitude]',
            get_color='[200, 30, 0, 160]',
            get_radius=150,
        ),
    ],
))

components.html(
    """
    <div class='my-legend'>
        <div class='legend-title'>Legend</div>
        <div class='legend-scale'>
            <ul class='legend-labels'>
                <li style="color:#FFFFFF;"><span style='background:#d2d293; margin-bottom: 8px;'></span>20%</li>
                <li style="color:#FFFFFF;"><span style='background:#daba66; margin-bottom: 8px;'></span>40%</li>
                <li style="color:#FFFFFF;"><span style='background:#d79741; margin-bottom: 8px;'></span>60%</li>
                <li style="color:#FFFFFF;"><span style='background:#d73c25; margin-bottom: 8px;'></span>80%</li>
                <li style="color:#FFFFFF;"><span style='background:#a10020; margin-bottom: 8px;'></span>100%</li>
            </ul>
        </div>
    </div>
<style type='text/css'>
    .my-legend .legend-title {
    text-align: left;
    margin-bottom: 8px;
    font-family: "Lucida Console"
    font-weight: bold;
    font-size: 120%;
    color: #FFFFFF;
    }
    .my-legend .legend-scale ul {
    margin: 0;
    padding: 0;
    float: left;
    list-style: none;
    }
    .my-legend .legend-scale ul li {
    display: block;
    float: left;
    width: 50px;
    margin-bottom: 6px;
    text-align: center;
    font-size: 80%;
    list-style: none;
    }
    .my-legend ul.legend-labels li span {
    display: block;
    float: left;
    height: 15px;
    width: 50px;
    }
    .my-legend .legend-source {
    font-size: 70%;
    color: #999;
    clear: both;
    }
    .my-legend a {
    color: #777;
    }
    </style>
    """)

x = df.groupby('category')['category'].count().index.tolist()
y = df.groupby('category')['category'].count().tolist()
df_pie = pd.DataFrame(list(zip(x, y)), columns=['Category', 'Number'])
fig1 = px.pie(df_pie, values='Number', names='Category', title='Distribution of commercial activities')
# fig1.show()
st.plotly_chart(fig1)