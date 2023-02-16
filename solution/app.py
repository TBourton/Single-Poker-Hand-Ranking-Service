from fastapi import APIRouter, FastAPI, HTTPException
from fastapi.responses import PlainTextResponse
from hand import Hand
from pydantic import BaseModel, ValidationError

app = FastAPI()
api_router = APIRouter()


class HandBody(BaseModel):
    hand: str


@api_router.post("/rank", response_class=PlainTextResponse)
def rank(body: HandBody) -> str:
    hand_str = body.hand
    try:
        return Hand.from_string(hand_str).rank()
    except (ValueError, ValidationError) as exp:
        raise HTTPException(500, str(exp)) from exp


app.include_router(api_router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")
