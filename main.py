# main.py

from fastapi import FastAPI, HTTPException
from crud import create_item, get_item, update_item, delete_item, get_all_items

app = FastAPI()

@app.post("/items/")
def create_item_route(item_data: dict):
    return create_item(item_data)


@app.get("/items/")
def read_all_items():
    items = get_all_items()
    return items

@app.get("/items/{item_id}")
def read_item(item_id: int):
    item = get_item(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.put("/items/{item_id}")
def update_item_route(item_id: int, item_data: dict):
    item = update_item(item_id, item_data)
    return item

@app.delete("/items/{item_id}")
def delete_item_route(item_id: int):
    return delete_item(item_id)
