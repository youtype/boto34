"""
Wrapper for aiobotocore AmplifyUIBuilder service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amplifyuibuilder/)

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
    # Returns type annotated aiobotocore AmplifyUIBuilder client
    async with session.amplifyuibuilder.create_client() as amplifyuibuilder_client:
        amplifyuibuilder_client: types_aiobotocore_amplifyuibuilder.client.AmplifyUIBuilderClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_amplifyuibuilder.client import AmplifyUIBuilderClient

from boto34.aiobotocore.service_factory import ServiceFactory


class AmplifyUIBuilderService(ServiceFactory[AmplifyUIBuilderClient]):
    SERVICE_NAME = "amplifyuibuilder"
    _SERVICE_PROP = "amplifyuibuilder"
