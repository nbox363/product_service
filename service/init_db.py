import asyncio

from utils import init_mongo


async def init_data():
    collection_product = await init_mongo()
    p = {
        "_id": 1,
        "name": "iPhone",
        "desc": "The iPhone is a smartphone made by Apple that combines a computer",
        "parameters": {"brand": "apple", "manufacturer": "USA"},
    }
    await collection_product.insert_one(p)


async def do_delete_all_documents():
    collection_product = await init_mongo()
    await collection_product.delete_many({})


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(init_data())


if __name__ == "__main__":
    main()
