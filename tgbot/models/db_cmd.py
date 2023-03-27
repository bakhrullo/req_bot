from typing import List

from tgbot.models.models import Operator


async def get_opers() -> List[Operator]:
    return await Operator.query.gino.all()


async def create_opers(name) -> Operator:
    return await Operator.create(name=name)


async def delete_opers(id):
    return await Operator.delete.where(Operator.id == id).gino.status()
