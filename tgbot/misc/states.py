from aiogram.dispatcher.filters.state import StatesGroup, State


class UserState(StatesGroup):
    get_country = State()
    get_name = State()
    get_number = State()
    get_prod = State()
    get_sum = State()
    get_social = State()
    get_operator = State()
    get_del_date = State()
    get_loc = State()
    get_loc_conf = State()


class UserCityState(StatesGroup):
    get_sum_type = State()


class UserVillageState(StatesGroup):
    get_del = State()
    get_area = State()


class UserWorldState(StatesGroup):
    get_del = State()


class AdminState(StatesGroup):
    get_param = State()


class AdminAddState(StatesGroup):
    get_name = State()


class AdminDelState(StatesGroup):
    get_id = State()

