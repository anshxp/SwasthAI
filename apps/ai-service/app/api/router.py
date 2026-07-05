from fastapi import APIRouter

from app.api.chatbot import router as chatbot_router
from app.api.clean import router as clean_router
from app.api.predict import router as predict_router
from app.api.inventory import router as inventory_router
from app.api.report import router as report_router

router = APIRouter()

router.include_router(chatbot_router, prefix="/chat", tags=["Chat"])
router.include_router(clean_router, prefix="/clean", tags=["Data Cleaning"])
router.include_router(predict_router, prefix="/predict", tags=["Prediction"])
router.include_router(inventory_router, prefix="/inventory", tags=["Inventory"])
router.include_router(report_router, prefix="/report", tags=["Reports"])