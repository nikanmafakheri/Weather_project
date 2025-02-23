# Weather App

A simple Django-based weather app that provides weather information using the OpenWeatherMap API. This app allows users to search for weather details by city name.

## Features

- **Weather Information**: Displays the current weather and temperature of any city.
- **API Integration**: Fetches data from the OpenWeatherMap API.
- **User-Friendly UI**: Easy-to-use interface to search and view weather details.

## Technologies Used

- **Backend**: Django
- **API**: OpenWeatherMap
- **Frontend**: HTML, CSS

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/weather-app.git
   ```

2. Navigate to the project directory:
   ```bash
   cd weather-app
   ```

3. Set up a virtual environment (optional but recommended):
   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Set up your OpenWeatherMap API key:
   - Sign up at [OpenWeatherMap](https://openweathermap.org/api) and get an API key.
   - Add the key to your environment variables or configuration settings (based on how you've set it up).

6. Run migrations to set up the database:
   ```bash
   python manage.py migrate
   ```

7. Run the development server:
   ```bash
   python manage.py runserver
   ```

8. Visit `http://127.0.0.1:8000` in your browser to use the app.

## Usage

- Enter the name of a city in the search bar and click "Get Forecast"
- The app will display the current weather information for that city, including temperature, humidity, wind speed, and weather conditions.
