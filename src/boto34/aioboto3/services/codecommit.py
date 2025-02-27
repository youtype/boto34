"""
Wrapper for aioboto3 CodeCommit service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_codecommit/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aioboto3 import Session

    # Wrapper for aioboto3.Session constructor
    # Returns boto34.Session inherited from aioboto3.Session
    session = Session()
    session: boto34.aioboto3.session.Session

    # Type annotated aioboto3.Client
    # Uses the same arguments as aioboto3.client method
    # Returns type annotated aioboto3 CodeCommit client
    codecommit_client = session.codecommit.client()
    codecommit_client: types_aiobotocore_codecommit.client.CodeCommitClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_codecommit.client import CodeCommitClient
except ImportError:
    CodeCommitClient = object  # type: ignore[misc,assignment]


class CodeCommitService(
    ServiceFactory[CodeCommitClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "codecommit"
    _SERVICE_PROP = "codecommit"
