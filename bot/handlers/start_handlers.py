from bot.loader import bot, dp
from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from aiogram.types.callback_query import CallbackQuery

from bot.state import AddIssue
from services import jira_api
from bot.keyboards.start_keyboard import *
@dp.message_handler(commands=['start'], state='*')
async def mainstart(m: Message, state: FSMContext):
    await state.finish()
    await m.answer('Hello',reply_markup=start_kb())

@dp.callback_query_handler(add_issue_call.filter())
async def add_issue(call:CallbackQuery):
    await call.message.edit_text('Choose project')
    projects = jira_api.get_projects()
    await call.message.edit_reply_markup(show_projects(projects))

@dp.callback_query_handler(choose_project_call.filter())
async def add_type_issue(call:CallbackQuery,callback_data:dict,state:FSMContext):
    id_project = callback_data.get('id')
    await state.update_data(id_project=id_project)
    await call.message.edit_text('Choose type issue',reply_markup=show_types_issue())

@dp.callback_query_handler(choose_type_issue.filter())
async def save_type_issue(call:CallbackQuery,callback_data:dict,state:FSMContext):
    type_issue = callback_data.get('type')
    await state.update_data(type_issue=type_issue)
    await call.message.edit_text('Input summary issue')
    await AddIssue.summary.set()

@dp.message_handler(state=AddIssue.summary)
async def add_count(m:Message,state:FSMContext):
    summary = m.text
    await state.update_data(summary=summary)
    await m.answer('Input count issue')
    await AddIssue.count.set()

@dp.message_handler(state=AddIssue.count)
async def create_issue(m:Message,state:FSMContext):
    count = m.text
    try:
        count = int(count)
        data = await state.get_data()
        msg = ''
        for n in  range(count):
            isuue = jira_api.create_issue(int(data['id_project']),data['summary'],data['type_issue'])
            msg += isuue.key+ 'add \n'
        await m.answer(msg,reply_markup=start_kb())
    except:
        await m.answer('Enter a number')