"""
Wrapper for boto3 PersonalizeEvents service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_personalize_events/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_personalize_events.client import PersonalizeEventsClient

from boto34.boto3.service_factory import ServiceFactory


class PersonalizeEventsService(ServiceFactory[PersonalizeEventsClient]):
    """
    PersonalizeEvents service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_personalize_events/)
    """
