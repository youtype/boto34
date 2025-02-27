"""
Wrapper for boto3 ChimeSDKMeetings service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_chime_sdk_meetings/)

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
    # Returns type annotated boto3 ChimeSDKMeetings client
    chime_sdk_meetings_client = session.chime_sdk_meetings.client()
    chime_sdk_meetings_client: types_boto3_chime_sdk_meetings.client.ChimeSDKMeetingsClient
    ```
"""

from __future__ import annotations

from types_boto3_chime_sdk_meetings.client import ChimeSDKMeetingsClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_chime_sdk_meetings.client import ChimeSDKMeetingsClient
except ImportError:
    ChimeSDKMeetingsClient = object  # type: ignore[misc,assignment]


class ChimeSDKMeetingsService(
    ServiceFactory[ChimeSDKMeetingsClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "chime-sdk-meetings"
    _SERVICE_PROP = "chime_sdk_meetings"
