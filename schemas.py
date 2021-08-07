from pydantic import BaseModel
from typing import Optional

class HousePrice(BaseModel):
    POSTED_BY: str
    UNDER_CONSTRUCTION: int
    RERA: int
    BHK_NO : int
    BHK_OR_RK: str
    SQUARE_FT: float
    READY_TO_MOVE: int
    RESALE: int
    ADDRESS: str
    LONGITUDE: float
    LATITUDE: float


    class Config:
        schema_extra = {
            "example": {
                "POSTED_BY": "Dealer",
                "UNDER_CONSTRUCTION": 0,
                "RERA": 1,
                "BHK_NO": 3,
                "BHK_OR_RK": "BHK",
                "SQUARE_FT": 1275.00,
                "READY_TO_MOVE": 1,
                "RESALE": 1,
                "ADDRESS": "New Town,Kolkata",
                "LONGITUDE": 22.592200,
                "LATITUDE": 88.484911}}


class HousePriceResponse(BaseModel):
    Outcome: float
    POSTED_BY: str
    UNDER_CONSTRUCTION: int
    RERA: int
    BHK_NO: int
    BHK_OR_RK: str
    SQUARE_FT: float
    READY_TO_MOVE: int
    RESALE: int
    ADDRESS: str
    LONGITUDE: float
    LATITUDE: float
