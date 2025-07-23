from aiogram import Router,F
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


@router.message(Command("start"))
async def start_command(message: Message):
    await message.answer("Привет! я бот могу отвичать на сообщения привет и пока.")
    
@router.message(F.text.lower() == "привет")
async def cmd_1(message: Message):
    await message.answer("Привет!")

@router.message(F.text.lower() == "пока")
async def cmd_2(message: Message):   
    await message.answer("Досвидания")

@router.message()
async def cmd_elis(message: Message):
    await message.answer("Я не понимаю эту команду. Пожалуйста, напиши 'привет' или 'пока'.")