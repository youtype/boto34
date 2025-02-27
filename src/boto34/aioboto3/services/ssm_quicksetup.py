"""
Wrapper for aioboto3 SystemsManagerQuickSetup service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_ssm_quicksetup/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aioboto3 import Session

    # Wrapper for aioboto3.Session constructor
    # Returns boto34.Session inherited from aioboto3.Session
    session = Session()
    session: boto34.aioboto3.session.Session

    # Type annotated aioboto3.Client
    # Uses the same arguments as aioboto3.client method
    # Returns type annotated aioboto3 SystemsManagerQuickSetup client
    ssm_quicksetup_client = session.ssm_quicksetup.client()
    ssm_quicksetup_client: types_aiobotocore_ssm_quicksetup.client.SystemsManagerQuickSetupClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_ssm_quicksetup.client import SystemsManagerQuickSetupClient
except ImportError:
    SystemsManagerQuickSetupClient = object  # type: ignore[misc,assignment]


class SystemsManagerQuickSetupService(
    ServiceFactory[SystemsManagerQuickSetupClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "ssm-quicksetup"
    _SERVICE_PROP = "ssm_quicksetup"
