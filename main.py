import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, html,types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from users.buttons import main_menu
from config.settings import TOKEN

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handlerstart(message: types.Message) -> None:
    await message.answer("Asosiy menyu:", reply_markup=main_menu())

async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
