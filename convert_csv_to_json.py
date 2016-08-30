import csv
import json

# https://docs.python.org/2/library/csv.html

with open('gl_table.csv') as csvfile:
    csvfile = csv.DictReader(csvfile)
    model_name = 'gl_table'
    field_1 = 'gl_acct'
    field_2 = 'gl_desc'
    x = 0
    output = []
    for each in csvfile:
        x += 1
        row = {}
        row = {'model': model_name, 'pk': x, 'fields': ({field_1: each['gl_acct'], field_2: each['gl_desc']})}
        output.append(row)
    json.dump(output, open('converted_file.json','w'), indent=4, sort_keys=False)


#........ json data model example......
# [
#   {
#     "model": "myapp.person",
#     "pk": 1,
#     "fields": {
#       "first_name": "John",
#       "last_name": "Lennon"
#     }
#   },
#   {
#     "model": "myapp.person",
#     "pk": 2,
#     "fields": {
#       "first_name": "Paul",
#       "last_name": "McCartney"
#     }
#   }
# ]