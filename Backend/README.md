# Virtual enviourments
A virtual enviourment is used to manage Python packages for different projects. This allows you to avoid installing Python packages globally which could break system tools or other projects.

## Create virtual enviourment

    Windows: py -m venv python_env
    Linux: python3 -m venv python_env
    
Don't forget to add the generated enviourment files to your .gitignore-file.

## Activate virtual enviourment
### activate

    Windows: .\python_env\Scripts\activate
    Linux: source python_env/bin/activate
To deactivate, use: `deactivate`

### Powershell issues
If activation does not work in PowerShell, give yourself right to do so.
1. Open PowerShell in administrator-mode
2. `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

### More info

More info: [https:/go.microsoft.com/fwlink/?LinkID=135170](https:/go.microsoft.com/fwlink/?LinkID=135170)

## Info about python virtual enviourments
 https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/

# Requirements (packages)
## Install required packages
To install required packages, open a virtual enviourment and run:

    pip install -r requirements.txt

### More information
`pip list` Shows a list of installed packages.

See this link for more information about requirements.txt
https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/
