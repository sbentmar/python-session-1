# to import a library, use import:
import json

json_string = '{"a": 1, "b": 2}'

json_document = json.loads(json_string)
print(json.dumps(json_document, indent=4))

# or use from, together with import

from json import dumps, loads

json_document = loads(json_string)
print(dumps(json_document, indent=4))

import mylibrary
mylibrary.gooby()