from typing import List

from datetime import datetime

from tgbot.models.models import Operator, Counter


async def get_opers() -> List[Operator]:
    return await Operator.query.gino.all()


async def create_opers(name) -> Operator:
    return await Operator.create(name=name)


async def delete_opers(id):
    return await Operator.delete.where(Operator.id == id).gino.status()


async def create_counter():
    if await Counter.query.where(Counter.name == "counter").gino.first() is None:
        await Counter.create(name="counter")


async def get_counter():
    res = await Counter.query.where(Counter.name == "counter").gino.first()
    if res.day == int(datetime.now().strftime("%d")):
        await res.update(count=res.count + 1).apply()
        return res.count
    await res.update(count=1, day=int(datetime.now().strftime("%d"))).apply()
    return 1
