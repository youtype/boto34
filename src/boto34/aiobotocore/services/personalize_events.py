"""
Wrapper for aiobotocore PersonalizeEvents service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_personalize_events/)

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
    # Returns type annotated aiobotocore PersonalizeEvents client
    async with session.personalize_events.create_client() as personalize_events_client:
        personalize_events_client: types_aiobotocore_personalize_events.client.PersonalizeEventsClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_personalize_events.client import PersonalizeEventsClient

from boto34.aiobotocore.service_factory import ServiceFactory


class PersonalizeEventsService(ServiceFactory[PersonalizeEventsClient]):
    SERVICE_NAME = "personalize-events"
    _SERVICE_PROP = "personalize_events"
