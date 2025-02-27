"""
Wrapper for aioboto3 CloudHSM service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_cloudhsm/)

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
    # Returns type annotated aioboto3 CloudHSM client
    cloudhsm_client = session.cloudhsm.client()
    cloudhsm_client: types_aiobotocore_cloudhsm.client.CloudHSMClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_cloudhsm.client import CloudHSMClient
except ImportError:
    CloudHSMClient = object  # type: ignore[misc,assignment]


class CloudHSMService(
    ServiceFactory[CloudHSMClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "cloudhsm"
    _SERVICE_PROP = "cloudhsm"
