import openpyxl

# Create a new Excel workbook and select the active worksheet
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Validation Results"

# Set headers
ws['A1'] = 'FAILED TESTS'
ws['B1'] = 'SUGGESTED PARAMS'

# Read failed tests and suggested parameters from results.txt
failed_tests = []
suggested_params = []

try:
    with open("results.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
        in_suggested_section = False
        for line in lines:
            if "Describing" in line and "FAIL" in line:
                failed_tests.append(line.strip())
            if "## Python Script Output" in line:
                in_suggested_section = True
                continue
            if in_suggested_section and line.strip():
                suggested_params.append(line.strip())
except FileNotFoundError:
    print("results.txt file not found.")

# Determine the maximum number of rows needed
max_rows = max(len(failed_tests), len(suggested_params))

# Write data to Excel
for i in range(max_rows):
    if i < len(failed_tests):
        ws.cell(row=i+2, column=1, value=failed_tests[i])
    if i < len(suggested_params):
        ws.cell(row=i+2, column=2, value=suggested_params[i])

# Save the workbook
wb.save("validation_results.xlsx")
print("Excel file 'validation_results.xlsx' has been created successfully.")

