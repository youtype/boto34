"""
Wrapper for boto3 RDS service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_rds/)

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
    # Returns type annotated boto3 RDS client
    rds_client = session.rds.client()
    rds_client: types_boto3_rds.client.RDSClient
    ```
"""

from __future__ import annotations

from types_boto3_rds.client import RDSClient

from boto34.boto3.service_factory import ServiceFactory


class RDSService(ServiceFactory[RDSClient]):
    SERVICE_NAME = "rds"
    _SERVICE_PROP = "rds"
