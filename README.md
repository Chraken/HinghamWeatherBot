Hingham Weather Bot 🌦️

  A serverless Python bot that automatically fetches the current weather for Hingham, MA, and posts an update to X. This project is designed to run as an AWS Lambda function on a daily schedule.

Features
  1)Weather Data: from [WeatherAPI](https://www.weatherapi.com/).
  2)X Integraion: Uses the [Tweepy](https://www.tweepy.org/) library to interact with the X API v2.
  3)Hosted on AWS Lambda for zero-maintenance execution scheduled to run 10 AM EST daily.
  4)Uses Environment Variables to keep API credentials private.

Architecture
  Language: Python 3.12
  Trigger: AWS EventBridge on a cron schedule.
  Layers: Includes custom Lambda Layers for `tweepy` and `requests`. (Note: Requests Layer pulled from:'https://github.com/keithrozario/Klayers')

Setup & Security
To run this bot yourself, you must configure the following Environment Variables in your AWS Lambda function settings:

| Variable | Description |
| :--- | :--- |
| `WEATHER_API_KEY` | Your API key from WeatherAPI.com |
| `X_CONSUMER_KEY` | X Developer Portal Consumer Key |
| `X_CONSUMER_SECRET` | X Developer Portal Consumer Secret |
| `X_ACCESS_TOKEN` | X Developer Portal Access Token |
| `X_ACCESS_SECRET` | X Developer Portal Access Token Secret |

How It Works
  1. The function is triggered by an EventBridge schedule.
  2. It calls the WeatherAPI to get the current temperature and conditions for Hingham.
  3. It formats a string with the weather details and a timestamp.
  4. It authenticates with the X API using the stored environment variables.
  5. It posts the tweet and logs the success/failure to Amazon CloudWatch.

License
  This project is open-source and available under the MIT License.
