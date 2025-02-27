"""
Wrapper for aiobotocore Artifact service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_artifact/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aiobotocore import get_session

    # Wrapper for aiobotocore.get_session function
    # Returns boto34.Session inherited from aiobotocore.Session
    session = get_session()
    session: boto34.aiobotocore.session.Session

    # Type annotated aiobotocore.AioBaseClient
    # Uses the same arguments as aiobotocore.create_client method
    # Returns type annotated aiobotocore Artifact client
    async with session.artifact.create_client() as artifact_client:
        artifact_client: types_aiobotocore_artifact.client.ArtifactClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_artifact.client import ArtifactClient

from boto34.aiobotocore.service_factory import ServiceFactory


class ArtifactService(ServiceFactory[ArtifactClient]):
    SERVICE_NAME = "artifact"
    _SERVICE_PROP = "artifact"
