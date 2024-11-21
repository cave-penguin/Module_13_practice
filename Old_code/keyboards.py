from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_kb = ReplyKeyboardMarkup(keyboard=
[
    [
        KeyboardButton(text='cost'),
        KeyboardButton(text='about')
    ]
],
    resize_keyboard=True
)

catalog_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Medium game', callback_data='medium')],
        [InlineKeyboardButton(text='Big game', callback_data='big')],
        [InlineKeyboardButton(text='Mega game', callback_data='mega')],
        [InlineKeyboardButton(text='Other options', callback_data='other')]
    ]
)

buy_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Buy', url='http://google.com')],
        [InlineKeyboardButton(text='Back', callback_data='back_to_catalog')]
    ],

)

admin_panel = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Users', callback_data='users')],
    [InlineKeyboardButton(text='Statistics', callback_data='stat')],
    [
        InlineKeyboardButton(text='Blocking', callback_data='block'),
        InlineKeyboardButton(text='Unblocking', callback_data='unblock')
    ]
])
