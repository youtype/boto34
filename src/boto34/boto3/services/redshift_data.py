"""
Wrapper for boto3 RedshiftDataAPIService service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_redshift_data/)

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
    # Returns type annotated boto3 RedshiftDataAPIService client
    redshift_data_client = session.redshift_data.client()
    redshift_data_client: types_boto3_redshift_data.client.RedshiftDataAPIServiceClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_redshift_data.client import RedshiftDataAPIServiceClient
except ImportError:
    RedshiftDataAPIServiceClient = object  # type: ignore[misc,assignment]


class RedshiftDataAPIServiceService(
    ServiceFactory[RedshiftDataAPIServiceClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "redshift-data"
    _SERVICE_PROP = "redshift_data"
