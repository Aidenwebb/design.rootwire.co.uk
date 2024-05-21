# design.rootwire.co.uk
The codebase for https://design.rootwire.co.uk


Inspired by [https://github.com/canonical/design.ubuntu.com]


## How to work on this repository

On Windows
```pwsh
# Create Python Virtual Environment
python -m venv .venv

# Permit execution of unsigned Powershell scripts for the current process only
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process 

# Activate Python Virtual Environment
. .\.venv\Scripts\activate
```

## To run with debugger

```bash
# Run flask webapp
flask --app webapp/app --debug run
```

[Flask Documentation](https://flask.palletsprojects.com/en/3.0.x/quickstart/)


# Email and phone icons credits

https://www.flaticon.com/free-icons/phone-email

<a href="https://www.flaticon.com/free-icons/email" title="email icons">Email icons created by laterunlabs - Flaticon</a><br>
<a href="https://www.flaticon.com/free-icons/phone" title="phone icons">Phone icons created by Azland Studio - Flaticon</a>