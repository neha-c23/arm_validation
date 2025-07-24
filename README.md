# ARM Templates validation automation  
  
### Purpose:  
Microsoft releases new ARM template schemas and resource API versions regularly, adding new features and updating the syntax for its ARM templates. 
The MAPS custom ARM templates repository supports BP’s resource deployment automation pipelines. It is supported by deprecated schemas and old API versions. According to Microsoft best practices, API versions must not be more than 730 days old, if newer versions are available.  
  
However, automating addition of regular updates to the ARM templates cannot be done, since they are protected and constrained by policies and governance for security compliance. Concerned team members must review suggestions before changing the templates, so that they are in line with BP’s governance policies.  
Thus, I propose this workflow, which will provide the team (or concerned stakeholders) a one-shot view of suggested updates and additions to the custom ARM Templates repository on a regular basis.  
At present, it is a primitive workflow for:  
1. Automating the validation of custom ARM templates with Microsoft best practices.  
2. Suggesting new parameters based on Microsoft-recommended sample templates, one template at a time.  
   
### Repository structure:  
arm_validation/  
├── .github/  
│   └── workflows/  
│       └── arm-template-validation.yml  
├── templates/  
│   └── azuredeploy.json  
├── tools/  
│   └── arm-ttk/  
│       └── arm-ttk.psd1  
│       └── Test-AzTemplate.ps1  
├── generate_excel.py  
└── compare.py  
  
The arm-template-validation.yml:  
1.	Carries out a suite of tests on the ARM template to validate the following:  
•	Validating the author’s intent (eg. unused parameters or variables)  
•	Security practices for the language (eg. outputting secrets in plain text)  
•	Using the appropriate language construct for the task at hand (eg. using environmental functions instead of hard-coding values).   
2.	 Runs a Python script (compare.py) to print parameters present in the custom ARM template and those in the corresponding Quickstart template.  
3.	 generate_excel.py compiles all the results and produces an artifact in .xlsx format.  
  
### Directions for use:  
The workflow has a workflow_dispatch trigger, that can be manually activated under the Actions tab of the repository.  
It is also triggered when a new template file is pushed to the .\templates folder.  
   
### Output:   
The workflow generates a downloadable artifact - a validate_results.xlsx file - that contains the list of failed arm-ttk tests, and the parameters contained in both - the custom template and the Azure Quickstart sample template.  
  
### Important note: The workflow can currently validate one template at a time.   
  
  
### Planned enhancements:  
The repository has been set up so that it can validate multiple templates at once. All templates must be added to the .\templates folder, and on triggering the workflow, all the templates will be validated at once.  
The Test-AzTemplate cmdlet can test multiple templates at once. The user can also select unit tests to conduct on the templates, according to their business needs.  
  
The issue arises in the compare.py script, which is highly primitive. At present, it can only handle one template at a time. To scale it up for accommodating more templates, we can:  
1.	Add a metadata label to the custom ARM templates, containing the name of the Azure resource being deployed by that template.  
2.	The Python script can be configured to fetch the corresponding sample Azure template from Azure’s Quickstart repository.  
3.	The generate_excel.py script must be configured to generate multiple sheets in one workbook, one corresponding to each resource.  
  

