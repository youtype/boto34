"""
Wrapper for aioboto3 ChimeSDKMeetings service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_chime_sdk_meetings/)

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
    # Returns type annotated aioboto3 ChimeSDKMeetings client
    chime_sdk_meetings_client = session.chime_sdk_meetings.client()
    chime_sdk_meetings_client: types_aiobotocore_chime_sdk_meetings.client.ChimeSDKMeetingsClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_chime_sdk_meetings.client import ChimeSDKMeetingsClient
except ImportError:
    ChimeSDKMeetingsClient = object  # type: ignore[misc,assignment]


class ChimeSDKMeetingsService(
    ServiceFactory[ChimeSDKMeetingsClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "chime-sdk-meetings"
    _SERVICE_PROP = "chime_sdk_meetings"
