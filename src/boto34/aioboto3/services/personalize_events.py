"""
Wrapper for aioboto3 PersonalizeEvents service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_personalize_events/)

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
    # Returns type annotated aioboto3 PersonalizeEvents client
    personalize_events_client = session.personalize_events.client()
    personalize_events_client: types_aiobotocore_personalize_events.client.PersonalizeEventsClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_personalize_events.client import PersonalizeEventsClient
except ImportError:
    PersonalizeEventsClient = object  # type: ignore[misc,assignment]


class PersonalizeEventsService(
    ServiceFactory[PersonalizeEventsClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "personalize-events"
    _SERVICE_PROP = "personalize_events"
