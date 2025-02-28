"""
Wrapper for aioboto3 CodeBuild service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_codebuild/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_codebuild.client import CodeBuildClient

from boto34.aioboto3.service_factory import ServiceFactory


class CodeBuildService(ServiceFactory[CodeBuildClient]):
    """
    CodeBuild service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_codebuild/)
    """
