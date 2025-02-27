"""
Wrapper for aiobotocore OpsWorksCM service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_opsworkscm/)

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
    # Returns type annotated aiobotocore OpsWorksCM client
    async with session.opsworkscm.create_client() as opsworkscm_client:
        opsworkscm_client: types_aiobotocore_opsworkscm.client.OpsWorksCMClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_opsworkscm.client import OpsWorksCMClient

from boto34.aiobotocore.service_factory import ServiceFactory


class OpsWorksCMService(ServiceFactory[OpsWorksCMClient]):
    SERVICE_NAME = "opsworkscm"
    _SERVICE_PROP = "opsworkscm"
