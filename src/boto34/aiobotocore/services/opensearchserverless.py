"""
Wrapper for aiobotocore OpenSearchServiceServerless service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearchserverless/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_opensearchserverless.client import OpenSearchServiceServerlessClient

from boto34.aiobotocore.service_factory import ServiceFactory


class OpenSearchServiceServerlessService(ServiceFactory[OpenSearchServiceServerlessClient]):
    """
    OpenSearchServiceServerless service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opensearchserverless/)
    """
