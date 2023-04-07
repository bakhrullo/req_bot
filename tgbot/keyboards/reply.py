from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

from tgbot.models.db_cmd import get_opers

direction_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(
    KeyboardButton("Toshkent shahar bo'ylab"),
    KeyboardButton("Viloyatlarga"),
    KeyboardButton("Dunyo bo'ylab"))

delivery_village_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(
    KeyboardButton("Yubor express"),
    KeyboardButton("BTS express"))

delivery_city_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(
    KeyboardButton("Yandex"),
    KeyboardButton("Kuryer"))

wrapper_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(
    KeyboardButton("Kraft paket"),
    KeyboardButton("Gulli paket"),
    KeyboardButton("Karobka"),
    KeyboardButton("O'ramsiz holat")
)

yubor_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(
    KeyboardButton("Markaz"),
    KeyboardButton("Chekka hudud"))

bts_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(
    KeyboardButton("Viloyatdagi ofisgacha"))

delivery_world_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(
    KeyboardButton("Ems express"),
    KeyboardButton("BTS express"))

social_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(
    KeyboardButton("Telegram"),
    KeyboardButton("Instagram"),
    KeyboardButton("Qo'ng'iroq"))


async def operators_kb():
    opers = await get_opers()
    operator_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    for oper in opers:
        operator_kb.insert(KeyboardButton(oper.name))
    return operator_kb

pay_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(
    KeyboardButton("To'langan ✅"),
    KeyboardButton("To'lanmagan ❌"))

contact_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton("Kontaktni yuborish 📱", request_contact=True))

loc_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton("Manzilni yuborish 📍", request_location=True))

loc_conf_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(
    KeyboardButton(text='✅ Manzilni tasdiqlash'))

comm_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(
    KeyboardButton(text='Tashalb ketish'))

remove_kb = ReplyKeyboardRemove()
