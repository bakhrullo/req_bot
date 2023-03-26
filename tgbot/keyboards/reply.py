from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

direction_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(
    KeyboardButton("Toshkent shahar bo'ylab"),
    KeyboardButton("Viloyatlarga"),
    KeyboardButton("Dunyo bo'ylab"))

delivery_village_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(
    KeyboardButton("Yubor express"),
    KeyboardButton("BTS express"))

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

operator_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(
    KeyboardButton("Alpha"),
    KeyboardButton("Betta"),
    KeyboardButton("Gamma"),
    KeyboardButton("Delta"))

pay_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(
    KeyboardButton("To'langan ✅"),
    KeyboardButton("To'lanmagan ❌"))

contact_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton("Kontaktni yuborish 📱", request_contact=True))

loc_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton("Manzilni yuborish 📍", request_location=True))

loc_conf_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(
    KeyboardButton(text='📍 Qayta yuborish', request_location=True),
    KeyboardButton(text='✅ Manzilni tasdiqlash'))

remove_kb = ReplyKeyboardRemove()
