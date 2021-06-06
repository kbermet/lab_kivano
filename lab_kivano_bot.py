import telebot
import os

from lab_kivano_parser import Products, find_deps, Writer


import pandas as pd

class Spy:
    help_text = ''' 
/categories выдать названия всех категорий.
/categories{название категории} выдать товары этой категории. (название и ссылку)
/product {название продукта} выдать информацию о данном товаре. (название, название категории, ссылка)
    '''

    __products = pd.read_csv('kivano_test.csv')
    fractionset = set(__products.frac)

    def products_from_fractions(self, frac):
        if len(frac) <= 0:
            return '\n'.join(self.fractionset)
        else:
            if frac == 'товар':
                frac = (f'Товар {frac}')
        if(frac) not in self.fractionset:
            return f'Товара с названием {frac} нет'
        else:
            dep = self.__products[self.__products.frac ==frac]
            dep = dep[['dep_fio', 'dep_link']].to_string()
            return dep


TOKEN = os.environ.get('TELEGRAM_TOKEN', 'some token')
bot = telebot.TeleBot(TOKEN)
kbot = Spy()

@bot.message_handler(commands=['start', 'help'])
def start_and_help(message):
    bot.send_message(message.chat.id, kbot.help_text)

@bot.message_handler(commands=['categories'])
def start_and_help(message):
    bot.send_message(message.chat.id, kbot.help_text)

@bot.message_handler(commands=['products'])
def start_and_help(message):
    bot.send_message(message.chat.id, kbot.help_text)


if __name__=='__main__':
    bot.polling()


