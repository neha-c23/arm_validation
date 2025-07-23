import openpyxl
from openpyxl.styles import Alignment

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

        # Collect full test messages
        current_test = []
        for line in lines:
            if line.startswith("[-]"):
                if current_test:
                    failed_tests.append("".join(current_test).strip())
                    current_test = []
                current_test.append(line)
            elif current_test:
                current_test.append(line)
        if current_test:
            failed_tests.append("".join(current_test).strip())

        # Collect parameters
        for line in lines:
            if "Custom params:" in line:
                custom_params = [param.strip() for param in line.split(":")[1].strip("{} \n").split(",")]
            elif "QS params:" in line:
                qs_params = [param.strip() for param in line.split(":")[1].strip("{} \n").split(",")]

except FileNotFoundError:
    print("results.txt file not found.")

# Determine the maximum number of rows needed
max_rows = max(len(failed_tests), len(custom_params), len(qs_params))

# Write data to Excel with wrap text enabled
for i in range(max_rows):
    if i < len(failed_tests):
        cell = ws.cell(row=i+2, column=1, value=failed_tests[i])
        cell.alignment = Alignment(wrap_text=True)
    if i < len(custom_params):
        cell = ws.cell(row=i+2, column=2, value=custom_params[i])
        cell.alignment = Alignment(wrap_text=True)
    if i < len(qs_params):
        cell = ws.cell(row=i+2, column=3, value=qs_params[i])
        cell.alignment = Alignment(wrap_text=True)

# Save the workbook
wb.save("validation_results.xlsx")
print("Excel file 'validation_results.xlsx' has been created successfully with wrap text enabled.")

