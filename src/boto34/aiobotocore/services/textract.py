"""
Wrapper for aiobotocore Textract service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_textract/)

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
    # Returns type annotated aiobotocore Textract client
    async with session.textract.create_client() as textract_client:
        textract_client: types_aiobotocore_textract.client.TextractClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_textract.client import TextractClient

from boto34.aiobotocore.service_factory import ServiceFactory


class TextractService(ServiceFactory[TextractClient]):
    SERVICE_NAME = "textract"
    _SERVICE_PROP = "textract"
