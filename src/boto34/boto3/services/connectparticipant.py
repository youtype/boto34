"""
Wrapper for boto3 ConnectParticipant service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_connectparticipant/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_connectparticipant.client import ConnectParticipantClient

from boto34.boto3.service_factory import ServiceFactory


class ConnectParticipantService(ServiceFactory[ConnectParticipantClient]):
    """
    ConnectParticipant service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_connectparticipant/)
    """
