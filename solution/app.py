from fastapi import APIRouter, FastAPI, HTTPException
from fastapi.responses import PlainTextResponse
from hand import Hand
from pydantic import ValidationError

app = FastAPI()
api_router = APIRouter()


@api_router.get("/health", status_code=200)
def health() -> dict:
    return {"msg": "Healthy"}


@api_router.post("/rank", response_class=PlainTextResponse)
def rank(hand: str) -> str:
    try:
        return Hand.from_string(hand).rank()
    except (ValueError, ValidationError) as exp:
        raise HTTPException(500, str(exp)) from exp


app.include_router(api_router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")
