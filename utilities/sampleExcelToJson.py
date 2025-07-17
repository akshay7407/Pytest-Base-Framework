# import pandas as pd
# import json

# def convert_sheets_to_json(file_path):
#  # Read data from multiple sheets into a dictionary
#         data = {}
#         xls = pd.ExcelFile(file_path)
#         for sheet_name in xls.sheet_names:
#             sheet_data = xls.parse(sheet_name).replace({pd.NA: None}).to_dict(orient='records')
#             data[sheet_name] = sheet_data

#         # Convert the dictionary to JSON
#         json_data = json.dumps(data, indent=4)

#         return json_data

# if __name__ == "__main__":
#         file_path = 'D:\\Pytest-Base-Framework\\Sample Data.xlsx'
#         json_data = convert_sheets_to_json(file_path)
#         with open('output.json', 'w') as json_file:
#             json_file.write(json_data)  