import csv
import json

# https://docs.python.org/2/library/csv.html

with open('gl_table.csv') as csvfile:
    csvfile = csv.DictReader(csvfile)
    output = []
    for each in csvfile:
        row = {}
        row = {"model": "gl_table"}
        row['gl_acct'] = each['gl_acct']
        row['gl_desc'] = each['gl_desc']
        output.append(row)
    json.dump(output,open('converted_file.json','w'), indent=4, sort_keys=False)







# output =[]
# for each in csvfile:
#     row = {}
#     row['gl_acct'] = each['gl_acct']
#     row['gl_desc'] = each['gl_desc']
#     output.append(row)
# json.dump(output,open('filename.json','w'), indent=4, sort_keys=False)