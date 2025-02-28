"""
Wrapper for aioboto3 EndUserMessagingSocial service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_socialmessaging/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_socialmessaging.client import EndUserMessagingSocialClient

from boto34.aioboto3.service_factory import ServiceFactory


class EndUserMessagingSocialService(ServiceFactory[EndUserMessagingSocialClient]):
    """
    EndUserMessagingSocial service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_socialmessaging/)
    """
