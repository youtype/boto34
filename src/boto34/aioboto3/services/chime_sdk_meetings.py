"""
Wrapper for aioboto3 ChimeSDKMeetings service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_chime_sdk_meetings/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_chime_sdk_meetings.client import ChimeSDKMeetingsClient

from boto34.aioboto3.service_factory import ServiceFactory


class ChimeSDKMeetingsService(ServiceFactory[ChimeSDKMeetingsClient]):
    """
    ChimeSDKMeetings service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_chime_sdk_meetings/)
    """
