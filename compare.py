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
compare_parameters(r"https://raw.githubusercontent.com/neha-c23/arm_validation/refs/heads/main/templates/DeploymentTemplate_ASEv3_Generic.json", r"https://raw.githubusercontent.com/Azure/azure-quickstart-templates/4b98edf26a59f311fe599bef4e48850d55e5fb50/quickstarts/microsoft.web/web-app-asp-app-on-asev3-create/azuredeploy.json")

