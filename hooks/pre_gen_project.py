# Note: cookiecutter first makes the main level directory using
# directory_name from cookiecutter.json before running this hook

import json
import sys

# Load the context that cookiecutter has generated from the user inputs
with open('cookiecutter.json') as f:
    context = json.load(f)

# Update the context based on the user inputs
context.update({
    "package_name": context['package_name'].lower().replace(" ", "_").replace("-", "_"),
    "directory_name": context['directory_name'].lower().replace(" ", "-"),
    "full_name": context['full_name'].replace('"', '\\"'),
    "repository": "https://github.com/" + context['github_organization'] + "/" + context['directory_name'].lower().replace(" ", "-"),
    "package_short_description": context['package_short_description'].replace('"', '\\"'),
})

# Overwrite the cookiecutter.json file with the new context
with open('cookiecutter.json', 'w') as f:
    json.dump(context, f)

# Optional: print out the updated context or any messages
print("Updated context:", context)

