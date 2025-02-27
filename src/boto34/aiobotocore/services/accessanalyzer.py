"""
Wrapper for aiobotocore AccessAnalyzer service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_accessanalyzer/)

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
    # Returns type annotated aiobotocore AccessAnalyzer client
    async with session.accessanalyzer.create_client() as accessanalyzer_client:
        accessanalyzer_client: types_aiobotocore_accessanalyzer.client.AccessAnalyzerClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_accessanalyzer.client import AccessAnalyzerClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_accessanalyzer.client import AccessAnalyzerClient
except ImportError:
    AccessAnalyzerClient = object  # type: ignore[misc,assignment]


class AccessAnalyzerService(
    ServiceFactory[AccessAnalyzerClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "accessanalyzer"
    _SERVICE_PROP = "accessanalyzer"
