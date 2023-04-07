from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import Message

from geopy.adapters import AioHTTPAdapter
from geopy.geocoders import Nominatim

from tgbot.filters.locfilter import LocFilter
from tgbot.keyboards.reply import *
from tgbot.misc.states import UserState, UserCityState, UserVillageState, UserWorldState
from tgbot.models.db_cmd import get_counter
from tgbot.services.google_sheets import worksheet


async def user_start(message: Message):
    await message.answer("Yo'nalishlardan birini tanlang 👇", reply_markup=direction_kb)
    await UserState.get_country.set()


async def get_country(m: Message, state: FSMContext):
    await state.update_data(country=m.text)
    await m.answer("Iltimos mijoz ismini kiriting 👤", reply_markup=remove_kb)
    await UserState.next()


async def get_name(m: Message, state: FSMContext):
    await state.update_data(name=m.text)
    await m.answer("Iltimos mijoz telefon raqamini yuboring 📲")
    await UserState.next()


async def get_contact(m: Message, state: FSMContext):
    await state.update_data(phone=m.text)
    await m.answer("Iltimos olgan mahsulotlaringizni yuboring 🛒", reply_markup=remove_kb)
    await UserState.next()


async def get_prod(m: Message, state: FSMContext):
    await state.update_data(prod=m.text)
    await m.answer("Iltimos to'lov qiymatini yuboring 💵")
    await UserState.next()


async def get_sum(m: Message, state: FSMContext):
    await state.update_data(sum=m.text)
    data = await state.get_data()
    if data["country"] == "Toshkent shahar bo'ylab":
        await UserCityState.get_sum_type.set()
        return await m.answer("To'lov holati 💸", reply_markup=pay_kb)
    elif data["country"] == "Viloyatlarga":
        await UserVillageState.get_del.set()
        return await m.answer("Yetkazib berish pochtasi 📬", reply_markup=delivery_village_kb)
    elif data["country"] == "Dunyo bo'ylab":
        await UserWorldState.get_del.set()
        return await m.answer("Yetkazib berish pochtasi 📬", reply_markup=delivery_world_kb)
    await m.answer("Iltimos to'lov qiymatini yuboring 💵")


async def get_del_world(m: Message, state: FSMContext):
    await state.update_data(pochta=m.text)
    await m.answer("Qaysi tarmoqdan murojaat qilindi 🌐", reply_markup=social_kb)
    await UserState.get_social.set()


async def get_del_vill(m: Message, state: FSMContext):
    await state.update_data(pochta=m.text)
    if m.text == "Yubor express":
        await m.answer("Hududni tanlang", reply_markup=yubor_kb)
    elif m.text == "BTS express":
        await m.answer("Hududni tanlang", reply_markup=bts_kb)
    await UserVillageState.next()


async def get_area(m: Message, state: FSMContext):
    await state.update_data(area=m.text)
    await m.answer("Qaysi tarmoqdan murojaat qilindi 🌐", reply_markup=social_kb)
    await UserState.get_social.set()


async def get_sum_type(m: Message, state: FSMContext):
    await state.update_data(sum_type=m.text)
    await m.answer("Qaysi tarmoqdan murojaat qilindi 🌐", reply_markup=social_kb)
    await UserState.get_social.set()


async def get_social(m: Message, state: FSMContext):
    await state.update_data(social=m.text)
    await m.answer("Qaysi mutaxassis qabul qildi 👨‍💻", reply_markup=await operators_kb())
    await UserState.next()


async def get_operator(m: Message, state: FSMContext):
    await state.update_data(operator=m.text)
    await m.answer("Yetkazib berish muddatini yuboring 📅", reply_markup=remove_kb)
    await UserState.next()


async def get_del_date(m: Message, state: FSMContext):
    await state.update_data(date=m.text)
    await m.answer("Iltimos manzilni yuboring yoki lokatsiya tashlang")
    await UserState.next()


async def get_loc(m: Message, state: FSMContext):
    if m.content_type == "location":
        async with Nominatim(user_agent="inn_bot", adapter_factory=AioHTTPAdapter) as geolocator:
            location = await geolocator.reverse(f"{m.location.latitude}, {m.location.longitude}")
        await state.update_data(address=location.address, long=m.location.longitude, lat=m.location.latitude, loc_type="T")
        return await m.answer(f"{location.address}\nTasdiqlaysizmi?", reply_markup=loc_conf_kb)
    await state.update_data(loc_type="F", address=m.text)
    return await m.answer(f"{m.text}\nTasdiqlaysizmi?", reply_markup=loc_conf_kb)


async def get_loc_conf(m: Message, state: FSMContext, config):
    res = await state.get_state()
    await m.answer("Izoh qoldiring 💬", reply_markup=comm_kb)
    await UserState.next()


async def get_comm(m: Message, state: FSMContext, config):
    data = await state.get_data()
    count = await get_counter()
    comm = " "
    group, text = "", f"👤 Ism: {data['name']}\n" \
                      f"📱 Raqam: {data['phone']}\n" \
                      f"🛣 Yo'nalish: {data['country']}\n" \
                      f"📦 Mahsulot: {data['prod']}\n" \
                      f"💲 To'lov qiymati: {data['sum']}\n"

    if data["country"] == "Toshkent shahar bo'ylab":
        text += f"💲 To'lov holati: {data['sum_type']}\n"
        group, sum_type = config.tg_bot.city, data["sum_type"]
        pochta, area = " ", " "
    elif data["country"] == "Viloyatlarga":
        text += f"📪 Pochta: {data['pochta']}\n" \
                f"🏙 Hudud: {data['area']}\n"
        group, sum_type = config.tg_bot.village, " "
        pochta, area = data['pochta'], data['area']
    elif data["country"] == "Dunyo bo'ylab":
        text += f"📪 Pochta: {data['pochta']}\n"
        group, sum_type = config.tg_bot.world, " "
        pochta , area = data['pochta'], ' '
    text += f"🌐 Tarmoq: {data['social']}\n" \
            f"👨‍💻 Mutaxassis: {data['operator']}\n" \
            f"📅 Yetkazib berish muddati: {data['date']}\n" \
            f"📍 Manzil:\n{data['address']}\n"
    if m.text != "Tashalb ketish":
        comm = m.text
        text += f"💬 Izoh: {comm}"
    mess = await m.bot.send_message(chat_id=group, text=text)
    await worksheet(no=count, name=data['name'], phone=data['phone'], country=data['country'], prod=data['prod'],
                    sum=data['sum'], sum_type=sum_type, pochta=pochta, area=area, social=data['social'],
                    operator=data['operator'], date=data['date'], address=data['address'], comm=comm)
    if data["loc_type"] == "T":
        await m.bot.send_location(chat_id=group, latitude=data["lat"], longitude=data["long"],
                                  reply_to_message_id=mess.message_id)
    await m.answer(f"✅ Ma'lumotlar saqlab qolindi\n"
                   f"{text}", reply_markup=remove_kb)
    await m.answer("Yo'nalishlardan birini tanlang 👇", reply_markup=direction_kb)
    await UserState.get_country.set()


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")
    dp.register_message_handler(get_country, state=UserState.get_country)
    dp.register_message_handler(get_name, state=UserState.get_name)
    dp.register_message_handler(get_contact, state=UserState.get_number)
    dp.register_message_handler(get_prod, state=UserState.get_prod)
    dp.register_message_handler(get_sum, state=UserState.get_sum)
    dp.register_message_handler(get_sum, state=UserState.get_sum)
    dp.register_message_handler(get_del_world, state=UserWorldState.get_del)
    dp.register_message_handler(get_del_vill, state=UserVillageState.get_del)
    dp.register_message_handler(get_area, state=UserVillageState.get_area)
    dp.register_message_handler(get_sum_type, state=UserCityState.get_sum_type)
    dp.register_message_handler(get_social, state=UserState.get_social)
    dp.register_message_handler(get_operator, state=UserState.get_operator)
    dp.register_message_handler(get_del_date, state=UserState.get_del_date)
    dp.register_message_handler(get_loc, LocFilter(), content_types=["location", "text"], state=UserState.get_loc)
    dp.register_message_handler(get_loc_conf, Text(equals="✅ Manzilni tasdiqlash"), state=UserState.get_loc)
    dp.register_message_handler(get_comm, state=UserState.get_comment)

