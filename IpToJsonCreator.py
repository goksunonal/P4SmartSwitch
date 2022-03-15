# importing the module
import re
import socket
import json

ipList = []

def extract_ip_address_from_txt_file():
    with open('ipAddressesList.txt') as fh:
        fstring = fh.readlines()
    for line in fstring:
        ip=line.strip()
        ipList.append(ip)
    print("Removing duplicates...")
    converted_set = list(set(ipList))
    print("Size after removed duplicates:", len(converted_set))
    fh.close()
    return converted_set

def main():
    set = extract_ip_address_from_txt_file()[:1000]
    jsonReader =  open('s1-runtime.json')
    currentJsonData = json.load(jsonReader)
    currentDict = currentJsonData['table_entries']
    added_entries = []
    try:
        print(len(set))
        for element in set:
            jsonString = {
                "table": "MyIngress.ipv4_lpm",
                "match": {
                    "hdr.ipv4.dstAddr": [element, 32]
                },
                "action_name": "MyIngress.drop",
                "action_params": {}
            }
            if jsonString in added_entries:
                print("No need to add")
            else:
                added_entries.append(jsonString)
                currentDict.append(jsonString)
                print("Entry Number Added #", len(added_entries))
        currentJsonData['table_entries'] = currentDict
        jsonFileWriter = open("s1-runtime.json", "w")
        json.dump(currentJsonData, jsonFileWriter, default = vars, indent=2)
    except:
        print("Error while writing")
main()
