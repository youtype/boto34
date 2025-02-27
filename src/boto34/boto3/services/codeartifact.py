"""
Wrapper for boto3 CodeArtifact service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_codeartifact/)

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
    # Returns type annotated boto3 CodeArtifact client
    codeartifact_client = session.codeartifact.client()
    codeartifact_client: types_boto3_codeartifact.client.CodeArtifactClient
    ```
"""

from __future__ import annotations

from types_boto3_codeartifact.client import CodeArtifactClient

from boto34.boto3.service_factory import ServiceFactory


class CodeArtifactService(ServiceFactory[CodeArtifactClient]):
    SERVICE_NAME = "codeartifact"
    _SERVICE_PROP = "codeartifact"
