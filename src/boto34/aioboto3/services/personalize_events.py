"""
Wrapper for aioboto3 PersonalizeEvents service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_personalize_events/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_personalize_events.client import PersonalizeEventsClient

from boto34.aioboto3.service_factory import ServiceFactory


class PersonalizeEventsService(ServiceFactory[PersonalizeEventsClient]):
    """
    PersonalizeEvents service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_personalize_events/)
    """
