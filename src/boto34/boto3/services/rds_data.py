"""
Wrapper for boto3 RDSDataService service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_rds_data/)

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
    # Returns type annotated boto3 RDSDataService client
    rds_data_client = session.rds_data.client()
    rds_data_client: types_boto3_rds_data.client.RDSDataServiceClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_rds_data.client import RDSDataServiceClient
except ImportError:
    RDSDataServiceClient = object  # type: ignore[misc,assignment]


class RDSDataServiceService(
    ServiceFactory[RDSDataServiceClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "rds-data"
    _SERVICE_PROP = "rds_data"
