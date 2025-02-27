"""
Wrapper for aiobotocore SWF service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_swf/)

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
    # Returns type annotated aiobotocore SWF client
    async with session.swf.create_client() as swf_client:
        swf_client: types_aiobotocore_swf.client.SWFClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_swf.client import SWFClient

from boto34.aiobotocore.service_factory import ServiceFactory


class SWFService(ServiceFactory[SWFClient]):
    SERVICE_NAME = "swf"
    _SERVICE_PROP = "swf"
