from fastapi import FastAPI
from models.data_table import DataTable
import uvicorn

app = FastAPI()

@app.get("/find")
async def find(find_string):
    find_res = data_table.find(find_string)
    return find_res

data_table = DataTable()
uvicorn.run(app, host = "0.0.0.0")