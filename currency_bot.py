import json
import requests
import telebot
from telebot.types import KeyboardButton,ReplyKeyboardMarkup


BOT_TOKEN = '6066120391:AAHKyUbdd1bfpiR8snnt24ZmyQSf7taaMT0'
EXC_TOKEN = '9122b1356a5841e63d685645'

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start', 'help'])
def get_base_input(message):
    markup = ReplyKeyboardMarkup()
    markup.row_width = 2
    markup.add(KeyboardButton('USD'),
               KeyboardButton('RUB'), 
               KeyboardButton('BGN'),
               KeyboardButton('KGS'),
               KeyboardButton('EUR'),
               KeyboardButton('KZT'))
    bot.reply_to(message, 'Choose your base currency: ', reply_markup=markup)
    
    @bot.message_handler(func=lambda message: True)
    def get_target_input(message):
        base_input = message.text
        bot.reply_to(message, 'Choose your target currency: ')
        
        @bot.message_handler(func=lambda message: True)
        def get_amount_input(message):
            target_input = message.text
            bot.reply_to(message, 'Choose your amount: ')
                    
            @bot.message_handler(func=lambda message: True)
            def get_value(message):   
                amount_input = message.text      

                params = {'base_code': base_input,
                        'target_code': target_input,
                        'AMOUNT': amount_input}
                
                response = requests.get(f'https://v6.exchangerate-api.com/v6/{EXC_TOKEN}/pair/{base_input}/{target_input}/{amount_input}')
                data = json.loads(response.text)
                
                
                bot.send_message(message.chat.id, f"Conversion Rate: {data['conversion_rate']}\nConversion Result: {data['conversion_result']} {target_input}")
                
            bot.register_next_step_handler(message, get_value)
        bot.register_next_step_handler(message, get_amount_input)
    bot.register_next_step_handler(message, get_target_input)


bot.infinity_polling()

