from fastapi import FastAPI
from app.routes.issues import router as issues_router
from fastapi.middleware.cors import CORSMiddleware
#from app.routes.issues import router as issues_router
from app.middleware.timer import timing_middleware

app=FastAPI(
    title="Issue Tracker API",
    version="0.1.0",
    description="A mini production-style API built with FastAPI",
)

app.middleware("http")(timing_middleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/v1/health")
def health_check():
    return {"status":"ok"}


app.include_router(issues_router)



# items= [
#     {"id":1, "name":"Item One"},
#     {"id":2, "name":"Item Two"},
#     {"id":2, "name":"Item Three"}
# ]

# @app.get("/health")
# def health_check():
#     return {"status":"ok"}

# @app.get("/items")
# def get_items():
#     return items

# @app.get("/items/{item_id}")
# def get_item(item_id: int):
#     for item in items:
#         if item["id"]==item_id:
#             print("yayyy")
#     return {"error":"Item not found"}

# @app.post("/item")
# def create_item(item: dict):
#     items.append(item)
#     return item

#This above commented code was just for intro and basic understanding 




