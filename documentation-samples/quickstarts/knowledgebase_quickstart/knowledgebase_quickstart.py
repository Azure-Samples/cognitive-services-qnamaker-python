# <dependencies>
import os
import time

# To install these packages, run:
# python -m pip install msrest
# python -m pip install azure.cognitiveservices.knowledge.qnamaker

from azure.cognitiveservices.knowledge.qnamaker.authoring import QnAMakerClient
from azure.cognitiveservices.knowledge.qnamaker.authoring.models import QnADTO, MetadataDTO, CreateKbDTO, OperationStateType, UpdateKbOperationDTO, UpdateKbOperationDTOAdd
from azure.cognitiveservices.knowledge.qnamaker.runtime import QnAMakerRuntimeClient
from azure.cognitiveservices.knowledge.qnamaker.runtime.models import QueryDTO
from msrest.authentication import CognitiveServicesCredentials, ApiKeyCredentials
# </dependencies>

# This sample does the following tasks.
# - Create a knowledge base.
# - Update a knowledge base.
# - Publish a knowledge base.
# - Download a knowledge base.
# - Query a knowledge base.
# - Delete a knowledge base.

# <resourcekeys>
key_var_name = 'QNA_MAKER_SUBSCRIPTION_KEY'
if not key_var_name in os.environ:
	raise Exception('Please set/export the environment variable: {}'.format(key_var_name))
subscription_key = os.environ[key_var_name]

# The QnA Maker authoring endpoint has the form:
# https://<your resource name>.cognitiveservices.azure.com
host_var_name = 'QNA_MAKER_ENDPOINT'
if not host_var_name in os.environ:
	raise Exception('Please set/export the environment variable: {}'.format(host_var_name))
host = os.environ[host_var_name]

# The QnA Maker runtime endpoint has the form:
# https://<your resource name>.azurewebsites.net
runtime_endpoint_var_name = 'QNA_MAKER_RUNTIME_ENDPOINT'
if not runtime_endpoint_var_name in os.environ:
	raise Exception('Please set/export the environment variable: {}'.format(runtime_endpoint_var_name))
runtime_endpoint = os.environ[runtime_endpoint_var_name]
# </resourcekeys>

# Helper functions
# <monitorOperation>
def _monitor_operation(client, operation):

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

# <downloadkb>
def download_kb(client, kb_id):
	kb_data = client.knowledgebase.download(kb_id=kb_id, environment="Prod")
	print("KB Downloaded. It has {} QnAs.".format(len(kb_data.qna_documents)))
# </downloadkb>

# <query>
def query_kb(client, kb_id):
# Payload type is QueryDTO. See:
# https://github.com/Azure/azure-sdk-for-python/blob/master/sdk/cognitiveservices/azure-cognitiveservices-knowledge-qnamaker/azure/cognitiveservices/knowledge/qnamaker/runtime/models/query_dto_py3.py
	payload = QueryDTO(question="How do I manage my knowledgebase?")
	result = client.runtime.generate_answer(kb_id=kb_id, generate_answer_payload=payload)
# Result type is QnASearchResultList. See:
# https://github.com/Azure/azure-sdk-for-python/blob/master/sdk/cognitiveservices/azure-cognitiveservices-knowledge-qnamaker/azure/cognitiveservices/knowledge/qnamaker/runtime/models/qn_asearch_result_list_py3.py
# https://github.com/Azure/azure-sdk-for-python/blob/master/sdk/cognitiveservices/azure-cognitiveservices-knowledge-qnamaker/azure/cognitiveservices/knowledge/qnamaker/runtime/models/qn_asearch_result_py3.py
	answers = result.answers
	print("Results:")
	for answer in answers:
		print("Answer: {}".format(answer.answer))
		print("Score: {}".format(answer.score))
		print()
# </query>

# <deletekb>
def delete_kb(client, kb_id):
	client.knowledgebase.delete(kb_id=kb_id)
# </deletekb>

# Main

# <authorization>
def get_runtime_endpoint_key(client):
	result = client.endpoint_keys.get_keys()
	return result.primary_endpoint_key

client = QnAMakerClient(endpoint=host, credentials=CognitiveServicesCredentials(subscription_key))

# You cannot authenticate to the QnA Maker runtime endpoint with the
# subscription key you use to authenticate to the authoring endpoint. Instead,
# you use a runtime endpoint key that you can obtain via the authoring
# endpoint.
# The runtime endpoint expects a header named "Authorization" with the value:
# EndpointKey <runtime endpoint key>
runtime_endpoint_key = get_runtime_endpoint_key(client)
runtime_client = QnAMakerRuntimeClient(runtime_endpoint=runtime_endpoint, credentials=ApiKeyCredentials({"Authorization": "EndpointKey " + runtime_endpoint_key}))
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

# Query the KB
print("Sending query to KB...")
query_kb (client=runtime_client, kb_id=kb_id)
print()

# Delete the KB
print("Deleting KB...")
delete_kb (client=client, kb_id=kb_id)
print("KB Deleted.")
