"""
Wrapper for aiobotocore Ivschat service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ivschat/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_ivschat.client import IvschatClient

from boto34.aiobotocore.service_factory import ServiceFactory


class IvschatService(ServiceFactory[IvschatClient]):
    """
    Ivschat service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ivschat/)
    """
