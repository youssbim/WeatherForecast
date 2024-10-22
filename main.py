import streamlit as st
import plotly.express as px
from backend import get_data

# Set up page configuration for a better look
st.set_page_config(page_title="Weather Forecast", page_icon="🌤️", layout="wide")

# Title and Description
st.title("🌦️ Weather Forecast")
st.markdown("Get the weather forecast for the next few days. Choose your location, select the forecast period, and see the expected temperatures or sky conditions.")

# User Input
place = st.text_input("Enter a Location:", placeholder="e.g., New York")
days = st.slider("Select Forecast Days:", min_value=1, max_value=5, help="Choose the number of days to see the forecast.")
option = st.selectbox("Choose Data to Display:", ("Temperature", "Sky Conditions"))
st.subheader(f"Weather Forecast: {option} for the Next {days} Days in {place}")

# Process and Display Data
if place:
    try:
        filtered_data = get_data(place, days)
        dates = [d["dt_txt"] for d in filtered_data]

        if option == "Temperature":
            temperatures = [d["main"]["temp"] / 10 for d in filtered_data]
            figure = px.line(
                x=dates, y=temperatures,
                labels={"x": "Date", "y": "Temperature (°C)"},
                title=f"Temperature Trend for the Next {days} Days in {place}"
            )
            figure.update_layout(xaxis_tickangle=-45, template="plotly_white")
            st.plotly_chart(figure, use_container_width=True)

        elif option == "Sky Conditions":
            images = {
                "clear": "images/clear.png",
                "clouds": "images/cloud.png",
                "rain": "images/rain.png",
                "snow": "images/snow.png"
            }

            sky_conditions = [d["weather"][0]["main"].lower() for d in filtered_data]
            image_paths = [images.get(condition, "images/default.png") for condition in sky_conditions]

            st.write("### Sky Conditions Overview:")
            for i in range(0, len(dates), 3):
                cols = st.columns(3)

                for col, date, image_path in zip(cols, dates[i:i+3], image_paths[i:i+3]):
                    with col:
                        st.markdown(f"**{date}**")  # Bold date display
                        st.image(image_path, width=80)

    except KeyError:
        st.error("⚠️ Invalid location. Please check your input and try again.")
