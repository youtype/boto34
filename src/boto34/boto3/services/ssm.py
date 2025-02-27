"""
Wrapper for boto3 SSM service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_ssm/)

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
    # Returns type annotated boto3 SSM client
    ssm_client = session.ssm.client()
    ssm_client: types_boto3_ssm.client.SSMClient
    ```
"""

from __future__ import annotations

from types_boto3_ssm.client import SSMClient

from boto34.boto3.service_factory import ServiceFactory


class SSMService(ServiceFactory[SSMClient]):
    SERVICE_NAME = "ssm"
    _SERVICE_PROP = "ssm"
