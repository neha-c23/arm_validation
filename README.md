# ARM Templates validation  

A primitive workflow for:  
1. Automating the validation of custom ARM templates with Microsoft best practices  
2. Suggesting new parameters based on Microsoft-recommended sample templates.  

Repository structure:  
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
  
Output:  
The workflow generates an artifact - a validate_results.xlsx file - that contains the results of all the tests run by arm-ttk, and the parameters contained in both, the custom template and the Azure Quickstart sample template. 
