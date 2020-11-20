import asyncio
import json
import motor.motor_asyncio as aiomotor
from aiohttp import web
from bson import ObjectId
from utils import init_mongo


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


class SiteHandler:
    def __init__(self, mongo):
        self.mongo = mongo

    async def post(self, request):
        product = await request.json()
        await self.mongo.insert_one(product)
        return web.json_response("OK")

    async def get_by_filter(self, request):
        dict_query = request.query
        d = dict_query.copy()

        dict_for_search = {}

        try:
            dict_for_search["name"] = d.pop("name")
        except KeyError:
            pass
        try:
            dict_for_search["desc"] = d.pop("desc")
        except KeyError:
            pass

        if d:
            dict_for_search["parameters"] = {}
            for k in d:
                dict_for_search["parameters"][k] = d[k]

        # dict_for_search = {
        #     'name': name,
        #     'desc': desc,
        #     'parameters': d
        # }

        print(dict_for_search)
        documents = self.mongo.find(dict_for_search)
        names = []
        for document in await documents.to_list(length=None):
            names.append(document["name"])

        return web.json_response(names)

    async def get_by_id(self, request):
        _id = request.match_info["id"]
        document = await self.mongo.find_one({"_id": ObjectId(_id)})
        document["_id"] = _id
        return web.json_response(document)

    async def get_all(self, request):
        result = self.mongo.find({})
        data = await result.to_list(length=None)
        d = JSONEncoder().encode(data)
        return web.json_response(d)


async def init():
    app = web.Application()
    client = aiomotor.AsyncIOMotorClient("mongodb://localhost:27017")
    db = client["product_service"]
    mongo = db["product"]
    handler = SiteHandler(mongo)
    app.add_routes(
        [
            web.get("/products/{id}", handler.get_by_id),
            web.get("/products/", handler.get_by_filter),
            web.post("/products", handler.post),
            web.get("/products", handler.get_all),
        ]
    )
    return app


def main():
    loop = asyncio.get_event_loop()
    app = loop.run_until_complete(init())
    web.run_app(app)


if __name__ == "__main__":
    main()
