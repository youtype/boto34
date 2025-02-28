"""
Wrapper for aioboto3 SES service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_ses/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_ses.client import SESClient

from boto34.aioboto3.service_factory import ServiceFactory


class SESService(ServiceFactory[SESClient]):
    """
    SES service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_ses/)
    """
