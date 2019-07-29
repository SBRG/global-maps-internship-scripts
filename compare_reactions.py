import json

# functions and variables with 0 at the end indicate that it refers to own map

# combines ids of subsystems for model
def combine_subsystem(ids1, subsystem2):
    with open('/Users/jerryhuang/Downloads/iLB1033_041318.json') as json_file:
        data = json.load(json_file)

    ids2 = []

    for item in data["reactions"]:
        if item["subsystem"] == subsystem2:
            ids2.append(item["id"])

    combined_ids = ids1 + ids2
    return combined_ids

# combines ids of subsystems for own map
def combine_subsystem0(ids1, ids2):
    return ids1 + ids2

# creates list of ids of subsystems in model
def create_subsystem(subsystem):
    with open('/Users/jerryhuang/Downloads/iLB1033_041318.json') as json_file:
        data = json.load(json_file)

    ids = []

    for item in data['reactions']:
        if item['subsystem'] == subsystem:
            ids.append(item['id'])

    return ids

# creates list of ids of subsystem in own map
def create_subsystem0(file_name):
    with open('/Users/jerryhuang/Downloads/' + file_name) as count_set:
        data0 = json.load(count_set)

    ids = []

    for item in data0[1]['reactions'].items():
        ids.append(item[1]['bigg_id'])

    return ids

#forms venn diagram lists
def compare_reactions():
    #ids_in_subsystem = create_subsystem('')
    ids_in_subsystem = combine_subsystem(combine_subsystem(create_subsystem("Phosphoglycerolipid metabolism"), "Galactoglycerolipid metabolism"), "Cardiolipin biosynthesis")
    ids_in_subsystem0 = combine_subsystem0(create_subsystem0('glycerolipid-metabolism.json'), create_subsystem0('Glycerophospholipid_Metabolism.json'))

    diff_ids0 = []
    for item in ids_in_subsystem0:
        if not item in ids_in_subsystem:
            diff_ids0.append(item)

    diff_ids = []
    for item in ids_in_subsystem:
        if not item in ids_in_subsystem0:
            diff_ids.append(item)

    # print("data: " + str(ids_in_subsystem))
    # print("data0: " + str(ids_in_subsystem0))
    # print(len(ids_in_subsystem0))

    return diff_ids0, diff_ids


print(compare_reactions())
