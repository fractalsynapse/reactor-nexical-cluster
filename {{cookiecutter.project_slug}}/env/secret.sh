#
# ArgoCD environment variables
#
export ARGOCD_SERVER_SECRET="{secret_key}"
export ARGOCD_ADMIN_PASSWORD="{{cookiecutter.argocd_admin_password}}"
#
# Zimagi environment configurations
#
export POSTGRESQL_PASSWORD="{password}"
export REDIS_PASSWORD="{password}"
export QDRANT_PASSWORD="{password}"

export ZIMAGI_SECRET_KEY="{secret_key}"
export ZIMAGI_ADMIN_API_KEY="{strong_password}"

export ZIMAGI_EMAIL_HOST_USER="{{cookiecutter.admin_email_smtp_user}}"
export ZIMAGI_EMAIL_HOST_PASSWORD="{{cookiecutter.admin_email_smtp_password}}"

export GITHUB_API_KEY="{{cookiecutter.github_deploy_key}}"

export MAILGUN_API_KEY="{{cookiecutter.mailgun_api_key}}"
export MAILGUN_WEBHOOK_KEY="{{cookiecutter.mailgun_webhook_key}}"

export HUGGINGFACE_API_TOKEN="{{cookiecutter.huggingface_api_key}}"
export DEEPINFRA_API_KEY="{{cookiecutter.deepinfra_api_key}}"
#
# Interface environment configurations
#
export INTERFACE_SECRET_KEY="{secret_key}"
export INTERFACE_API_KEY=""
