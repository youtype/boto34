"""
Wrapper for boto3 EMRServerless service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_emr_serverless/)

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
    # Returns type annotated boto3 EMRServerless client
    emr_serverless_client = session.emr_serverless.client()
    emr_serverless_client: types_boto3_emr_serverless.client.EMRServerlessClient
    ```
"""

from __future__ import annotations

from types_boto3_emr_serverless.client import EMRServerlessClient

from boto34.boto3.service_factory import ServiceFactory


class EMRServerlessService(ServiceFactory[EMRServerlessClient]):
    SERVICE_NAME = "emr-serverless"
    _SERVICE_PROP = "emr_serverless"
