"""
Wrapper for boto3 Artifact service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_artifact/)

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
    # Returns type annotated boto3 Artifact client
    artifact_client = session.artifact.client()
    artifact_client: types_boto3_artifact.client.ArtifactClient
    ```
"""

from __future__ import annotations

from types_boto3_artifact.client import ArtifactClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_artifact.client import ArtifactClient
except ImportError:
    ArtifactClient = object  # type: ignore[misc,assignment]


class ArtifactService(
    ServiceFactory[ArtifactClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "artifact"
    _SERVICE_PROP = "artifact"
