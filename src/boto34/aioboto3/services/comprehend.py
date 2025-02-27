"""
Wrapper for aioboto3 Comprehend service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_comprehend/)

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
    # Returns type annotated aioboto3 Comprehend client
    comprehend_client = session.comprehend.client()
    comprehend_client: types_aiobotocore_comprehend.client.ComprehendClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_comprehend.client import ComprehendClient

from boto34.aioboto3.service_factory import ServiceFactory


class ComprehendService(ServiceFactory[ComprehendClient]):
    SERVICE_NAME = "comprehend"
    _SERVICE_PROP = "comprehend"
