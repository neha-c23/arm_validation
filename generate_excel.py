import openpyxl

# Create a new Excel workbook and select the active worksheet
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Validation Results"

# Set headers
ws['A1'] = 'FAILED TESTS'
ws['B1'] = 'CUSTOM TEMPLATE PARAMETERS'
ws['C1'] = 'QS TEMPLATE PARAMETERS'

# Read failed tests and suggested parameters from results.txt
failed_tests = []
custom_params = []
qs_params = []

try:
    with open("results.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
        in_suggested_section = False

        for line in lines:
            if "[-]" in line:
                failed_tests.append(line)
            if line == "**********************":
                break

        for line in lines:
            if "Custom Params" in line:
                in_suggested_section = True
                continue
            if in_suggested_section:
                custom_params.append(line.strip())
            if "QS Params" in line:
                in_suggested_section = False
            if in_suggested_section == False:
                qs_params.append(line)
except FileNotFoundError:
    print("results.txt file not found.")

# Determine the maximum number of rows needed
max_rows = max(len(failed_tests), len(custom_params), len(qs_params))

# Write data to Excel
for i in range(max_rows):
    if i < len(failed_tests):
        ws.cell(row=i+2, column=1, value=failed_tests[i])
    if i < len(custom_params):
        ws.cell(row=i+2, column=2, value=custom_params[i])
    if i<len(qs_params):
        ws.cell(row = i+2, column = 3, value = qs_params[i])

# Save the workbook
wb.save("validation_results.xlsx")
print("Excel file 'validation_results.xlsx' has been created successfully.")

