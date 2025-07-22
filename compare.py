import json
import urllib.request

def load_parameters_from_url(url):
    with urllib.request.urlopen(url) as response:
        data = response.read().decode('utf-8-sig')
        template = json.loads(data)
    return set(template.get('parameters', {}).keys())

def compare_parameters(maps_template_url, quickstart_template_url): 
    maps_params = load_parameters_from_url(maps_template_url)
    quickstart_params = load_parameters_from_url(quickstart_template_url)

    missing_params = quickstart_params - maps_params

    print("Parameters present in the Quickstart template but missing from the user's template:")
    for param in sorted(missing_params):
        print(param)

# Call the function with URLs
compare_parameters(
    "https://raw.githubusercontent.com/neha-c23/arm_validation/refs/heads/main/templates/DeploymentTemplate_ASEv3_Generic.json",
    "https://raw.githubusercontent.com/Azure/azure-quickstart-templates/4b98edf26a59f311fe599bef4e48850d55e5fb50/quickstarts/microsoft.web/web-app-asp-app-on-asev3-create/azuredeploy.json"
)
