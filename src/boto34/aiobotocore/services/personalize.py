"""
Wrapper for aiobotocore Personalize service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_personalize/)

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
    # Returns type annotated aiobotocore Personalize client
    async with session.personalize.create_client() as personalize_client:
        personalize_client: types_aiobotocore_personalize.client.PersonalizeClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_personalize.client import PersonalizeClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_personalize.client import PersonalizeClient
except ImportError:
    PersonalizeClient = object  # type: ignore[misc,assignment]


class PersonalizeService(
    ServiceFactory[PersonalizeClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "personalize"
    _SERVICE_PROP = "personalize"
