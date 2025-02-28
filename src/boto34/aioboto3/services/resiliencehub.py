"""
Wrapper for aioboto3 ResilienceHub service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_resiliencehub/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_resiliencehub.client import ResilienceHubClient

from boto34.aioboto3.service_factory import ServiceFactory


class ResilienceHubService(ServiceFactory[ResilienceHubClient]):
    """
    ResilienceHub service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_resiliencehub/)
    """
