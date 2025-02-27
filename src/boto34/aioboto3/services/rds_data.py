"""
Wrapper for aioboto3 RDSDataService service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_rds_data/)

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
    # Returns type annotated aioboto3 RDSDataService client
    rds_data_client = session.rds_data.client()
    rds_data_client: types_aiobotocore_rds_data.client.RDSDataServiceClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_rds_data.client import RDSDataServiceClient
except ImportError:
    RDSDataServiceClient = object  # type: ignore[misc,assignment]


class RDSDataServiceService(
    ServiceFactory[RDSDataServiceClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "rds-data"
    _SERVICE_PROP = "rds_data"
