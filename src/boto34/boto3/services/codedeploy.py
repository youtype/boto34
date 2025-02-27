"""
Wrapper for boto3 CodeDeploy service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_codedeploy/)

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
    # Returns type annotated boto3 CodeDeploy client
    codedeploy_client = session.codedeploy.client()
    codedeploy_client: types_boto3_codedeploy.client.CodeDeployClient
    ```
"""

from __future__ import annotations

from types_boto3_codedeploy.client import CodeDeployClient

from boto34.boto3.service_factory import ServiceFactory


class CodeDeployService(ServiceFactory[CodeDeployClient]):
    SERVICE_NAME = "codedeploy"
    _SERVICE_PROP = "codedeploy"
