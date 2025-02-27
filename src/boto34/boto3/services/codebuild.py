"""
Wrapper for boto3 CodeBuild service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_codebuild/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.boto3 import Session

    # Wrapper for boto3.Session constructor
    # Returns boto34.Session inherited from boto3.Session
    session = Session()
    session: boto34.boto3.session.Session

    # Type annotated boto3.Client
    # Uses the same arguments as boto3.client method
    # Returns type annotated boto3 CodeBuild client
    codebuild_client = session.codebuild.client()
    codebuild_client: types_boto3_codebuild.client.CodeBuildClient
    ```
"""

from __future__ import annotations

from types_boto3_codebuild.client import CodeBuildClient

from boto34.boto3.service_factory import ServiceFactory


class CodeBuildService(ServiceFactory[CodeBuildClient]):
    SERVICE_NAME = "codebuild"
    _SERVICE_PROP = "codebuild"
