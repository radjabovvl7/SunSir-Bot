from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🎥 Videolar", callback_data="videos")],
        [InlineKeyboardButton(text="🧑‍🔧 Ustalar", callback_data="ustalar")],
        [InlineKeyboardButton(text="📷 Instagram", url="https://www.instagram.com/sunsir.uzbekistan/")]
    ]
)
