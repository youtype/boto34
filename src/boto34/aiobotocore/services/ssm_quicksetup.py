"""
Wrapper for aiobotocore SystemsManagerQuickSetup service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ssm_quicksetup/)

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
    # Returns type annotated aiobotocore SystemsManagerQuickSetup client
    async with session.ssm_quicksetup.create_client() as ssm_quicksetup_client:
        ssm_quicksetup_client: types_aiobotocore_ssm_quicksetup.client.SystemsManagerQuickSetupClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_ssm_quicksetup.client import SystemsManagerQuickSetupClient
except ImportError:
    SystemsManagerQuickSetupClient = object  # type: ignore[misc,assignment]


class SystemsManagerQuickSetupService(
    ServiceFactory[SystemsManagerQuickSetupClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "ssm-quicksetup"
    _SERVICE_PROP = "ssm_quicksetup"
