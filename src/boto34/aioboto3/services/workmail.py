"""
Wrapper for aioboto3 WorkMail service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_workmail/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_workmail.client import WorkMailClient

from boto34.aioboto3.service_factory import ServiceFactory


class WorkMailService(ServiceFactory[WorkMailClient]):
    """
    WorkMail service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_workmail/)
    """
