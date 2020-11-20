import asyncio

import motor.motor_asyncio as aiomotor
from aiohttp import web
from bson import ObjectId


class SiteHandler:
    def __init__(self, mongo):
        self.mongo = mongo

    async def post(self, request):
        product = await request.json()
        await self.mongo.insert_one(product)
        return web.json_response("OK")

    async def get_all(self, request):
        all_products = self.mongo.find({})
        names_and_id = []
        for product in await all_products.to_list(length=None):
            names_and_id.append((product["name"], str(product["_id"])))
        return web.json_response(names_and_id)

    async def get_by_id(self, request):
        _id = request.match_info["id"]
        document = await self.mongo.find_one({"_id": ObjectId(_id)})
        document["_id"] = _id
        return web.json_response(document)

    async def get_by_filter(self, request):
        dict_query = request.query.copy()
        dict_for_search = {}
        try:
            dict_for_search["name"] = dict_query.pop("name")
        except KeyError:
            pass
        try:
            dict_for_search["desc"] = dict_query.pop("desc")
        except KeyError:
            pass
        if dict_query:
            dict_for_search["parameters"] = {}
            for k in dict_query:
                dict_for_search["parameters"][k] = dict_query[k]
        documents = self.mongo.find(dict_for_search)
        names = []
        for document in await documents.to_list(length=None):
            names.append(document["name"])
        return web.json_response(names)


async def init():
    app = web.Application()
    client = aiomotor.AsyncIOMotorClient("mongodb://localhost:27017")
    db = client["product_service"]
    mongo = db["product"]
    handler = SiteHandler(mongo)
    app.add_routes(
        [
            web.get("/product/{id}", handler.get_by_id),
            web.get("/product/", handler.get_by_filter),
            web.post("/product", handler.post),
            web.get("/product", handler.get_all),
        ]
    )
    return app


def main():
    loop = asyncio.get_event_loop()
    app = loop.run_until_complete(init())
    web.run_app(app)


if __name__ == "__main__":
    main()
