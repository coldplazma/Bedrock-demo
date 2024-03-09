from langchain_community.chat_models import BedrockChat
import boto3
import os
import streamlit as st

# Environment variables for AWS credentials should be set in your deployment service
aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')

bedrock_client = boto3.client(
    service_name="bedrock-runtime",
    region_name="us-west-2",  # Updated to the correct region based on your previous message
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
)

modelID = "anthropic.claude-3-sonnet-20240229-v1:0"

llm = BedrockChat(
    model_id=modelID,
    client=bedrock_client,
    model_kwargs={
        "max_tokens": 1000,
        "anthropic_version": "bedrock-2023-05-31"
    }
)

def my_chatbot(freeform_text):
    messages = [
        {
            "role": "user",
            "content": freeform_text,
            "type": "text",
        }
    ]

    try:
        response = llm.invoke(messages)
        return response.content
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return "Sorry, I encountered an error. Please try again."

st.title("Claude 3 Sonnet Chatbot")

freeform_text = st.text_area(label="What's your question?", max_chars=100)

if freeform_text:
    response = my_chatbot(freeform_text)
    st.write(response)
