import motor.motor_asyncio as aiomotor


async def init_mongo():
    client = aiomotor.AsyncIOMotorClient("mongodb://localhost:27017")
    db = client["product_service"]
    collection_product = db["product"]
    return collection_product
