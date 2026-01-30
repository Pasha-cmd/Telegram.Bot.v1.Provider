import asyncio  
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types.input_file import FSInputFile
import time
import random


bot = Bot(tokenbot)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message):
    button1 = InlineKeyboardButton(
        text = "Test1",
        callback_data="test1"
    )
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[[button1]]
    )
    await message.answer(
        text="Привет! драсте ё",
        reply_markup=keyboard
    )

@dp.message()
async def text_handler(message):
    # приводим текст к нижнему регистру
    text = message.text.lower()

    if text == "hello":
        # отправка картинки с компьютера
        await message.answer(
            "привет я сигма"
        )
    elif text == "bye":
        await message.answer("ну ок пока")
        time.sleep(2)
        await message.answer_voice(
            voice="https://github.com/Pasha-cmd/filesfortgtest1/raw/refs/heads/main/Undertale%20last%20breath%20phase%203.mp3"
        )
        time.sleep(1)
        await message.answer("или нет..")
        time.sleep(16.5)
        for i in range(6):
            await message.answer("я.не.буду.умирать...")
        await message.answer("круто.")
        def chosenext():
            chosed = random.randint(0, len(wordsrandom) - 1)
            x = wordsrandom[chosed]
            return x
        wordsrandom = ["нет.", "no", "oh noes", ".", "...", "dsa"]
        for i in range(51):
            x = chosenext()
            await message.answer(x)
            time.sleep(0.1)
        time.sleep(300)
        for u in range(6):
            await message.answer("я все еще тут..")
        time.sleep(300)
        for i in range(6):
            await message.answer("...")
        for q in range(6):
            time.sleep(300)
            for u in range(11):
                await message.answer("....")

# ===== Обработка нажатия кнопки =====
@dp.callback_query()
async def callback_handler(callback):
    if callback.data == "test1":
        await callback.message.answer(
            "Ну кароче вот тест 123123132"
        )

        # обязательно отвечаем на callback (чтобы не было «часиков»)
        await callback.answer()


# ===== Запуск бота =====
async def main():
    # запускаем polling (бот постоянно слушает сообщения)
    await dp.start_polling(bot)


# ===== Точка входа =====
if __name__ == "__main__":
    asyncio.run(main())
