import uvicorn
from fastapi import FastAPI, Query, Path, Body
from pydantic import BaseModel
from typing import Annotated, Optional

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

class User(BaseModel):
    username: str
    full_name: str | None = None

app = FastAPI()

@app.get('/')
def health_check():
    return {"success": True}

# localhost:8080/69
# @app.get("/{item_id}")
# def path_params(item_id: int):
#     print(type(item_id))
#     return {item_id: item_id}

# localhost:8080/q?
@app.get("/q/")
def query_params(skip: Annotated[int, Query(gt=0, lt=100)] , limit: Optional[int] = None):
    return {
        "skip": skip,
        "limit": limit
    }

@app.get("/items/{item_id}")
async def read_user_item(item_id: Annotated[int, Path(title="The ID of the item", ge=0, le=100)]):
    return {item_id}

@app.post("/items")
def create_item(item: Item):
    if item.name == "iphone":
        print(item.model_dump())

    return item



@app.post("/items/{item_id}")
async def update_item(
    *,
    item_id: int,
    item: Annotated[Item, Body()],
    user: Annotated[User, Body()],
    importance: Annotated[int, Query(ge=0)]
):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    return results

if __name__ == "__main__":
    uvicorn.run(app="main:app", port=8080, reload=True)
