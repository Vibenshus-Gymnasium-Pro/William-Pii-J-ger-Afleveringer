import json


def analyze_json_structure(json_obj, structure, parent_key=None, visited=None):
    if visited is None:
        visited = set()

    if isinstance(json_obj, dict):
        for key in json_obj:

            ## Temp fix for edges containing similar metadata
            if (parent_key == "graph"):
                visited.clear()

            if key in visited:
                return
            else:
                visited.add(key)

            ## Return if object has same obj keys as previous object
            if (isinstance(json_obj[key], dict)):
                for x in json_obj[key]:
                    if (x in visited):
                        return
            
            ## Structure with path
            # new_key = "{}.{}".format(parent_key, key) if parent_key else key
            ## Structure without path
            new_key = key


            if new_key not in structure:
                structure[new_key] = {}
            else:
                print("Error traversing json object at: " + str(key))

            analyze_json_structure(json_obj[key], structure[new_key], new_key, visited)
    elif isinstance(json_obj, list):
        if json_obj:
            analyze_json_structure(json_obj[0], structure, parent_key, visited)





## Temp error for multiple clean_up_dict words. Solution is to check against whitelist
def clean_up_json_structure(json_obj):
    ## Add/remove/edit words
    # clean_up_dict = {"nodes": "id", "edges": "test"}
    clean_up_dict = {"nodes": "id"}


    for key in json_obj:
        if key in clean_up_dict:
            tempnode = {}
            tempnode[clean_up_dict[key]] = json_obj[key]
            if (clean_up_dict[key] in json_obj[key]):
                tempnode = json_obj[key]
            else:
                # print(*json_obj[key])
                tempnode[clean_up_dict[key]] = json_obj[key].pop(*json_obj[key])
            json_obj[key] = tempnode

        clean_up_json_structure(json_obj[key])





with open("les_miserables.json") as f:
    json_data = json.load(f)
    

structure = {}
analyze_json_structure(json_data, structure)

clean_up_json_structure(structure)
print(structure)


