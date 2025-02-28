"""
Wrapper for boto3 CodeBuild service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_codebuild/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_codebuild.client import CodeBuildClient

from boto34.boto3.service_factory import ServiceFactory


class CodeBuildService(ServiceFactory[CodeBuildClient]):
    """
    CodeBuild service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_codebuild/)
    """
