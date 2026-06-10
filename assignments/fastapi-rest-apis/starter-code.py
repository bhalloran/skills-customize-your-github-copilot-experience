from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Optional

app = FastAPI()


class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None


_db: Dict[int, Item] = {}


@app.get("/items")
def list_items():
    return list(_db.values())


@app.get("/items/{item_id}")
def get_item(item_id: int):
    item = _db.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@app.post("/items", status_code=201)
def create_item(item: Item):
    if item.id in _db:
        raise HTTPException(status_code=400, detail="Item with this ID already exists")
    _db[item.id] = item
    return item


@app.put("/items/{item_id}")
def update_item(item_id: int, updated: Item):
    if item_id != updated.id:
        raise HTTPException(status_code=400, detail="ID in path and body must match")
    if item_id not in _db:
        raise HTTPException(status_code=404, detail="Item not found")
    _db[item_id] = updated
    return updated


@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    if item_id not in _db:
        raise HTTPException(status_code=404, detail="Item not found")
    del _db[item_id]
    return
