# Company     : PT. Arsytech Information Technology
# Owner       : Adi Surizal
# Email       : adisurizal.cyber@outlook.com

import os
from flask.json.provider import DefaultJSONProvider
from collections import OrderedDict

class Config:
    EXCHANGE_API_KEY = os.getenv("EXCHANGE_API_KEY")
    BASE_CURRENCY = os.getenv("BASE_CURRENCY", "USD")

class CustomJSONProvider(DefaultJSONProvider):
    def dumps(self, obj, **kwargs):
        kwargs.setdefault("sort_keys", False)
        return super().dumps(obj, **kwargs)

    def loads(self, s, **kwargs):
        return super().loads(s, object_pairs_hook=OrderedDict)
