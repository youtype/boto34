"""
Wrapper for aioboto3 SWF service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_swf/)

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
    # Returns type annotated aioboto3 SWF client
    swf_client = session.swf.client()
    swf_client: types_aiobotocore_swf.client.SWFClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_swf.client import SWFClient

from boto34.aioboto3.service_factory import ServiceFactory


class SWFService(ServiceFactory[SWFClient]):
    SERVICE_NAME = "swf"
    _SERVICE_PROP = "swf"
