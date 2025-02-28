"""
Wrapper for boto3 EndUserMessagingSocial service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_socialmessaging/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_socialmessaging.client import EndUserMessagingSocialClient

from boto34.boto3.service_factory import ServiceFactory


class EndUserMessagingSocialService(ServiceFactory[EndUserMessagingSocialClient]):
    """
    EndUserMessagingSocial service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_socialmessaging/)
    """
