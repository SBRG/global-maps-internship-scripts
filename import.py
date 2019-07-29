import json

def import_map(file1, file2, file_combined):
    with open('/Users/jerryhuang/Downloads/' + file1) as json_file:
        data1 = json.load(json_file)
    with open('/Users/jerryhuang/Downloads/' + file2) as json_file:
        data2 = json.load(json_file)

    # combine reactions
    combined_data1 = combine_json(data1[1]['reactions'], data2[1]['reactions'])
    #print(json.dumps(combined_data1, indent=4))

    # combine nodes
    combined_data2 = combine_json(data1[1]['nodes'], data2[1]['nodes'])

    # combine text labels
    combined_data3 = combine_json(data1[1]['text_labels'], data2[1]['text_labels'])

    # combine everything
    #total_data = combine_json(combine_json(combined_data1, combined_data2), combined_data3)

    data2[1]['reactions'] = combined_data1
    data2[1]['nodes'] = combined_data2
    data2[1]['text_labels'] = combined_data3

    print(json.dumps(data2, indent=4))

    # Creates combined json file
    with open('/Users/jerryhuang/Downloads/' + file_combined, 'w') as outfile:
        json.dump(data2, outfile, indent=4)

# Puts everything in the first json file
def combine_json(t1, t2):
    for i in t2.keys():
        if i in t1:
            t1[i].update(json.loads(json.dumps(t2[i])))
        else:
            t1[i] = json.loads(json.dumps(t2[i]))
    return t1

import_map()
