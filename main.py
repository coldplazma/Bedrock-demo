from langchain_community.chat_models import BedrockChat
import boto3
import os
import streamlit as st

os.environ["AWS_PROFILE"] = "BedrockProj"

bedrock_client = boto3.client(
    service_name="bedrock-runtime",
    region_name="us-west-2"
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
    # Add "type": "user" to the message (lowercase)
    messages = [
        {
            "role": "user",
            "content": freeform_text,
            "type": "text",  # Comma added
        }  # Indentation fixed
    ]

    # ... rest of the code


    try:
        response = llm.invoke(messages)
        return response.content
    except Exception as e:
        print(f"An error occurred: {e}")
        return "Sorry, I encountered an error. Please try again."


st.title("Claude 3 Sonnet Chatbot")

freeform_text = st.text_area(label="What's your question?", max_chars=100)

if freeform_text:
    response = my_chatbot(freeform_text)
    st.write(response)