"""
Wrapper for boto3 Artifact service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_artifact/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_artifact.client import ArtifactClient

from boto34.boto3.service_factory import ServiceFactory


class ArtifactService(ServiceFactory[ArtifactClient]):
    """
    Artifact service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_artifact/)
    """
