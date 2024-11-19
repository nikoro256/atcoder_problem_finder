from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/search")
async def search(search_string):
    return {"problem" : search_string}

uvicorn.run(app, host = "0.0.0.0")