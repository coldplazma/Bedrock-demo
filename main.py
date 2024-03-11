from langchain_community.chat_models import BedrockChat
import boto3
import os
import streamlit as st

# Load AWS credentials from environment variables
aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')

# Initialize a boto3 client for the Bedrock AI service
bedrock_client = boto3.client(
    service_name="bedrock-runtime",
    region_name="us-west-2",  # Make sure the region matches the service availability
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
)

# Define the model ID for the Bedrock language model
modelID = "anthropic.claude-3-sonnet-20240229-v1:0"

# Create an instance of BedrockChat with the specific language model
llm = BedrockChat(
    model_id=modelID,
    client=bedrock_client,
    model_kwargs={
        "max_tokens": 1000,  # Set the maximum number of tokens to be generated
        "anthropic_version": "bedrock-2023-05-31"  # Version of the model
    }
)

# Define a function to interact with the chatbot model
def my_chatbot(freeform_text):
    # Prepare the user's input message
    messages = [
        {
            "role": "user",
            "content": freeform_text,  # User-provided text
            "type": "text",
        }
    ]

    # Attempt to get a
