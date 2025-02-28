"""
Wrapper for aioboto3 Amplify service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_amplify/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_amplify.client import AmplifyClient

from boto34.aioboto3.service_factory import ServiceFactory


class AmplifyService(ServiceFactory[AmplifyClient]):
    """
    Amplify service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_amplify/)
    """
