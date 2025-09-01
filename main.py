import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import F

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# 🔑 حط التوكن تاعك هنا (من BotFather)
BOT_TOKEN = "حط_التوكن_تاعك_هنا"

# ---------- لوحة الأزرار ----------
def main_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📚 الدروس", callback_data="lessons")],
        [InlineKeyboardButton(text="📝 التمارين", callback_data="exercises")],
        [InlineKeyboardButton(text="📖 القوانين المهمة", callback_data="rules")],
        [InlineKeyboardButton(text="🎥 الفيديوهات", callback_data="videos")],
    ])

# ---------- إعدادات البوت ----------
bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(storage=MemoryStorage())

# ---------- الأوامر ----------

# /start
@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        "👋 مرحبا بك في *بوت الباك*!\n"
        "اختـر من القائـمة 👇",
        reply_markup=main_menu(),
        parse_mode="Markdown"
    )

# 📚 الدروس
@dp.callback_query(F.data == "lessons")
async def cb_lessons(cq: CallbackQuery):
    await cq.message.edit_text(
        "📚 المواد الدراسية:\n\n"
        "1️⃣ رياضيات\n"
        "2️⃣ فيزياء\n"
        "3️⃣ علوم طبيعية\n"
        "4️⃣ عربية\n\n"
        "🔜 سنضيف محتوى لكل مادة."
    )

# 📝 التمارين
@dp.callback_query(F.data == "exercises")
async def cb_exercises(cq: CallbackQuery):
    await cq.message.edit_text(
        "📝 هنا ستجد تمارين مع الحلول.\n"
        "🔜 سنضيف ملفات PDF وتمارين محلولة."
    )

# 📖 القوانين
@dp.callback_query(F.data == "rules")
async def cb_rules(cq: CallbackQuery):
    await cq.message.edit_text(
        "📖 القوانين الأساسية:\n"
        "- Δ = b² - 4ac\n"
        "- V = l × w × h\n"
        "- F = m × a\n\n"
        "🔜 سنضيف قوانين كاملة في PDF."
    )

# 🎥 الفيديوهات
@dp.callback_query(F.data == "videos")
async def cb_videos(cq: CallbackQuery):
    await cq.message.edit_text(
        "🎥 دروس فيديو:\n"
        "- [رياضيات - YouTube](https://www.youtube.com/)\n"
        "- [فيزياء - YouTube](https://www.youtube.com/)\n"
        "- [علوم - YouTube](https://www.youtube.com/)\n",
        disable_web_page_preview=True,
        parse_mode="Markdown"
    )

# ---------- تشغيل البوت ----------
async def main():
    print("🚀 البوت راهو يخدم...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
