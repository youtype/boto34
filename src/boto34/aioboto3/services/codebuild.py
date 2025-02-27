"""
Wrapper for aioboto3 CodeBuild service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_codebuild/)

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
    # Returns type annotated aioboto3 CodeBuild client
    codebuild_client = session.codebuild.client()
    codebuild_client: types_aiobotocore_codebuild.client.CodeBuildClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_codebuild.client import CodeBuildClient
except ImportError:
    CodeBuildClient = object  # type: ignore[misc,assignment]


class CodeBuildService(
    ServiceFactory[CodeBuildClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "codebuild"
    _SERVICE_PROP = "codebuild"
