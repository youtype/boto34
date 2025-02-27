"""
Wrapper for aiobotocore ResilienceHub service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_resiliencehub/)

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
    # Returns type annotated aiobotocore ResilienceHub client
    async with session.resiliencehub.create_client() as resiliencehub_client:
        resiliencehub_client: types_aiobotocore_resiliencehub.client.ResilienceHubClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_resiliencehub.client import ResilienceHubClient

from boto34.aiobotocore.service_factory import ServiceFactory


class ResilienceHubService(ServiceFactory[ResilienceHubClient]):
    SERVICE_NAME = "resiliencehub"
    _SERVICE_PROP = "resiliencehub"
