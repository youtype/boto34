"""
Wrapper for aiobotocore CodeCommit service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codecommit/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aiobotocore import get_session

    # Wrapper for aiobotocore.get_session function
    # Returns boto34.Session inherited from aiobotocore.Session
    session = get_session()
    session: boto34.aiobotocore.session.Session

    # Type annotated aiobotocore.AioBaseClient
    # Uses the same arguments as aiobotocore.create_client method
    # Returns type annotated aiobotocore CodeCommit client
    async with session.codecommit.create_client() as codecommit_client:
        codecommit_client: types_aiobotocore_codecommit.client.CodeCommitClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_codecommit.client import CodeCommitClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_codecommit.client import CodeCommitClient
except ImportError:
    CodeCommitClient = object  # type: ignore[misc,assignment]


class CodeCommitService(
    ServiceFactory[CodeCommitClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "codecommit"
    _SERVICE_PROP = "codecommit"
