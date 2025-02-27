"""
Wrapper for aioboto3 Artifact service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_artifact/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aioboto3 import Session

    # Wrapper for aioboto3.Session constructor
    # Returns boto34.Session inherited from aioboto3.Session
    session = Session()
    session: boto34.aioboto3.session.Session

    # Type annotated aioboto3.Client
    # Uses the same arguments as aioboto3.client method
    # Returns type annotated aioboto3 Artifact client
    artifact_client = session.artifact.client()
    artifact_client: types_aiobotocore_artifact.client.ArtifactClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_artifact.client import ArtifactClient

from boto34.aioboto3.service_factory import ServiceFactory


class ArtifactService(ServiceFactory[ArtifactClient]):
    SERVICE_NAME = "artifact"
    _SERVICE_PROP = "artifact"
