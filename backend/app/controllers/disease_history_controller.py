from fastapi import APIRouter
import base64
from pydantic import BaseModel
from typing import List
from fastapi.responses import JSONResponse

from app.services import DiseaseHistoryService


router = APIRouter()

class SaveRequest(BaseModel):
    UserID: int
    Image: str
    ClassIdxList: List[int]

disease_history_service = DiseaseHistoryService()

@router.post("/save")
async def save_history(request: SaveRequest):
    try:
        image_data = request.Image
        image_byte = base64.b64decode((image_data))
        result = await disease_history_service.save_history(request.UserID, image_byte, request.ClassIdxList)
        message = {
            "Message": result,
            "Reload_Status": True
        }
        return JSONResponse(
            content=message,
            headers = {"Content-Type": "application/json; charset=utf-8"}
        )
    except Exception as e:
        message = {
            "Message": "Error to save history",
            "Reload_Status": False
        }
        return JSONResponse(
            content=message,
            headers={"Content-Type": "application/json; charset=utf-8"}
        )

@router.get("/{user_id}")
async def get_by_id(user_id: int):
    try:
        result = await disease_history_service.get_predict_history_by_id(user_id)
        return JSONResponse(
            content=result,
            headers={"Content-Type": "application/json; charset=utf-8"}
        )
    except Exception as e:
        print(e)
        message = {
            "Message": "Error to get history",
        }
        return JSONResponse(
            content=message,
            headers={"Content-Type": "application/json; charset=utf-8"}
        )