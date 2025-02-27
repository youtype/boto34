"""
Wrapper for aioboto3 TelcoNetworkBuilder service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_tnb/)

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
    # Returns type annotated aioboto3 TelcoNetworkBuilder client
    tnb_client = session.tnb.client()
    tnb_client: types_aiobotocore_tnb.client.TelcoNetworkBuilderClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_tnb.client import TelcoNetworkBuilderClient

from boto34.aioboto3.service_factory import ServiceFactory


class TelcoNetworkBuilderService(ServiceFactory[TelcoNetworkBuilderClient]):
    SERVICE_NAME = "tnb"
    _SERVICE_PROP = "tnb"
