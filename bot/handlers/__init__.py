from .start import router as start_router
from .admin import router as admin_router

from aiogram import Router

router = Router()
router.include_router(start_router)
router.include_router(admin_router)