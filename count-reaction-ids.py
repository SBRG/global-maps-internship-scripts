import json

def count_reactions():
    with open('/Users/jerryhuang/Downloads/List_of_reactions.json') as count_set:
        data0 = json.load(count_set)
    with open(
            '/Users/jerryhuang/Downloads/central-metabolism.json') as json_file:
        data = json.load(json_file)

    count = 0

    for item in data[1]['reactions'].items():
        data0.append(item[1]['bigg_id'])
        count += 1

    data0 = list(dict.fromkeys(data0))
    length = len(data0)
    print(count)

    with open('/Users/jerryhuang/Downloads/List_of_reactions.json',
              'w') as outfile:
        json.dump(data0, outfile)

    return length

print(count_reactions())
