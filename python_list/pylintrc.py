import sys

pylint_config = pylint.RcFile()

# Add additional pylint configuration options
pylint_config['disable'] = ['invalid-name', 'missing-docstring']
pylint_config['max-line-length'] = 100
pylint_config['import-error'] = 'ignore-on-third-party'

# Process all Python files in the current directory and its subdirectories, except for the `tests` directory
sys.exit(pylint.lint_from_file_list(['.'], exclude=['tests']))