"""
Wrapper for aiobotocore CodeBuild service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codebuild/)

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
    # Returns type annotated aiobotocore CodeBuild client
    async with session.codebuild.create_client() as codebuild_client:
        codebuild_client: types_aiobotocore_codebuild.client.CodeBuildClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_codebuild.client import CodeBuildClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_codebuild.client import CodeBuildClient
except ImportError:
    CodeBuildClient = object  # type: ignore[misc,assignment]


class CodeBuildService(
    ServiceFactory[CodeBuildClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "codebuild"
    _SERVICE_PROP = "codebuild"
