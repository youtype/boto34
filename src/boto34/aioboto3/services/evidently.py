"""
Wrapper for aioboto3 CloudWatchEvidently service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_evidently/)

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
    # Returns type annotated aioboto3 CloudWatchEvidently client
    evidently_client = session.evidently.client()
    evidently_client: types_aiobotocore_evidently.client.CloudWatchEvidentlyClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_evidently.client import CloudWatchEvidentlyClient

from boto34.aioboto3.service_factory import ServiceFactory


class CloudWatchEvidentlyService(ServiceFactory[CloudWatchEvidentlyClient]):
    SERVICE_NAME = "evidently"
    _SERVICE_PROP = "evidently"
