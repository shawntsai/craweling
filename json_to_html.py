import json
item = json.load(open("first.json"))
with open("first.html", 'wb') as f:
    f.write(item['raw_content'].encode('utf-8'))
