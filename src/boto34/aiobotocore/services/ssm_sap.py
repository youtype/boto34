"""
Wrapper for aiobotocore SsmSap service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ssm_sap/)

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
    # Returns type annotated aiobotocore SsmSap client
    async with session.ssm_sap.create_client() as ssm_sap_client:
        ssm_sap_client: types_aiobotocore_ssm_sap.client.SsmSapClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_ssm_sap.client import SsmSapClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_ssm_sap.client import SsmSapClient
except ImportError:
    SsmSapClient = object  # type: ignore[misc,assignment]


class SsmSapService(
    ServiceFactory[SsmSapClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "ssm-sap"
    _SERVICE_PROP = "ssm_sap"
