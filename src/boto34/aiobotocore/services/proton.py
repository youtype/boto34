"""
Wrapper for aiobotocore Proton service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/)

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
    # Returns type annotated aiobotocore Proton client
    async with session.proton.create_client() as proton_client:
        proton_client: types_aiobotocore_proton.client.ProtonClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_proton.client import ProtonClient

from boto34.aiobotocore.service_factory import ServiceFactory


class ProtonService(ServiceFactory[ProtonClient]):
    SERVICE_NAME = "proton"
    _SERVICE_PROP = "proton"
