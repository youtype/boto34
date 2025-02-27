"""
Wrapper for aiobotocore ConnectParticipant service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connectparticipant/)

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
    # Returns type annotated aiobotocore ConnectParticipant client
    async with session.connectparticipant.create_client() as connectparticipant_client:
        connectparticipant_client: types_aiobotocore_connectparticipant.client.ConnectParticipantClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_connectparticipant.client import ConnectParticipantClient

from boto34.aiobotocore.service_factory import ServiceFactory


class ConnectParticipantService(ServiceFactory[ConnectParticipantClient]):
    SERVICE_NAME = "connectparticipant"
    _SERVICE_PROP = "connectparticipant"
