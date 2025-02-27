"""
Wrapper for boto3 RedshiftServerless service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_redshift_serverless/)

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
    # Returns type annotated boto3 RedshiftServerless client
    redshift_serverless_client = session.redshift_serverless.client()
    redshift_serverless_client: types_boto3_redshift_serverless.client.RedshiftServerlessClient
    ```
"""

from __future__ import annotations

from types_boto3_redshift_serverless.client import RedshiftServerlessClient

from boto34.boto3.service_factory import ServiceFactory


class RedshiftServerlessService(ServiceFactory[RedshiftServerlessClient]):
    SERVICE_NAME = "redshift-serverless"
    _SERVICE_PROP = "redshift_serverless"
