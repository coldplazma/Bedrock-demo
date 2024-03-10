# Bedrock Chatbot YouTube Project

## Introduction
The goal of this phase of the project was to create a simple AI chatbot using Amazon Bedrock and the Anthropic Claude 3 Sonnet model. The chatbot would be accessible through a web interface built with the Streamlit library, allowing users to interact with the AI model by asking questions and receiving responses.

## Initial Code and Libraries
The project started with the following Python code and libraries:

- `langchain`: A Python library for building applications with large language models (LLMs).
- `langchain_community`: A community-driven extension of the langchain library.
- `boto3`: The AWS SDK for Python, used to interact with Amazon Bedrock.
- `streamlit`: A Python library for building interactive web applications.

The initial code set up the necessary environment variables, created a Bedrock client, and defined a function called `my_chatbot` to handle the user's input and generate a response from the AI model.

## Errors Encountered
During the development process, several errors were encountered:

1. **ProfileNotFound error**: This error occurred when the specified AWS profile could not be found. It was resolved by properly configuring the AWS credentials for the "BedrockProj" profile.
2. **ValidationError**: This error indicated that the Claude v3 model was not supported by the current version of the `langchain` library. The issue was resolved by using the `BedrockChat` class from the `langchain_community` library instead.
3. **AttributeError**: The error message suggested that the `message` object in the `_format_anthropic_messages` function did not have a `type` attribute. This was resolved by modifying the format of the messages passed to the `BedrockChat` class.

## Code Modifications
To resolve the encountered errors and improve the functionality of the chatbot, the following changes were made to the code:

- The `LLMChain` import and usage were removed, and the `BedrockChat` class was directly instantiated with the necessary parameters.
- The `my_chatbot` function was updated to use the `invoke` method of the `BedrockChat` class to generate a response from the model.
- The format of the messages passed to the `BedrockChat` class was modified to include the appropriate `role` and `content` attributes.

## Conclusion
Through the process of resolving errors and making necessary code modifications, the project successfully created a functional AI chatbot using Amazon Bedrock and the Anthropic Claude 3 Sonnet model. The chatbot can be accessed through a user-friendly web interface built with the Streamlit library, allowing users to interact with the AI model seamlessly.

## References
- [Amazon Bedrock](https://aws.amazon.com/bedrock/)
- [Anthropic Claude](https://www.anthropic.com/claude.html)
- [Streamlit](https://streamlit.io/)
- [Langchain](https://github.com/hwchase17/langchain)
- [Langchain Community](https://github.com/hwchase17/langchain-community)
- [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
