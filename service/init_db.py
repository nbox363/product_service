import asyncio

import motor.motor_asyncio as aiomotor
from bson import ObjectId


async def init_data():
    client = aiomotor.AsyncIOMotorClient("mongodb://localhost:27017")
    db = client["product_service"]
    collection_product = db["product"]
    p = {
        "_id": ObjectId(),
        "name": "iphone",
        "desc": "The iPhone is a smartphone made by Apple that combines a computer",
        "parameters": {"size": "10", "brand": "apple"},
    }
    await collection_product.insert_one(p)


async def do_delete_all_documents():
    client = aiomotor.AsyncIOMotorClient("mongodb://localhost:27017")
    db = client["product_service"]
    collection_product = db["product"]
    await collection_product.delete_many({})


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(init_data())


if __name__ == "__main__":
    main()
