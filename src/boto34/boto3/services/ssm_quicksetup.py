"""
Wrapper for boto3 SystemsManagerQuickSetup service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_ssm_quicksetup/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.boto3 import Session

    # Wrapper for boto3.Session constructor
    # Returns boto34.Session inherited from boto3.Session
    session = Session()
    session: boto34.boto3.session.Session

    # Type annotated boto3.Client
    # Uses the same arguments as boto3.client method
    # Returns type annotated boto3 SystemsManagerQuickSetup client
    ssm_quicksetup_client = session.ssm_quicksetup.client()
    ssm_quicksetup_client: types_boto3_ssm_quicksetup.client.SystemsManagerQuickSetupClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_ssm_quicksetup.client import SystemsManagerQuickSetupClient
except ImportError:
    SystemsManagerQuickSetupClient = object  # type: ignore[misc,assignment]


class SystemsManagerQuickSetupService(
    ServiceFactory[SystemsManagerQuickSetupClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "ssm-quicksetup"
    _SERVICE_PROP = "ssm_quicksetup"
