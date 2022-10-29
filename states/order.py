from aiogram.dispatcher.filters.state import StatesGroup, State


class Orders(StatesGroup):
    order1 = State()
    order2 = State()
    order3 = State()


class DataTimeHand(StatesGroup):
    datatime1 = State()


class Blanks(StatesGroup):
    blank1 = State()


class DelAddDress(StatesGroup):
    DelAdd1 = State()
    DelAdd2 = State()


class LastName(StatesGroup):
    lastname1 = State()
