"""
Wrapper for aioboto3 Artifact service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_artifact/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_artifact.client import ArtifactClient

from boto34.aioboto3.service_factory import ServiceFactory


class ArtifactService(ServiceFactory[ArtifactClient]):
    """
    Artifact service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_artifact/)
    """
