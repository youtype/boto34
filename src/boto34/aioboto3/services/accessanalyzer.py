"""
Wrapper for aioboto3 AccessAnalyzer service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_accessanalyzer/)

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
    # Returns type annotated aioboto3 AccessAnalyzer client
    accessanalyzer_client = session.accessanalyzer.client()
    accessanalyzer_client: types_aiobotocore_accessanalyzer.client.AccessAnalyzerClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_accessanalyzer.client import AccessAnalyzerClient

from boto34.aioboto3.service_factory import ServiceFactory


class AccessAnalyzerService(ServiceFactory[AccessAnalyzerClient]):
    SERVICE_NAME = "accessanalyzer"
    _SERVICE_PROP = "accessanalyzer"
