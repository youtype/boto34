"""
Wrapper for aioboto3 ConfigService service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_config/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_config.client import ConfigServiceClient

from boto34.aioboto3.service_factory import ServiceFactory


class ConfigServiceService(ServiceFactory[ConfigServiceClient]):
    """
    ConfigService service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_config/)
    """
