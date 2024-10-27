import logging
import os
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup
from writer import writer_func

# Set up logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot('7882446823:AAG0A_7LepL2DQKXoCFRuK2IefnBZpOeRjM')
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Set up reply keyboard
language = ReplyKeyboardMarkup(resize_keyboard=True)
language.add('Russian', 'English')

class UserState(StatesGroup):
    language = State()
    fullname = State()
    company = State()
    phone = State()
    email = State()
    site = State()
    address = State()
    job = State()

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await UserState.language.set()
    await message.answer('Выберите язык: ', reply_markup=language)


@dp.errors_handler()
async def my_error_handler(update, exception):
    logging.exception("An error occurred: %s", exception)
    return True


@dp.message_handler(state=UserState.language)
async def choose_language(message: types.Message, state: FSMContext):
    if message.text not in ['Russian', 'English']:
        await message.answer('Пожалуйста, выберите язык!')
        return

    async with state.proxy() as data:
        data['language'] = message.text

    await UserState.next()
    welcome_msg = "Добро пожаловать в нашего бота! Введите свое полное имя: " if data['language'] == 'Russian' else "Welcome to our bot! Enter your fullname "
    await message.answer(welcome_msg)

@dp.message_handler(state=UserState.fullname)
async def get_fullname(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['fullname'] = message.text

    await UserState.next()
    await message.answer('Введите название вашей компании: ' if data['language'] == 'Russian' else 'Enter your company name: ')


@dp.message_handler(state=UserState.company)
async def get_company(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['company'] = message.text

    await UserState.next()
    await message.answer(
        'Введите ваш номер телефона: ' if data['language'] == 'Russian' else 'Enter your phone number: ')


@dp.message_handler(state=UserState.phone)
async def get_phone(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone'] = message.text

    await UserState.next()
    await message.answer(
        'Введите вашу электронная почта: ' if data['language'] == 'Russian' else 'Enter your email: ')


@dp.message_handler(state=UserState.email)
async def get_email(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['email'] = message.text

    await UserState.next()
    await message.answer('Введите вашу сайт: ' if data['language'] == 'Russian' else 'Enter your site: ')


@dp.message_handler(state=UserState.site)
async def get_site(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['site'] = message.text

    await UserState.next()
    await message.answer(
        'Введите вашу адрес: ' if data['language'] == 'Russian' else 'Enter your address: ')


@dp.message_handler(state=UserState.address)
async def get_address(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['address'] = message.text

    await UserState.next()
    await message.answer('Введите вашу работу: ' if data['language'] == 'Russian' else 'Enter your job: ')


@dp.message_handler(state=UserState.job)
async def get_job(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['job'] = message.text

        # Call the writer function to generate images
        await writer_func(data['fullname'], data['job'], data['phone'], data['email'], data['site'], data['address'], data['company'])

        # Sending the first image
        with open(f'media/{data["fullname"]}1.png', 'rb') as img_file1:
            await message.answer_photo(img_file1)

        # Sending the second image
        with open(f'media/{data["fullname"]}2.png', 'rb') as img_file2:
            await message.answer_photo(img_file2)

        thank_you_msg = 'Спасибо за информацию!' if data['language'] == 'Russian' else 'Thank you for your information!'
        await message.answer(thank_you_msg)

        os.remove(f"media/{data['fullname']}1.png")
        os.remove(f"media/{data['fullname']}2.png")

    await state.finish()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

