import json
import csv


def json_to_tsv():

    json_file = open("datatest.json", "r")
    json_data = json.load(json_file)
    json_file.close()

    data = json.dumps(json_data)

    tsv_file = open("data.tsv", "w")
    tsv_writer = csv.writer(tsv_file, delimiter='\t')

    tsv_writer.writerow(data[0].keys())

    for row in data:
        tsv_writer.writerow(row.values())

    tsv_file.close()


json_to_tsv()
