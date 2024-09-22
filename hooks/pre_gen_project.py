"""
NOTE:
    the below code maintains the Base Reactor Cluster
    CookieCutter Django project initialization

    * It sets local environment variables
    * It managed the OS license and community files

"""

TERMINATOR = "\x1b[0m"
WARNING = "\x1b[1;33m [WARNING]: "
INFO = "\x1b[1;33m [INFO]: "
HINT = "\x1b[3;33m"
SUCCESS = "\x1b[1;32m [SUCCESS]: "

# The content of this string is evaluated by Jinja, and plays an important role.
# It updates the cookiecutter context to trim leading and trailing spaces
# from values
"""
{{ cookiecutter.update({ "ingress_node_port": cookiecutter.ingress_node_port | trim }) }}
{{ cookiecutter.update({ "argocd_admin_password": cookiecutter.argocd_admin_password | trim }) }}
{{ cookiecutter.update({ "github_org": cookiecutter.github_org | trim }) }}
{{ cookiecutter.update({ "github_deploy_key": cookiecutter.github_deploy_key | trim }) }}
{{ cookiecutter.update({ "mailgun_domain": cookiecutter.mailgun_domain | trim }) }}
{{ cookiecutter.update({ "mailgun_api_key": cookiecutter.mailgun_api_key | trim }) }}
{{ cookiecutter.update({ "mailgun_webhook_key": cookiecutter.mailgun_webhook_key | trim }) }}
{{ cookiecutter.update({ "from_email": cookiecutter.from_email | trim }) }}
{{ cookiecutter.update({ "contact_email": cookiecutter.contact_email | trim }) }}
{{ cookiecutter.update({ "admin_email_smtp_domain": cookiecutter.admin_email_smtp_domain | trim }) }}
{{ cookiecutter.update({ "admin_email_smtp_port": cookiecutter.admin_email_smtp_port | trim }) }}
{{ cookiecutter.update({ "admin_email_smtp_user": cookiecutter.admin_email_smtp_user | trim }) }}
{{ cookiecutter.update({ "admin_email_smtp_password": cookiecutter.admin_email_smtp_password | trim }) }}
{{ cookiecutter.update({ "huggingface_api_key": cookiecutter.huggingface_api_key | trim }) }}
{{ cookiecutter.update({ "deepinfra_api_key": cookiecutter.deepinfra_api_key | trim }) }}
"""

project_slug = "{{ cookiecutter.project_slug }}"
if hasattr(project_slug, "isidentifier"):
    assert project_slug.isidentifier(), "'{}' project slug is not a valid Python identifier.".format(project_slug)

assert project_slug == project_slug.lower(), "'{}' project slug should be all lowercase".format(project_slug)
