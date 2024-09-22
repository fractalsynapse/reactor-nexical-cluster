#
# ArgoCD environment configurations
#
export ARGOCD_PROJECT_SEQUENCE='[
  "system",
  "platform",
  "database",
  "management"
]'
#
# Cluster environment configurations
#
export GATEWAY_NODE_PORT="{{cookiecutter.ingress_node_port}}"
#
# Zimagi environment configurations
#
export ZIMAGI_GITHUB_ORG="{{cookiecutter.github_org}}"

export ZIMAGI_EMAIL_HOST_DOMAIN="{{cookiecutter.admin_email_smtp_domain}}"
export ZIMAGI_EMAIL_HOST_PORT="{{cookiecutter.admin_email_smtp_port}}"

export MAILGUN_DOMAIN="{{cookiecutter.mailgun_domain}}"
#
# Interface environment configurations
#
export INTERFACE_FROM_EMAIL="{{cookiecutter.from_email}}"
export INTERFACE_CONTACT_EMAIL="{{cookiecutter.contact_email}}"
