# Pulumi Azure Demo
Azure docs:
[https://www.pulumi.com/registry/packages/azure-native/](https://www.pulumi.com/registry/packages/azure-native/)

## Starting a Pulumi Project for Azure
```sh
mkdir quickstart && cd quickstart
pulumi new azure-python
```

## Create Virtualenv
```sh
python3 -m venv venv && \
. venv/bin/activate && \
pip install --upgrade pip && \
pip install --no-cache-dir --upgrade -r requirements.txt
```

## Azure Login and set subscription, or do other configurations
[https://www.pulumi.com/registry/packages/azure-native/installation-configuration/](https://www.pulumi.com/registry/packages/azure-native/installation-configuration/)

```sh
az login
az account set --subscription=<id>
```

## Deploy
This command evaluates your program and determines the resource updates to make. First, a preview is shown that outlines the changes that will be made when you run the update:
```sh
pulumi up
```

## Stack output
```sh
pulumi stack output account_name
```

## Destroy
You’ll be prompted to make sure you really want to delete these resources. This can take a minute or two; Pulumi waits until all resources are shut down and deleted before it considers the destroy operation to be complete.
```sh
pulumi destroy
```

## Delete Stack
Note that this removes the stack entirely from the Pulumi Service, along with all of its update history.
```sh
pulumi stack rm
```