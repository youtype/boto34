"""
Wrapper for aioboto3 Chatbot service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_chatbot/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aioboto3 import Session

    # Wrapper for aioboto3.Session constructor
    # Returns boto34.Session inherited from aioboto3.Session
    session = Session()
    session: boto34.aioboto3.session.Session

    # Type annotated aioboto3.Client
    # Uses the same arguments as aioboto3.client method
    # Returns type annotated aioboto3 Chatbot client
    chatbot_client = session.chatbot.client()
    chatbot_client: types_aiobotocore_chatbot.client.ChatbotClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_chatbot.client import ChatbotClient

from boto34.aioboto3.service_factory import ServiceFactory


class ChatbotService(ServiceFactory[ChatbotClient]):
    SERVICE_NAME = "chatbot"
    _SERVICE_PROP = "chatbot"
