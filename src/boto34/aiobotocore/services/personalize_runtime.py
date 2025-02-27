"""
Wrapper for aiobotocore PersonalizeRuntime service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_personalize_runtime/)

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
    # Returns type annotated aiobotocore PersonalizeRuntime client
    async with session.personalize_runtime.create_client() as personalize_runtime_client:
        personalize_runtime_client: (
            types_aiobotocore_personalize_runtime.client.PersonalizeRuntimeClient
        )
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_personalize_runtime.client import PersonalizeRuntimeClient
except ImportError:
    PersonalizeRuntimeClient = object  # type: ignore[misc,assignment]


class PersonalizeRuntimeService(
    ServiceFactory[PersonalizeRuntimeClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "personalize-runtime"
    _SERVICE_PROP = "personalize_runtime"
