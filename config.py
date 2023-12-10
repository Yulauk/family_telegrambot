import os


"""in this file you need to set the API keys"""

'''If you are using Docker!'''
# In your self-contained Docker environment, perform the following steps:
# 1. Replace "your_actual_bot_token" with your actual Telegram bot token.
# 2. Change "your_image_name" to your Docker image name.

# After making the changes, run the following command to start the Docker container:
# docker run -e TELEGRAM_BOT_TOKEN=your_actual_bot_token your_image_name


'''If you are running your script outside of Docker'''
# set api-key and token in your shell before executing the script


DEFAULT_VALUE = ''

# your telegram_BOT API-Key
dandy_cat_bot = os.environ.get('TELEGRAM_BOT_TOKEN', 'DEFAULT_VALUE')


# your telegram_BOT API-Key
# dandy_cat_bot = 'TELEGRAM_BOT-TOKEN'
