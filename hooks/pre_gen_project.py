# Note: cookiecutter first makes the main level directory using
# directory_name from cookiecutter.json before running this hook

import re
import sys

# Function to validate the package name
def is_valid_package_name(name):
    return re.match("^[a-zA-Z_][a-zA-Z0-9_]*$", name)

# Access the cookiecutter dictionary which contains all the input variables
package_name = '{{ cookiecutter.package_name }}'
directory_name = '{{ cookiecutter.directory_name }}'
full_name = '{{ cookiecutter.full_name }}'
github_organization = '{{ cookiecutter.github_organization }}'
package_short_description = '{{ cookiecutter.package_short_description }}'

# Perform your manipulations
package_name = package_name.lower().replace(" ", "_").replace("-", "_")
directory_name = directory_name.lower().replace(" ", "-")
full_name = full_name.replace('"', '\\"')
repository = "https://github.com/{}/{}".format(github_organization, directory_name)
package_short_description = package_short_description.replace('"', '\\"')

# Example of using the validation function
if not is_valid_package_name(package_name):
    print('ERROR: The package name "{}" is not a valid Python package name.'.format(package_name))
    # Exit with an error code
    sys.exit(1)

# You would typically set these variables in the context without writing back to cookiecutter.json.
# The values would be available in the template files directly using the cookiecutter object.

print('Everything is fine with the inputs.')
