from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters import CommandStart
from aiogram.enums import ParseMode
from asgiref.sync import sync_to_async
from keyboards import start_menu
from core.models import Category, SubCategory, Video, Master

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    full_name = message.from_user.full_name
    await message.answer(
        f"Assalomu alaykum, {full_name}!\n\nSunSir botiga xush kelibsiz ☺️\n\nQuyidagi bo‘limlardan birini tanlang:",
        reply_markup=start_menu
    )


@router.callback_query(F.data == "videos")  
async def video_categories(callback: CallbackQuery):
    categories = await sync_to_async(list)(Category.objects.all())
    if not categories:
        await callback.message.answer("Hali kategoriyalar mavjud emas.")
        return

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=cat.name, callback_data=f"category_{cat.id}")]
        for cat in categories
    ] + [[InlineKeyboardButton(text="⬅️ Orqaga", callback_data="back_to_main")]])

    await callback.message.answer("📂 Kategoriyalardan birini tanlang:", reply_markup=keyboard)

@router.callback_query(F.data.startswith("category_"))
async def show_subcategories(callback: CallbackQuery):
    category_id = int(callback.data.split("_")[1])
    subcategories = await sync_to_async(list)(
        SubCategory.objects.filter(category__id=category_id)
    )
    if not subcategories:
        await callback.message.answer("Bu kategoriyada subkategoriya mavjud emas.")
        return

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=sub.name, callback_data=f"subcategory_{sub.id}")]
        for sub in subcategories
    ] + [[InlineKeyboardButton(text="⬅️ Orqaga", callback_data="videos")]])

    await callback.message.answer("📁 Videolar kategoriyasidan birini tanlang:", reply_markup=keyboard)

@router.callback_query(F.data.startswith("subcategory_"))
async def send_videos(callback: CallbackQuery):
    subcat_id = int(callback.data.split("_")[1])
    subcategory = await sync_to_async(SubCategory.objects.select_related("category").get)(id=subcat_id)

    videos = await sync_to_async(list)(
        Video.objects.filter(subcategory_id=subcat_id)
    )

    if not videos:
        await callback.message.answer("Bu subkategoriyada videolar mavjud emas.")
        return

    await callback.message.answer(f"🎥 “{subcategory.name}” subkategoriyasidagi videolar:")

    for video in videos:
        await callback.message.answer(
            f"🖼 <b>{video.title}</b>\n🔗 {video.youtube_link}",
            parse_mode=ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup(
                inline_keyboard=[
                    [InlineKeyboardButton(text="⬅️ Orqaga", callback_data=f"category_{subcategory.category.id}")]
                ]
            )
        )


@router.callback_query(F.data == "ustalar")
async def send_ustalar(callback: CallbackQuery):
    ustalar = await sync_to_async(list)(Master.objects.all())
    if not ustalar:
        await callback.message.answer("Ustalar ro'yxati mavjud emas.")
        return

    text = "\n\n".join(
        [f"👨‍🔧 Usta: {usta.name}\n📞 Tel: {usta.phone}" for usta in ustalar]
    )

    await callback.message.answer(
        text,
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="⬅️ Orqaga", callback_data="back_to_main")]
            ]
        )
    )

@router.callback_query(F.data == "back_to_main")
async def back_to_main(callback: CallbackQuery):
    await callback.message.answer("Quyidagi bo‘limlardan birini tanlang:", reply_markup=start_menu)