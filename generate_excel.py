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

        # Collect full failed test messages
        current_message = ""
        for line in lines:
            if "[-]" in line:
                if current_message:
                    failed_tests.append(current_message.strip())
                current_message = line
            elif current_message and "[+]" not in line:
                current_message += line
        if current_message:
            failed_tests.append(current_message.strip())

        # Collect custom and QS parameters
        for line in lines:
            if "Custom params" in line:
                custom_params = [param.strip() for param in line.split(":")[1].strip("{} \n").split(",")]
            elif "QS params" in line:
                qs_params = [param.strip() for param in line.split(":")[1].strip("{} \n").split(",")]

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
    if i < len(qs_params):
        ws.cell(row=i+2, column=3, value=qs_params[i])

# Save the workbook
wb.save("validation_results.xlsx")
print("Excel file 'validation_results.xlsx' has been created successfully.")

