"""
Wrapper for aiobotocore CodePipeline service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codepipeline/)

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
    # Returns type annotated aiobotocore CodePipeline client
    async with session.codepipeline.create_client() as codepipeline_client:
        codepipeline_client: types_aiobotocore_codepipeline.client.CodePipelineClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_codepipeline.client import CodePipelineClient

from boto34.aiobotocore.service_factory import ServiceFactory


class CodePipelineService(ServiceFactory[CodePipelineClient]):
    SERVICE_NAME = "codepipeline"
    _SERVICE_PROP = "codepipeline"
