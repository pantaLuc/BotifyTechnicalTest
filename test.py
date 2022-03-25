import json
FIELDS=[
    "id",
    "code",
    "name",
    "average_age",
    "district_code",
    "department_code",
    "region_code",
    "region_name",

]

def get_data(file):
    with open(file) as data_file:
        return json.load(data_file)

def process(data):
   
    where_clause = ""
    if isinstance(data, list):
        for part in data:
            if part not in FIELDS:
                
                where_clause += " ({}) ".format(process(part))
            else:
                where_clause += process(part)
    elif isinstance(data, dict):
        where_clause += " {}  '{}'".format("code=",data["code"] ,data["name"] ,data["average_age"] ,data["district_code"] ,data["department_code"] ,data["region_code"] ,data["region_name"])
    elif isinstance(data, str):
        return data
    return where_clause

def main():
    expression = get_data("file1.json")["fields"]
    where_clause = process(expression)

    return "SELECT * FROM Town  WHERE {}".format(where_clause)

if __name__ == '__main__':
    print(main())