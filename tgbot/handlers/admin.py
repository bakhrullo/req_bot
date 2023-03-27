from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery

from tgbot.filters.back import BackFilter
from tgbot.keyboards.inline import admin_kb, operators_kb, back_kb
from tgbot.misc.states import AdminState, AdminAddState, AdminDelState
from tgbot.models.db_cmd import create_opers, delete_opers


async def admin_start(message: Message):
    await message.answer("Salom, admin! 👋", reply_markup=admin_kb)
    await AdminState.get_param.set()


async def get_param(c: CallbackQuery):
    if c.data == "add":
        await AdminAddState.get_name.set()
        return await c.message.edit_text("Operator nomini yuboring", reply_markup=back_kb)
    await c.message.edit_text("O'chirish kerak bo'lgan operatorni tanlang 👇", reply_markup=await operators_kb())
    await AdminDelState.get_id.set()


async def get_name(m: Message):
    await create_opers(m.text)
    await m.answer("Operator qo'shildi ✅", reply_markup=admin_kb)
    await AdminState.get_param.set()


async def get_id(c: CallbackQuery):
    await delete_opers(int(c.data))
    await c.message.edit_text("Operator o'chirlidi ✅", reply_markup=admin_kb)
    await AdminState.get_param.set()


async def back(c: CallbackQuery):
    await c.message.delete()
    await c.message.answer("Salom, admin! 👋", reply_markup=admin_kb)
    await AdminState.get_param.set()


def register_admin(dp: Dispatcher):
    dp.register_message_handler(admin_start, commands=["start"], state="*", is_admin=True)
    dp.register_callback_query_handler(get_param, state=AdminState.get_param, is_admin=True)
    dp.register_message_handler(get_name, state=AdminAddState.get_name, is_admin=True)
    dp.register_callback_query_handler(get_id, BackFilter(),state=AdminDelState.get_id, is_admin=True)
    dp.register_callback_query_handler(back, state="*", is_admin=True)
