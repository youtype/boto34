"""
Wrapper for boto3 CodeArtifact service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_codeartifact/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_codeartifact.client import CodeArtifactClient

from boto34.boto3.service_factory import ServiceFactory


class CodeArtifactService(ServiceFactory[CodeArtifactClient]):
    """
    CodeArtifact service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_codeartifact/)
    """
