import openpyxl

excel_file_path = 'Try.xlsx'
udid_list = []

workbook = openpyxl.load_workbook(excel_file_path)
sheet = workbook.active

for udid in sheet.iter_rows(min_col=1, max_col=1, values_only=True):
    udid_list.append(udid[0])

for i in udid_list:
    print(f"iOS:///{i}")
