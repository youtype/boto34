"""
Wrapper for aiobotocore MigrationHub service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mgh/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_mgh.client import MigrationHubClient

from boto34.aiobotocore.service_factory import ServiceFactory


class MigrationHubService(ServiceFactory[MigrationHubClient]):
    """
    MigrationHub service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_mgh/)
    """
