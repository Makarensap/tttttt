from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN

bot = Bot(token= TELEGRAM_TOKEN)
dp = Dispatcher(bot)
async def set_commands(bot: Bot):
    commands = [
        types.BotCommand(command= '/start', description= 'Команда для тогоб чтобы запусить бота'),
        types.BotCommand(command='/help', description='Команда для тогоб чтобы узнать с чем может помочь наш бот'),
        types.BotCommand(command='/pufic', description='Узнать сколько лет я питался дошиком'),
        types.BotCommand(command='/dota2', description='зачем я играю в доту?'),
        types.BotCommand(command='/pechenka', description='хочешь испеку печенье????')
    ]
    await bot.set_my_commands(commands)

@dp.message_handler(commands="start")
async def start(message: types.Message):
    await message.answer('Привет, я твой бот, чем могу помочь тебе?')

@dp.message_handler(commands="help")
async def help(message: types.Message):
     await message.reply('я могу сказать несколько фактов о себе')

@dp.message_handler(commands="pufic")
async def help(message: types.Message):
    await message.reply('я ел дошик на протяжении 20 лет')

@dp.message_handler(commands="dota2")
async def help(message: types.Message):
    await message.reply('я люблю жостко саппортить на лионе')

@dp.message_handler(commands="pechenka")
async def help(message: types.Message):
     await message.reply('вот, держи печенье!')


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

async def on_startup(dispather):
    await set_commands(dispather.bot)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)