"""
Wrapper for aiobotocore CodeDeploy service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codedeploy/)

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
    # Returns type annotated aiobotocore CodeDeploy client
    async with session.codedeploy.create_client() as codedeploy_client:
        codedeploy_client: types_aiobotocore_codedeploy.client.CodeDeployClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_codedeploy.client import CodeDeployClient

from boto34.aiobotocore.service_factory import ServiceFactory


class CodeDeployService(ServiceFactory[CodeDeployClient]):
    SERVICE_NAME = "codedeploy"
    _SERVICE_PROP = "codedeploy"
