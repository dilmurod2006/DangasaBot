import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html,types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart,Command
from aiogram.types import Message


from buttons import main_menu, tests_menu, translation_options, download_options, profile_actions

from tarjimon import uz_to_en, en_to_uz

TOKEN = getenv("TOKEN")

# print(TOKEN)


dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: types.Message) -> None:
    await message.answer("Asosiy menyu:", reply_markup=main_menu())

@dp.message(lambda message: message.text == "📊 Testlar")
async def handle_tests(message: types.Message):
    await message.answer("Testlar bo'limi:", reply_markup=tests_menu())

@dp.message(lambda message: message.text == "Tarjimon")
async def handle_translation(message: types.Message):
    await message.answer("Tarjima yo'nalishini tanlang:", reply_markup=translation_options())

@dp.message(lambda message: message.text == "Yuklab olish")
async def handle_download(message: types.Message):
    await message.answer("Yuklab olish formati:", reply_markup=download_options())

@dp.message(lambda message: message.text == "Profil")
async def handle_profile(message: types.Message):
    await message.answer("Profil ma'lumotlari:\nIsm: Foydalanuvchi\nBall: 100", 
                        reply_markup=profile_actions())

@dp.message(lambda message: message.text == "← Orqaga")
async def handle_back(message: types.Message):
    await message.answer("Asosiy menyu:", reply_markup=main_menu())

# Inline tugmalar uchun handlerlar
@dp.callback_query(lambda callback: callback.data.startswith("lang_"))
async def handle_lang_selection(callback: types.CallbackQuery):
    lang_pair = callback.data.split("_")[1:]
    await callback.message.answer(f"Siz tanladingiz: {' ➝ '.join(lang_pair).upper()}")
    await callback.answer()

@dp.callback_query(lambda callback: callback.data.startswith("download_"))
async def handle_download_format(callback: types.CallbackQuery):
    fmt = callback.data.split("_")[1]
    await callback.message.answer(f"{fmt.upper()} formatida yuklab olish boshlandi!")
    await callback.answer()



async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
