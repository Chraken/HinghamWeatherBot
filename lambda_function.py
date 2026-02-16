import requests
import tweepy
import os
def lambda_handler(event, context):
    # WeatherAPI Key
    weather_api_key = os.environ.get('WEATHER_API_KEY')

    # X API Keys
    consumer_key = os.environ.get('X_CONSUMER_KEY')
    consumer_secret = os.environ.get('X_CONSUMER_SECRET')
    access_token = os.environ.get('X_ACCESS_TOKEN')
    access_token_secret = os.environ.get('X_ACCESS_SECRET')

    #Weather URl- Could be consolidated into single variable
    baseurl = 'http://api.weatherapi.com/v1'
    current_weather_endpoint = '/current.json' 
    location = "Hingham"

    try:
        response = requests.get(f'{baseurl}{current_weather_endpoint}?key={weather_api_key}&q={location}')
        response.raise_for_status() # Check for errors (like 404 or 401)
        data = response.json()
        
        current = data['current']
        temp_f = current['temp_f']
        condition = current['condition']['text']
        time=current['last_updated']
        
        # Create the x post body
        post_body = f"The current weather in {location} is {temp_f}°f and {condition} as of {time}. #HinghamWeather"
        
        print(f"Prepared Tweet: {post_body}")

        client = tweepy.Client(
            consumer_key=consumer_key, consumer_secret=consumer_secret,
            access_token=access_token, access_token_secret=access_token_secret
        )

        # Post on X
        response = client.create_tweet(text=post_body)
        print(f"Success! Tweet posted. ID: {response.data['id']}")

    except Exception as e:
        print(f"An error occurred: {e}")
