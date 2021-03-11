import zlib, json, base64
 
ZIPJSON_KEY = 'data'

def json_zip(j):

    j = {
        ZIPJSON_KEY: base64.b64encode(
            zlib.compress(
                json.dumps(j).encode('utf-8')
            )
        ).decode('ascii')
    }

    return j
    

original = {'a': "A", 'b': "B"}
print(json_zip(original))
