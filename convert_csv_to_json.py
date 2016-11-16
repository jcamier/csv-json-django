import csv
import json

# https://docs.python.org/2/library/csv.html
file_name = 'gl_table.csv' # use the csv file that you are trying to upload
with open(file_name) as csvfile:
    csvfile = csv.DictReader(csvfile)
    app_name = 'myapp' # change this to your Django app name
    model_name = 'GlTable' # the name of you Django model
    field_1 = 'gl_acct' # the name of first field
    field_2 = 'gl_desc' # the name of second field
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
