import json
import csv
import os

def tsv_to_json(tsvname, jsonname):

    if os.path.exists(tsvname):
        data = {}
        with open(tsvname) as tsvfile:
            tsvread = csv.DictReader(tsvfile, delimiter = "\t")
            for tsvrow in tsvread:
                data["completed"] = tsvrow

        root = {}

        root["completed"] = data

        with open(jsonname, "w") as jsonfile:
            jsonfile.write(json.dumps(data, indent=4))

        return 1
    else:
        return 0




tsv_to_json("sampletsv2.tsv", "samplejson2.json")
