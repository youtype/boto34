"""
Wrapper for aiobotocore ChimeSDKMeetings service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_chime_sdk_meetings/)

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
    # Returns type annotated aiobotocore ChimeSDKMeetings client
    async with session.chime_sdk_meetings.create_client() as chime_sdk_meetings_client:
        chime_sdk_meetings_client: types_aiobotocore_chime_sdk_meetings.client.ChimeSDKMeetingsClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_chime_sdk_meetings.client import ChimeSDKMeetingsClient

from boto34.aiobotocore.service_factory import ServiceFactory


class ChimeSDKMeetingsService(ServiceFactory[ChimeSDKMeetingsClient]):
    SERVICE_NAME = "chime-sdk-meetings"
    _SERVICE_PROP = "chime_sdk_meetings"
