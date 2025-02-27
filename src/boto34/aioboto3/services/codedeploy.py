"""
Wrapper for aioboto3 CodeDeploy service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_codedeploy/)

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
    # Returns type annotated aioboto3 CodeDeploy client
    codedeploy_client = session.codedeploy.client()
    codedeploy_client: types_aiobotocore_codedeploy.client.CodeDeployClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_codedeploy.client import CodeDeployClient

from boto34.aioboto3.service_factory import ServiceFactory


class CodeDeployService(ServiceFactory[CodeDeployClient]):
    SERVICE_NAME = "codedeploy"
    _SERVICE_PROP = "codedeploy"
