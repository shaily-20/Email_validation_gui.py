# Email_validiation.py
# Email Validation Checker with GUI
## Features

- **Validation Criteria**:
  - Ensures the email contains exactly one '@' symbol.
  - Validates the local part (before '@') for allowed characters.
  - Validates the domain part (after '@') for allowed characters and structure.
  - Checks that the local part is no longer than 64 characters.
  - Checks that the domain part is no longer than 255 characters.
  - Ensures no consecutive dots in the local part.
  - Ensures the local part doesn't start or end with a dot.

- **GUI Features**:
  - Simple and intuitive user interface.
  - Input field for entering email addresses.
  - Validate button to check the email address.
  - Informative messages indicating whether the email is valid or invalid, with specific reasons for invalidity
