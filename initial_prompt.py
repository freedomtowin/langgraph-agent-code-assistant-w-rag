template_str = """
{% set test_cases = test_case_data %}
errors = []

{% for case in test_cases %}
# Test case {{ loop.index }}
output = {{ function_name }}("{{ case.input }}")
if output != "{{ case.expected }}":
    err = f"Error: Expected '{{ case.expected }}', but got '{output}'"
    errors.append(err)
{% endfor %}

errors = "\\n".join(errors)
if errors:
    raise Exception(errors)
else:
    print("All test cases passed successfully.")
"""

from jinja2 import Template
import json
def create_test_case_code(function_name, test_case_data):

    # Create a Jinja2 template object
    template = Template(template_str)

    # Render the template, passing the test cases and function name
    rendered_code = template.render(function_name=function_name, test_case_data=test_case_data)
    return rendered_code


def create_question(function_name, description, test_case_data):

    format_test_cases = []
    for indx, tc in enumerate(test_case_data):
        tmp = f"{indx}. {json.dumps(tc)}"
        format_test_cases.append(tmp)

    format_test_cases = "\n".join(format_test_cases)
    prompt = (
        f"{description}\n\n"
        f"Create a function called: {function_name}.\n\n"
        f"Test cases:\n{format_test_cases}"
    )
    return prompt
    