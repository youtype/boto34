"""
Wrapper for boto3 CodePipeline service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_codepipeline/)

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
    # Returns type annotated boto3 CodePipeline client
    codepipeline_client = session.codepipeline.client()
    codepipeline_client: types_boto3_codepipeline.client.CodePipelineClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_codepipeline.client import CodePipelineClient
except ImportError:
    CodePipelineClient = object  # type: ignore[misc,assignment]


class CodePipelineService(
    ServiceFactory[CodePipelineClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "codepipeline"
    _SERVICE_PROP = "codepipeline"
