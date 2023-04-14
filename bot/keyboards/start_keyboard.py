from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from bot.callbacks import *

def start_kb():
    k = InlineKeyboardMarkup()
    k.add(InlineKeyboardButton('Add issue',callback_data=add_issue_call.new()))
    return k

def show_projects(projects):
    k = InlineKeyboardMarkup()
    for project in projects:
        k.add(InlineKeyboardButton(project.name,callback_data=choose_project_call.new(project.id)))
    return k

def show_types_issue():
    k = InlineKeyboardMarkup()
    k.add(InlineKeyboardButton(text='Development',callback_data=choose_type_issue.new('Development')))
    k.add(InlineKeyboardButton(text='Farm', callback_data=choose_type_issue.new('Farm')))
    k.add(InlineKeyboardButton(text='Design', callback_data=choose_type_issue.new('Design')))
    return k

