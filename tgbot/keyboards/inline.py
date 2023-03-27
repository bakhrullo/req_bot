from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from tgbot.models.db_cmd import get_opers

admin_kb = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton("Operator qo'shish", callback_data="add"),
    InlineKeyboardButton("Operator o'chirish", callback_data="delete"))

back_btn = InlineKeyboardButton("Orqaga 🔙", callback_data="back")
back_kb = InlineKeyboardMarkup().add(back_btn)


async def operators_kb():
    opers = await get_opers()
    operator_kb = InlineKeyboardMarkup(row_width=1)
    for oper in opers:
        operator_kb.insert(InlineKeyboardButton(oper.name, callback_data=oper.id))
    operator_kb.insert(back_btn)
    return operator_kb
