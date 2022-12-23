import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the Next Days")
location = st.text_input("Location")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of forecasted days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {location}")

if location:
    try:
        # Get the temperature/sky data
        filtered_weather_values = get_data(location, days)

        if option == "Temperature":
            temperatures = [temp_obs["main"]["temp"] / 10 for temp_obs in filtered_weather_values]
            dates = [temp_obs["dt_txt"] for temp_obs in filtered_weather_values]
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature"})
            st.plotly_chart(figure)
        if option == "Sky":
            images = {
                "Clear": "images/clear.png",
                "Clouds": "images/clouds.png",
                "Rain": "images/rain.png",
                "Snow": "images/snow.png"
            }
            sky_conditions = [temp_obs["weather"][0]["main"] for temp_obs in filtered_weather_values]
            sky_images = [images[sky_condition] for sky_condition in sky_conditions]
            print(sky_images)
            st.image(sky_images, width=115)
    except KeyError:
        st.write("Please enter a valid city")
