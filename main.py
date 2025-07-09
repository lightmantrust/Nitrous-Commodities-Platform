from fastapi import FastAPI
from app.routers import auth, users, commodities, inventory, orders, compliance

app = FastAPI()

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(commodities.router)
app.include_router(inventory.router)
app.include_router(orders.router)
app.include_router(compliance.router)

@app.get("/")
def root():
    return {"status": "Nitrous API running"}
