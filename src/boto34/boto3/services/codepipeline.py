"""
Wrapper for boto3 CodePipeline service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_codepipeline/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_codepipeline.client import CodePipelineClient

from boto34.boto3.service_factory import ServiceFactory


class CodePipelineService(ServiceFactory[CodePipelineClient]):
    """
    CodePipeline service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_codepipeline/)
    """
