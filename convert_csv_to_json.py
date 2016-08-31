import csv
import json

# https://docs.python.org/2/library/csv.html
file_name = 'gl_table.csv'
with open(file_name) as csvfile:
    csvfile = csv.DictReader(csvfile)
    app_name = 'myapp'
    model_name = 'GlTable'
    field_1 = 'gl_acct'
    field_2 = 'gl_desc'
    x = 0
    output = []
    for each in csvfile:
        x += 1
        row = {}
        row = {'model': app_name+'.'+model_name, 'pk': x, 'fields': ({field_1: each[field_1], field_2: each[field_2]})}
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