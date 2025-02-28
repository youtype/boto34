"""
Wrapper for aioboto3 MigrationHub service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_mgh/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_mgh.client import MigrationHubClient

from boto34.aioboto3.service_factory import ServiceFactory


class MigrationHubService(ServiceFactory[MigrationHubClient]):
    """
    MigrationHub service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_mgh/)
    """
