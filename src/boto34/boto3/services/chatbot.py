"""
Wrapper for boto3 Chatbot service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_chatbot/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.boto3 import Session

    # Wrapper for boto3.Session constructor
    # Returns boto34.Session inherited from boto3.Session
    session = Session()
    session: boto34.boto3.session.Session

    # Type annotated boto3.Client
    # Uses the same arguments as boto3.client method
    # Returns type annotated boto3 Chatbot client
    chatbot_client = session.chatbot.client()
    chatbot_client: types_boto3_chatbot.client.ChatbotClient
    ```
"""

from __future__ import annotations

from types_boto3_chatbot.client import ChatbotClient

from boto34.boto3.service_factory import ServiceFactory


class ChatbotService(ServiceFactory[ChatbotClient]):
    SERVICE_NAME = "chatbot"
    _SERVICE_PROP = "chatbot"
