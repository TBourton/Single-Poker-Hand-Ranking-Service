from fastapi import APIRouter, Body, FastAPI

app = FastAPI()
api_router = APIRouter()


@api_router.get("/health", status_code=200)
def health() -> dict:
    return {"msg": "Healthy"}


@api_router.post("/rank")
def rank(hand: str = Body()) -> str:
    return "foo"


app.include_router(api_router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")
