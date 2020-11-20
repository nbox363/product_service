import trafaret as t
from trafaret.base import Dict, String
from trafaret.contrib.object_id import MongoId


product = t.Dict(
    {
        t.Key("_id"): MongoId(),
        t.Key("name"): t.String(max_length=50),
        t.Key("desc"): t.String(),
        t.Key("parameters"): t.List(String),
    }
)
