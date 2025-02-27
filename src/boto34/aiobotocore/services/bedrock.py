"""
Wrapper for aiobotocore Bedrock service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_bedrock/)

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
    # Returns type annotated aiobotocore Bedrock client
    async with session.bedrock.create_client() as bedrock_client:
        bedrock_client: types_aiobotocore_bedrock.client.BedrockClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_bedrock.client import BedrockClient

from boto34.aiobotocore.service_factory import ServiceFactory


class BedrockService(ServiceFactory[BedrockClient]):
    SERVICE_NAME = "bedrock"
    _SERVICE_PROP = "bedrock"
