"""
Wrapper for aioboto3 ConnectParticipant service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_connectparticipant/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_connectparticipant.client import ConnectParticipantClient

from boto34.aioboto3.service_factory import ServiceFactory


class ConnectParticipantService(ServiceFactory[ConnectParticipantClient]):
    """
    ConnectParticipant service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_connectparticipant/)
    """
