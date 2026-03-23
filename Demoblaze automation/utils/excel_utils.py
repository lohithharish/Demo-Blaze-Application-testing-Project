def get_login_data(file_path, sheet_name):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook[sheet_name]

    data = []

    for row in sheet.iter_rows(min_row=2, values_only=True):
        username, password, expected = row
        data.append((username, password, expected))

    return data