import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Загружаем токен из файла .env
API_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Создаем главное меню с кнопками
keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📸 Узнать цены")],
        [KeyboardButton(text="📅 Свободные даты")],
        [KeyboardButton(text="📍 Локации в Тбилиси")],
        [KeyboardButton(text="📞 Связаться с фотографом")]
    ],
    resize_keyboard=True
)

@dp.message(CommandStart())
async def send_welcome(message: types.Message):
    await message.reply(
        "Привет! 👋 Я помощник фотографа Виталия Быстрова в Тбилиси.\n\n"
        "Я люблю настоящие эмоции и живые истории. Вам не обязательно уметь позировать — я всё подскажу!\n\n"
        "Чем могу помочь? Выберите вариант ниже:",
        reply_markup=keyboard
    )

@dp.message()
async def handle_messages(message: types.Message):
    text = message.text.lower()
    
    if "цен" in text or "прайс" in text or "стоим" in text:
        await message.reply(
            "💰 **Наши пакеты:**\n\n"
            "• **BASIC** — 180 ₾ (до 1 часа, 15 фото, 5 в ретуши)\n"
            "• **BUSINESS** — 300 ₾ (до 2 часов, 35 фото в ретуши)\n"
            "• **PREMIUM** — 500 ₾ (до 4 часов, 70 фото в ретуши)\n\n"
            "✨ Во все пакеты входит: помощь с образом, позированием и подбор локации!"
        )
    elif "дат" in text or "запис" in text or "брон" in text:
        await message.reply(
            "📅 Отличный выбор! Чтобы проверить свободные даты, напишите, пожалуйста:\n"
            "1. Желаемый месяц\n"
            "2. Ваш номер телефона\n\n"
            "Виталий свяжется с вами для подтверждения в течение часа!"
        )
    elif "локац" in text or "мест" in text:
        await message.reply(
            "🏛 Мы снимаем в самых атмосферных местах Тбилиси:\n"
            "• Улочки Старого города\n"
            "• Зеленый парк Ваке\n"
            "• Уютные профессиональные студии в центре\n\n"
            "Я помогу подобрать идеальное место под вашу историю!"
        )
    elif "связ" in text or "телефон" in text or "позвон" in text:
        await message.reply(
            "📱 Пожалуйста, напишите ваш номер телефона в этом чате, и Виталий лично свяжется с вами для обсуждения деталей!"
        )
    else:
        await message.reply(
            "Я пока учусь понимать все вопросы 😊 Пожалуйста, выберите вариант из меню ниже или просто оставьте свой номер телефона, и Виталий свяжется с вами!"
        )

async def main():
    print("Бот запущен и готов к работе! 🚀")
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())