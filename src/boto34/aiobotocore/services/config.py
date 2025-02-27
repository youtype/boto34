"""
Wrapper for aiobotocore ConfigService service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_config/)

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
    # Returns type annotated aiobotocore ConfigService client
    async with session.config.create_client() as config_client:
        config_client: types_aiobotocore_config.client.ConfigServiceClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_config.client import ConfigServiceClient

from boto34.aiobotocore.service_factory import ServiceFactory


class ConfigServiceService(ServiceFactory[ConfigServiceClient]):
    SERVICE_NAME = "config"
    _SERVICE_PROP = "config"
