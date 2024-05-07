from aiogram import Bot, types
import random
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
#__________________________________________________________
from Config import Token
from jokes import jokes
#__________________________________________________________
bot = Bot(token=Token) # Создаем бота по токену
dp = Dispatcher(bot)  # Просто диспетчер бота
#__________________________________________________________

menu = [
    [InlineKeyboardButton(text="📝 Генерировать текст", callback_data="generate_text"),
    InlineKeyboardButton(text="🖼 Генерировать изображение", callback_data="generate_image")],
    [InlineKeyboardButton(text="💳 Купить токены", callback_data="buy_tokens"),
    InlineKeyboardButton(text="💰 Баланс", callback_data="balance")],
    [InlineKeyboardButton(text="💎 Jokes", callback_data="Jokes"),
    InlineKeyboardButton(text="🎁 Бесплатные токены", callback_data="free_tokens")],
    [InlineKeyboardButton(text="🔎 Помощь", callback_data="help")]
]
capsule_menu = InlineKeyboardMarkup(inline_keyboard=menu)
exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="◀️ Выйти в меню")]], resize_keyboard=True)
iexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️ Выйти в меню", callback_data="menu")]])

Greet_msg = "Привет, я бот"
Menu_msg = "Главное меню"

@dp.message_handler(commands="Menu")
async def proccess_Menu(message: types.Message):
    await message.answer(Greet_msg.format(name=message.from_user.full_name), reply_markup=capsule_menu)

#__________________________________________________________


button_command_settings = KeyboardButton("settings") # Создаем кнопку
button_command_info = KeyboardButton("info") # Создаем кнопку
capsule_start = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button_command_info,button_command_settings)
#__________________________________________________________
button_request = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton('Отправить свой контакт ☎️', request_contact=True)
).add(
    KeyboardButton('Отправить свою локацию 🗺️', request_location=True)
)
#__________________________________________________________
button_info = KeyboardButton("Information", callback_data="Info")
button_settings = KeyboardButton("Settings", callback_data="Set")
capsule_info = InlineKeyboardMarkup().add(button_info,button_settings)

'''button_command_joke = KeyboardButton("/Joke")
capsule_command = InlineKeyboardMarkup().add(button_command_joke)'''

button_source = KeyboardButton("Reference to source", url = "https://www.youtube.com/watch?v=5RlXStnMirE&ab_channel=BrettLenahan")
capsule_source = InlineKeyboardMarkup(row_width=2).add(button_source)
#__________________________________________________________
joke_button_one = KeyboardButton("JokeOne", callback_data="JokeOne")
joke_button_two = KeyboardButton("JokeTwo", callback_data="JokeTwo")

capsule_joke = InlineKeyboardMarkup().add(joke_button_one,joke_button_two)
#__________________________________________________________

#__________________________________________________________
@dp.message_handler(commands="Joke")
async def proccess_start(message: types.Message):
    await message.reply("Bы выбрали команду - Joke", reply_markup=capsule_joke)
@dp.message_handler(commands="Start")
async def proccess_start(message: types.Message):
    await message.reply("Bы выбрали команду - Start", reply_markup=capsule_info)
@dp.message_handler(commands=['Location'])
async def process_hi6_command(message: types.Message):
    await message.reply("Запрашиваем контакт и геолокацию\n", reply_markup=button_request)
@dp.message_handler(commands=['Source'])
async def process_command_2(message: types.Message):
    await message.reply("Отправляю ссылку на видео", reply_markup=capsule_source)
#__________________________________________________________
@dp.callback_query_handler(lambda c: c.data == "Info")
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Вам доступны команды\n/Joke\nSource\n/Location")
@dp.callback_query_handler(lambda c: c.data == "Set")
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Нажата кнопка - settings")
@dp.callback_query_handler(lambda c: c.data == "Source")
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Нажата кнопка - info")
@dp.callback_query_handler(lambda c: c.data == "JokeOne")
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "JokeOne")
@dp.callback_query_handler(lambda c: c.data == "JokeTwo")
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "JokeTwo")
# __________________________________________________________

@dp.callback_query_handler(lambda c: c.data == "Jokes")
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, jokes[random.randint(0,len(jokes))])




executor.start_polling(dp)
