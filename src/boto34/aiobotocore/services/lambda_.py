"""
Wrapper for aiobotocore Lambda service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lambda/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_lambda.client import LambdaClient

from boto34.aiobotocore.service_factory import ServiceFactory


class LambdaService(ServiceFactory[LambdaClient]):
    """
    Lambda service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lambda/)
    """
