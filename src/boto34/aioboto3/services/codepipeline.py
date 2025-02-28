"""
Wrapper for aioboto3 CodePipeline service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_codepipeline/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_codepipeline.client import CodePipelineClient

from boto34.aioboto3.service_factory import ServiceFactory


class CodePipelineService(ServiceFactory[CodePipelineClient]):
    """
    CodePipeline service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_codepipeline/)
    """
