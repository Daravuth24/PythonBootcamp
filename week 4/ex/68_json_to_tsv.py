import json
import csv
import os


def json_to_tsv(jsonname,tsvname):

    if os.path.exists(jsonname):

        json_file = open(jsonname)
        json_data = json.load(json_file)

        json_file.close()

        tsv_file = open(tsvname, "w")
        tsv_writer = csv.DictWriter(tsv_file, sorted(json_data[0].keys()), delimiter='\t')

        tsv_writer.writeheader()
        tsv_writer.writerows(json_data)

        tsv_file.close()

        return 1

    else:
        return 0


json_to_tsv("samplejson.json", "sampletsv.tsv")
