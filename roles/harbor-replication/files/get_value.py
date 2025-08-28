import sys
import json

def get_value(json_text, key, where):
    try:
        json_object = json.loads(json_text) # .decode('utf-8'))
        if not isinstance(json_object, list):
            json_object = [ json_object ]
        (json_path, regex1) = where.split('=')
        for i in json_object:
            if json_path in i and str(i.get(json_path)) == regex1:
                return (0, i.get(key))
        return(10, "NOT_FOUND")
    except Exception as e:
        print("error:", e)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python jsonpathx.py 'json_text' 'jsonpath' 'jsonpath=regex'")
        sys.exit(1)
    json_text = (sys.argv[1])
    key = (sys.argv[2])
    where = (sys.argv[3])
    # print(json_text)
    # print(key)
    # print(where)
    code, value = get_value(json_text, key, where)
    print(value)
    sys.exit(code)
