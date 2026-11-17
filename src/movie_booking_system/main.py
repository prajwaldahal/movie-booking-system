from fastapi import FastAPI

app = FastAPI(title="Movie Booking System")


@app.get("/health")
def read_root():
    return {"status": "ok"}

