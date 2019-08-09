# <dependencies>
import os
import time

from azure.cognitiveservices.knowledge.qnamaker import QnAMakerClient
from azure.cognitiveservices.knowledge.qnamaker.models import QnADTO, MetadataDTO, CreateKbDTO, OperationStateType, UpdateKbOperationDTO, UpdateKbOperationDTOAdd
from msrest.authentication import CognitiveServicesCredentials
# </dependencies>

# This sample does the following tasks.
# - Create a knowledge base.
# - Update a knowledge base.
# - Publish a knowledge base.
# - Download a knowledge base.
# - Delete a knowledge base.

# <resourcekeys>
key_var_name = 'QNAMAKER_KEY'
if not key_var_name in os.environ:
	raise Exception('Please set/export the environment variable: {}'.format(key_var_name))
subscription_key = os.environ[key_var_name]

host_var_name = 'QNAMAKER_HOST'
if not host_var_name in os.environ:
	raise Exception('Please set/export the environment variable: {}'.format(host_var_name))
host = os.environ[host_var_name]
# </resourcekeys>

# Helper functions
# <monitorOperation>
def _monitor_operation(client, operation):
    """Helper function for knowledge_based_crud_sample.

    This helper function takes in a QnAMakerClient and an operation, and loops until the operation has either succeeded
    or failed and returns the operation.
    """
    for i in range(20):
        if operation.operation_state in [OperationStateType.not_started, OperationStateType.running]:
            print("Waiting for operation: {} to complete.".format(operation.operation_id))
            time.sleep(5)
            operation = client.operations.get_details(operation_id=operation.operation_id)
        else:
            break
    if operation.operation_state != OperationStateType.succeeded:
        raise Exception("Operation {} failed to complete.".format(operation.operation_id))
    return operation
# </monitorOperation>

# <createkb>
def create_kb(client):
    """Helper function for knowledge_based_crud_sample.

    This helper function takes in a QnAMakerClient and returns an operation of a created knowledge base.
    """
    qna = QnADTO(
        answer="You can use our REST APIs to manage your knowledge base.",
        questions=["How do I manage my knowledgebase?"],
        metadata=[MetadataDTO(name="Category", value="api")]
    )
    urls = ["https://docs.microsoft.com/en-in/azure/cognitive-services/qnamaker/faqs"]
    create_kb_dto = CreateKbDTO(
        name="QnA Maker FAQ from quickstart",
        qna_list=[qna],
        urls=urls
    )
    create_op = client.knowledgebase.create(create_kb_payload=create_kb_dto)
    create_op = _monitor_operation(client=client, operation=create_op)
    return create_op.resource_location.replace("/knowledgebases/", "")
# </createkb>

# <updatekb>
def update_kb(client, kb_id):
    update_kb_operation_dto = UpdateKbOperationDTO(
        add=UpdateKbOperationDTOAdd(
            qna_list=[
                QnADTO(questions=["bye"], answer="goodbye")
            ]
        )
    )
    update_op = client.knowledgebase.update(kb_id=kb_id, update_kb=update_kb_operation_dto)
    _monitor_operation(client=client, operation=update_op)
# </updatekb>

# <publishkb>
def publish_kb(client, kb_id):
    client.knowledgebase.publish(kb_id=kb_id)
# </publishkb>

# <deletekbs>
def download_kb(client, kb_id):
	kb_data = client.knowledgebase.download(kb_id=kb_id, environment="Prod")
	print("KB Downloaded. It has {} QnAs.".format(len(kb_data.qna_documents)))

def delete_kb(client, kb_id):
	client.knowledgebase.delete(kb_id=kb_id)
# </deletekbs>

# Main

# <authorization>
client = QnAMakerClient(endpoint=host, credentials=CognitiveServicesCredentials(subscription_key))
# </authorization>

# Create a KB
print("Creating KB...")
kb_id = create_kb(client=client)
print("Created KB with ID: {}".format(kb_id))
print()

# Update a KB
print("Updating KB...")
update_kb (client=client, kb_id=kb_id)
print("KB Updated.")
print()

# Publish the KB
print("Publishing KB...")
publish_kb (client=client, kb_id=kb_id)
print("KB Published.")
print()

# Download the KB
print("Downloading KB...")
download_kb (client=client, kb_id=kb_id)
print()

# Delete the KB
print("Deleting KB...")
delete_kb (client=client, kb_id=kb_id)
print("KB Deleted.")
