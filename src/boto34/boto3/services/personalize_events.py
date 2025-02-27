"""
Wrapper for boto3 PersonalizeEvents service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_personalize_events/)

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
    # Returns type annotated boto3 PersonalizeEvents client
    personalize_events_client = session.personalize_events.client()
    personalize_events_client: types_boto3_personalize_events.client.PersonalizeEventsClient
    ```
"""

from __future__ import annotations

from types_boto3_personalize_events.client import PersonalizeEventsClient

from boto34.boto3.service_factory import ServiceFactory


class PersonalizeEventsService(ServiceFactory[PersonalizeEventsClient]):
    SERVICE_NAME = "personalize-events"
    _SERVICE_PROP = "personalize_events"
