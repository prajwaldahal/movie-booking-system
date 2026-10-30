from fastapi import FastAPI

app = FastAPI(title="Movie Booking System")

@app.get("/")
def read_root():
    return {"status": "ok"}