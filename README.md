
# Weather Forecast App

## Overview

This application provides a simple and interactive way to check the weather forecast for the next few days. Users can choose a location, specify the number of forecast days, and view either the temperature trends or sky conditions in an intuitive interface.

The app uses the OpenWeatherMap API to fetch weather data and displays it using Streamlit and Plotly.

## Features

- Enter a location to get the weather forecast.
- Select the number of days (up to 5) for which you want to see the forecast.
- Choose between viewing temperature trends or sky conditions (e.g., clear, cloudy, rain).
- Interactive and visually appealing charts using Plotly.

## Prerequisites

Make sure you have Python installed. You will also need the following Python packages:

- `streamlit`
- `plotly`
- `requests`

You can install them using:

```bash
pip install streamlit plotly requests
```

## Setup

1. **Clone the Repository:**

    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Configure the API Key:**

   Replace `API_KEY` in `backend.py` with your OpenWeatherMap API key:

   ```python
   API_KEY = "your_api_key_here"
   ```

3. **Run the Application:**

    ```bash
    streamlit run app.py
    ```

4. **Access the App:**

   Open your browser and go to `http://localhost:8501`.


## Notes

- Make sure your OpenWeatherMap API key is active and has sufficient credits.
- The app can forecast up to 5 days of weather data, each day having 8 data points (3-hour intervals).

---
