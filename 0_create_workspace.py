# check azure ML version
from azureml.core import Workspace
import azureml.core
# print(azureml.core.VERSION)


# Create workspace object
ws = Workspace.create(name='dp_machine_learning_1',
                      subscription_id='1f022c9f-0a99-45e9-aa02-a62ae7a41e6a',
                      resource_group='Dex_machine_learning',
                      create_resource_group=False,
                      location='eastus2'
                     )