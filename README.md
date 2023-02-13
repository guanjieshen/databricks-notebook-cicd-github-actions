# databricks-notebook-cicd-github-actions

This is a sample project for Databricks showcasing how to leverage DBX with Github Actions.


## CICD pipeline settings

Configure `DATABRICKS_HOST` and `DATABRICKS_TOKEN` secrets for your project in [GitHub UI](https://docs.github.com/en/actions/security-guides/encrypted-secrets).

## Deploying from IDE (Local Machine)
The workflow can also be deployed and restarted locally using the following commands in the terminal:

1. Deploy updated job configuration
`dbx deploy --deployment-file=conf/dev-deployment.yml --no-rebuild`

<br>

2. Start job, and restart and current executions
`dbx launch --job=databricks-notebook-cicd-ado-dev --existing-runs=cancel `