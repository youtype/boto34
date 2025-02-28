"""
Wrapper for aioboto3 MailManager service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_mailmanager/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_mailmanager.client import MailManagerClient

from boto34.aioboto3.service_factory import ServiceFactory


class MailManagerService(ServiceFactory[MailManagerClient]):
    """
    MailManager service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_mailmanager/)
    """
