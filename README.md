---
page_type: sample
languages:
- python
products:
- azure
description: "These REST samples show you how to programmatically create,"
urlFragment: cognitive-services-qnamaker-python
---

# Cognitive Services QnA Maker Samples in Python

These REST samples show you how to programmatically create, update, publish, and replace a QnA Maker knowledge base, amongst many other ways to interact with it. All samples are in Python. To view these same samples in other languages:

[cognitive-services-qnamaker-csharp](https://github.com/Azure-Samples/cognitive-services-qnamaker-csharp)

[cognitive-services-qnamaker-java](https://github.com/Azure-Samples/cognitive-services-qnamaker-java)

[cognitive-services-qnamaker-nodejs](https://github.com/Azure-Samples/cognitive-services-qnamaker-nodejs)


## Features

Included are the following samples:

* [Create knowledge base](https://github.com/Azure-Samples/cognitive-services-qnamaker-python/blob/master/create-new-knowledge-base.py). Create a brand new knowledge base with given FAQ URLs. You may supply your own.
* [Update knowledge base](https://github.com/Azure-Samples/cognitive-services-qnamaker-python/blob/master/update-knowledge-base.py). Update an existing knowledge base by changing its name.
* [Publish knowledge base](https://github.com/Azure-Samples/cognitive-services-qnamaker-python/blob/master/publish-knowledge-base.py). Publish any existing knowledge base to the host your Azure account.
* [Replace knowledge base](https://github.com/Azure-Samples/cognitive-services-qnamaker-python/blob/master/replace-knowledge-base.py). Replace an entire existing knowledge base with a custom question/answer pair.
* [Download knowledge base](https://github.com/Azure-Samples/cognitive-services-qnamaker-python/blob/master/download-knowledge-base.py). Download the contents of your existing knowledge base in JSON.
* [Delete knowledge base](https://github.com/Azure-Samples/cognitive-services-qnamaker-python/blob/master/delete-knowledge-base.py). Delete an existing knowledge base, which has already been published.

All REST samples revolve around what you can do with a knowledge base, which is made up of FAQs or product manuals where there is a question and an answer. QnA Maker gives you more control over how to answer questions by allowing you to train a chat bot to give answers in a variety of ways that feels more like natural, conversational exchanges.

<img src="https://docs.microsoft.com/en-us/azure/cognitive-services/qnamaker/media/botFrameworkArch.png" width="700">

## Getting Started

### Prerequisites

For each sample, a subscription key is required from your Azure Portal account. 
* To create a new account/resource for QnA Maker, see [Create a Cognitive Services API account in the Azure portal](https://docs.microsoft.com/en-us/azure/cognitive-services/cognitive-services-apis-create-account). You may need to 'Search in Marketplace' for QnA Maker if you don't see it in the list given.  
* For existing accounts, the key can be found in your [Azure Portal](https://ms.portal.azure.com/) dashboard in your QnA Maker resource under Resource Management > Keys. 

With the exception of creating a new knowledge base, these samples will require your [QnA Maker account](https://www.qnamaker.ai/Home/MyServices) knowledge base ID. To find your knowledge base ID, go to [My knowledge bases](https://www.qnamaker.ai/Home/MyServices) and select `View Code` on the right. You'll see the http request and your knowledge base ID is in the topmost line: for example, `POST /knowledgebases/2700e6b9-91a1-41e9-a958-6d1a98735b10/...`. Use only the ID.

<img src="find-kb-id.png">

### Run the sample

1. Create a new python project in your favorite IDE or create one in [PyCharm](https://www.jetbrains.com/pycharm/), which has a free evaluation version. If using Pycharm, it is easiest to create one project, then fill it with python files (add to your root folder) for each sample.

1. Copy/paste the sample you want to test into a python file.

1. Add your Azure subscription key and your knowledge base ID (if applicable) at the top of the file where indicated.

1. Run the sample. In PyCharm, go to Run > Edit Configurations and add a new configuration (click the + sign) and choose which script path you want to use (select your python file), then select OK. Run the sample now.

1. Go to your knowledge bases in [qnamaker.ai](https://www.qnamaker.ai/Home/MyServices) to see changes.

### Quickstart

* Quickstart: [Create a new knowledge base in Python](https://docs.microsoft.com/en-us/azure/cognitive-services/qnamaker/quickstarts/create-new-kb-python)
* Quickstart: [Update a knowledge base in Python](https://docs.microsoft.com/en-us/azure/cognitive-services/qnamaker/quickstarts/update-kb-python)
* Quickstart: [Publish a knowledge base in Python](https://docs.microsoft.com/en-us/azure/cognitive-services/qnamaker/quickstarts/publish-kb-python)
* More quickstarts coming soon... in the meantime, refer to [Quickstart for Microsoft QnA Maker API with Python](https://docs.microsoft.com/en-us/azure/cognitive-services/qnamaker/quickstarts/python) for all quickstarts in minimal format.

## References

[QnA Maker V4.0](https://westus.dev.cognitive.microsoft.com/docs/services/5a93fcf85b4ccd136866eb37/operations/5ac266295b4ccd1554da75ff)
