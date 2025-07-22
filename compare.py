import json

def load_parameters(file_path):
    with open(file_path, 'r', encoding = "utf-8-sig") as f:
        template = json.load(f)
    return set(template.get('parameters', {}).keys()) #store parameters of the template file in a set

def compare_parameters(maps_template_path, quickstart_template_path): 
    maps_params = load_parameters(maps_template_path) #parameters from MAPS template
    quickstart_params = load_parameters(quickstart_template_path) #parameters from azure quickstart template

    missing_params = quickstart_params - maps_params #extract params present in quickstart but not in MAPS template

    print("Parameters present in the Quickstart template but missing from the user's template:")
    for param in sorted(missing_params):
        print(param)

#call function
compare_parameters(r"C:\Users\1925zn\OneDrive - BP\MyFiles\TemplatesAgain\PostgresSQL\Azure PostgreSQL\Flexible_Server_Template.json", r"C:\Users\1925zn\OneDrive - BP\MyFiles\AZQuickstart\postgresql.json")

