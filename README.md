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
└── compare.py  
  
Output:  
The workflow generates an artifact - a results.txt file - that contains the results of all the tests run by arm-ttk, and the additional parameters that can be added to the custom template  
