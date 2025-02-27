"""
Wrapper for aioboto3 CodePipeline service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_codepipeline/)

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
    # Returns type annotated aioboto3 CodePipeline client
    codepipeline_client = session.codepipeline.client()
    codepipeline_client: types_aiobotocore_codepipeline.client.CodePipelineClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_codepipeline.client import CodePipelineClient

from boto34.aioboto3.service_factory import ServiceFactory


class CodePipelineService(ServiceFactory[CodePipelineClient]):
    SERVICE_NAME = "codepipeline"
    _SERVICE_PROP = "codepipeline"
