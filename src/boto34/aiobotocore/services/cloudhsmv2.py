"""
Wrapper for aiobotocore CloudHSMV2 service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudhsmv2/)

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
    # Returns type annotated aiobotocore CloudHSMV2 client
    async with session.cloudhsmv2.create_client() as cloudhsmv2_client:
        cloudhsmv2_client: types_aiobotocore_cloudhsmv2.client.CloudHSMV2Client
    ```
"""

from __future__ import annotations

from types_aiobotocore_cloudhsmv2.client import CloudHSMV2Client

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_cloudhsmv2.client import CloudHSMV2Client
except ImportError:
    CloudHSMV2Client = object  # type: ignore[misc,assignment]


class CloudHSMV2Service(
    ServiceFactory[CloudHSMV2Client]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "cloudhsmv2"
    _SERVICE_PROP = "cloudhsmv2"
