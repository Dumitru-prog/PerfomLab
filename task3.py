import json

with open("tests.json", "r") as test:
    a = json.load(test)

with open("values.json", "r") as value:
    b = json.load(value)


id2m = {x['id']: x['value'] for x in b['values']}

def report(q):
    to_r = []
    for x in q:
            ll = {**x, 'value': id2m[x['id']] if x['id'] in id2m else "??"}
            if 'values' in ll:
                    ll['values'] = report(ll['values'])
            to_r += [ll]
    return to_r

def write(data, filename):
    data = json.dumps(data)
    data = json.loads(str(data))
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent = 2)

write(report(a['tests']), 'report.json')
