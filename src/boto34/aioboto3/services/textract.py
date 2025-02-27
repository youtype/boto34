"""
Wrapper for aioboto3 Textract service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_textract/)

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
    # Returns type annotated aioboto3 Textract client
    textract_client = session.textract.client()
    textract_client: types_aiobotocore_textract.client.TextractClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_textract.client import TextractClient

from boto34.aioboto3.service_factory import ServiceFactory


class TextractService(ServiceFactory[TextractClient]):
    SERVICE_NAME = "textract"
    _SERVICE_PROP = "textract"
