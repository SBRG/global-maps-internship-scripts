import json

# This is useless. Keep it in case for the future.
def search_and_replace(string, filename):
    f = open('/Users/jerryhuang/Downloads/' + filename, 'r')
    file = f.read()
    f2 = open('/Users/jerryhuang/Downloads/' + filename, 'w')
    string2 = '111' + string
    file = file.replace(string, string2)
    f2.write(file)
    with open('/Users/jerryhuang/Downloads/' + filename) as json_file:
        data = json.load(json_file)
    print(string2)
    return data

# Searches and replaces all instances of a particular string by adding 111 before it.
def search_and_replace2(string, filename):
    f = open('/Users/jerryhuang/Downloads/' + filename, 'r')
    file = f.read()
    f2 = open('/Users/jerryhuang/Downloads/' + filename, 'w')
    file = file.replace(string, '"111' + string[1:-1] + '"')
    f2.write(file)
    with open('/Users/jerryhuang/Downloads/' + filename) as json_file:
        data = json.load(json_file)
    return data


    #print(file)
def check(string):
    if string[-2] != '_':
        return string + '_m'
    else:
        string = string[:-1] + 'm'
        return string

def read_json(file_name):
    with open('/Users/jerryhuang/Downloads/' + file_name) as json_file:
        data = json.load(json_file)

        #Adding 111 to reaction/metabolite ids
        for item in data[1]['reactions']:
          new_data = search_and_replace2('"' + item + '"')
        for item in data[1]['nodes']:
           new_data = search_and_replace2('"' + item + '"')
        #Adding 111 to segment ids
        for item in data[1]['reactions'].items():
            for item2 in item[1]['segments']:
               new_data = search_and_replace2('"' + item2 + '"')
        #Adding 111 to text labels
        for item in data[1]['text_labels']:
            new_data = search_and_replace2('"' + item + '"')
        #Shifting coordinates by 6000
        for item in new_data[1]['reactions'].items():
            item[1]['label_x'] += 6000
            for item2 in item[1]['segments'].items():
                if item2[1]['b1'] is not None:
                    item2[1]['b1']['x'] += 6000
                if item2[1]['b2'] is not None:
                    item2[1]['b2']['x'] += 6000
        for item in new_data[1]['nodes'].items():
            item[1]['x'] += 6000
            if 'label_x' in item[1]:
                item[1]['label_x'] += 6000
        for item in new_data[1]['text_labels'].items():
            item[1]['x'] += 6000
        new_data[1]['canvas']['width'] += 6000
    return new_data

# Makes the json file into clean, readable format
def clean_up(data, output_file):
    with open('/Users/jerryhuang/Downloads/' + output_file, 'w') as outfile:
        json.dump(data, outfile, indent = 4)

clean_up(read_json())

