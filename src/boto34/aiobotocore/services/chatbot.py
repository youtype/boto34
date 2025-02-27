"""
Wrapper for aiobotocore Chatbot service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_chatbot/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aiobotocore import get_session

    # Wrapper for aiobotocore.get_session function
    # Returns boto34.Session inherited from aiobotocore.Session
    session = get_session()
    session: boto34.aiobotocore.session.Session

    # Type annotated aiobotocore.AioBaseClient
    # Uses the same arguments as aiobotocore.create_client method
    # Returns type annotated aiobotocore Chatbot client
    async with session.chatbot.create_client() as chatbot_client:
        chatbot_client: types_aiobotocore_chatbot.client.ChatbotClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_chatbot.client import ChatbotClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_chatbot.client import ChatbotClient
except ImportError:
    ChatbotClient = object  # type: ignore[misc,assignment]


class ChatbotService(
    ServiceFactory[ChatbotClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "chatbot"
    _SERVICE_PROP = "chatbot"
