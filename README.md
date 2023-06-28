# Currency-Bot-Telegram

This code provides a simple Telegram bot that allows users to convert currencies using the ExchangeRate-API. The bot prompts the user to select the base currency, target currency, and enter the amount to be converted.

Prerequisites

Before running the code, make sure you have the following:
Python 3.x installed on your system
The required Python packages installed (json, requests, telebot)

Setup

Obtain a Telegram bot token from the BotFather. If you don't know how to create a Telegram bot, refer to the Telegram Bot Documentation.
Sign up for an account on ExchangeRate-API and obtain an API token.
Replace the placeholders BOT_TOKEN and EXC_TOKEN in the code with your actual Telegram bot token and ExchangeRate-API token, respectively.

Usage

Run the code using a Python interpreter.
Start a conversation with your bot on Telegram.
Use the /start or /help command to initiate the currency conversion process.
The bot will present a list of base currencies as keyboard buttons. Choose your base currency by selecting one of the buttons.
The bot will then prompt you to choose the target currency.
Enter the amount you want to convert when prompted by the bot.
The bot will fetch the conversion rate and perform the currency conversion using the ExchangeRate-API.
Finally, the bot will display the conversion rate and the converted amount in the target currency.
Note: The code assumes that you have a stable internet connection and that the ExchangeRate-API is accessible.

Limitations

The code does not handle errors or exceptions, so it is advisable to add error handling for production use.
The code only supports a fixed set of base currencies. If you want to add or modify the available currencies, you need to update the ReplyKeyboardMarkup section accordingly.
The code performs a single conversion based on the provided base currency, target currency, and amount. If you want to add additional features, such as historical rates or multiple conversions, you need to extend the code accordingly.
Contributing

Contributions are welcome! If you find any issues or want to add new features to the code, feel free to open a pull request.

License
This code is licensed under the MIT License.
