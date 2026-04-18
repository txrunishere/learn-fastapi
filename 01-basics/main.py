import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

app = FastAPI()

@app.get('/')
def health_check():
    return {"success": True}

# localhost:8080/69
@app.get("/{item_id}")
def path_params(item_id: int):
    print(type(item_id))
    return {item_id: item_id}

# localhost:8080/q?
@app.get("/q/")
def query_params(skip: int , limit: int | None = None):
    return {
        "skip": skip,
        "limit": limit
    }

@app.get("/items/{item_id}")
async def read_user_item(item_id: str, needy: str | None = None):
    item = {"item_id": item_id, "needy": needy}
    return item

@app.post("/items")
def create_item(item: Item):
    if item.name == "iphone":
        print(item.model_dump())

    return item


if __name__ == "__main__":
    uvicorn.run(app="main:app", port=8080, reload=True)
