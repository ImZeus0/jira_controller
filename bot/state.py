from aiogram.dispatcher.filters.state import StatesGroup, State


class AddIssue(StatesGroup):
    summary = State()
    count = State()