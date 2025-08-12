from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from asgiref.sync import sync_to_async
from core.models import BotUser
from config.settings import ADMIN_ID

router = Router()

@router.message(Command("broadcast"))
async def start_broadcast(message: types.Message, state: FSMContext):
    if message.from_user.id != ADMIN_ID:
        return await message.answer("⛔ Sizga ruxsat yo‘q.")
    
    await state.set_data({"broadcast": True})
    await message.answer("✍️ Yuboriladigan xabar matnini yoki mediasini yuboring:")


@router.message(F.content_type.in_({"text", "photo", "video", "document", "audio"}))
async def send_broadcast(message: types.Message, state: FSMContext):
    data = await state.get_data()

    if not data.get("broadcast") or message.from_user.id != ADMIN_ID:
        return 

    await state.clear()

    user_ids = await sync_to_async(list)(
        BotUser.objects.values_list("chat_id", flat=True)
    )

    count = 0
    for uid in user_ids:
        try:
            if message.content_type == "text":
                await message.bot.send_message(uid, message.text)
            elif message.content_type == "photo":
                await message.bot.send_photo(uid, message.photo[-1].file_id, caption=message.caption or "")
            elif message.content_type == "video":
                await message.bot.send_video(uid, message.video.file_id, caption=message.caption or "")
            elif message.content_type == "document":
                await message.bot.send_document(uid, message.document.file_id, caption=message.caption or "")
            elif message.content_type == "audio":
                await message.bot.send_audio(uid, message.audio.file_id, caption=message.caption or "")
            count += 1
        except Exception:
            continue

    await message.answer(f"✅ {count} ta foydalanuvchiga xabar yuborildi.")
