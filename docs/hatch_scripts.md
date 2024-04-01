
# Hatch Scripts Reference

`hatch run <env-name>:<script-name>`

- Run script in an environment.
- If no environment supplied, use current environment if any, otherwise use default environment

## Defining Scripts

`script-name = "command"` or `["script1", "command1", "command2", ...]`

- The value supplied to each script is the command to run as a string or a set of commands to run as a list of strings
- The value can contain variables that will be replaced when the script is run
- The value can refer to previously defined scripts by name
- Script names starting with _ are hidden and will not be displayed in the output of hatch env show

# Variable Syntax

`{variable-name:default-value}`

- default-value is optional and only used if the variable is not defined or empty

# Special Variables

`{args:tests}`

- Replaced with user supplied args, or "tests" if no args are supplied

`{env:FOO:bar}`

- Uses the value of the FOO environment variable, or "bar" if it is not defined

`{matrix:python:3.11}`

- Uses the value of the python matrix variable, or "3.11" if it is not defined

`{env_name}, {env_type}, {verbosity}`

- The name, type, or verbosity level of the environment
