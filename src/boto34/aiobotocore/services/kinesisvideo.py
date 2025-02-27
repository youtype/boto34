"""
Wrapper for aiobotocore KinesisVideo service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kinesisvideo/)

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
    # Returns type annotated aiobotocore KinesisVideo client
    async with session.kinesisvideo.create_client() as kinesisvideo_client:
        kinesisvideo_client: types_aiobotocore_kinesisvideo.client.KinesisVideoClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_kinesisvideo.client import KinesisVideoClient

from boto34.aiobotocore.service_factory import ServiceFactory


class KinesisVideoService(ServiceFactory[KinesisVideoClient]):
    SERVICE_NAME = "kinesisvideo"
    _SERVICE_PROP = "kinesisvideo"
