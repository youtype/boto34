"""
Wrapper for aiobotocore SES service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ses/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_ses.client import SESClient

from boto34.aiobotocore.service_factory import ServiceFactory


class SESService(ServiceFactory[SESClient]):
    """
    SES service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ses/)
    """
