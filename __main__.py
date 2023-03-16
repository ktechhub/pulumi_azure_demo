"""An Azure RM Python Pulumi program"""

import pulumi
from pulumi_azure_native import storage
from pulumi_azure_native import resources
import pulumi_azure_native as azure_native

# Create an Azure Resource Group
resource_group = resources.ResourceGroup('resource_group', location="eastus")

# Create an Azure resource (Storage Account)
account = storage.StorageAccount('sa',
    resource_group_name=resource_group.name,
    sku=storage.SkuArgs(
        name=storage.SkuName.STANDARD_LRS,
    ),
    kind=storage.Kind.STORAGE_V2)

# Export the account name
pulumi.export("account_name", account.name)
pulumi.export("account_type", account.type)
pulumi.export("account_location", account.location)










# Key vault creation
vault = azure_native.keyvault.Vault("vault",
    location="eastus",
    properties=azure_native.keyvault.VaultPropertiesArgs(
        access_policies=[{
            "objectId": "00000000-0000-0000-0000-000000000001",
            "permissions": azure_native.keyvault.PermissionsArgs(
                certificates=[
                    "get",
                    "list",
                    "delete",
                    "create",
                    "import",
                    "update",
                    "managecontacts",
                    "getissuers",
                    "listissuers",
                    "setissuers",
                    "deleteissuers",
                    "manageissuers",
                    "recover",
                    "purge",
                ],
                keys=[
                    "encrypt",
                    "decrypt",
                    "wrapKey",
                    "unwrapKey",
                    "sign",
                    "verify",
                    "get",
                    "list",
                    "create",
                    "update",
                    "import",
                    "delete",
                    "backup",
                    "restore",
                    "recover",
                    "purge",
                ],
                secrets=[
                    "get",
                    "list",
                    "set",
                    "delete",
                    "backup",
                    "restore",
                    "recover",
                    "purge",
                ],
            ),
            "tenantId": "47d43b05-8a98-4be2-91f6-bc8af5832a28",
        }],
        enabled_for_deployment=True,
        enabled_for_disk_encryption=True,
        enabled_for_template_deployment=True,
        sku=azure_native.keyvault.SkuArgs(
            family="A",
            name=azure_native.keyvault.SkuName.STANDARD,
        ),
        tenant_id="47d43b05-8a98-4be2-91f6-bc8af5832a28",
    ),
    resource_group_name=resource_group.name,
    vault_name="samplevault2487536213334")


pulumi.export("vault_id", vault.id)
pulumi.export("vault_name", vault.name)
pulumi.export("vault_type", vault.type)