"""
Wrapper for aiobotocore SupportApp service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_support_app/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_support_app.client import SupportAppClient

from boto34.aiobotocore.service_factory import ServiceFactory


class SupportAppService(ServiceFactory[SupportAppClient]):
    """
    SupportApp service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_support_app/)
    """
