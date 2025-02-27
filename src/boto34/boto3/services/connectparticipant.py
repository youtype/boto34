"""
Wrapper for boto3 ConnectParticipant service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_connectparticipant/)

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
    # Returns type annotated boto3 ConnectParticipant client
    connectparticipant_client = session.connectparticipant.client()
    connectparticipant_client: types_boto3_connectparticipant.client.ConnectParticipantClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_connectparticipant.client import ConnectParticipantClient
except ImportError:
    ConnectParticipantClient = object  # type: ignore[misc,assignment]


class ConnectParticipantService(
    ServiceFactory[ConnectParticipantClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "connectparticipant"
    _SERVICE_PROP = "connectparticipant"
