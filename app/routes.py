from fastapi import APIRouter
from .models import Data

router = APIRouter()

@router.post("/data")
def push_data(d: Data):
    return {"received": d.value}
