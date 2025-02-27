"""
Wrapper for aioboto3 RedshiftDataAPIService service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_redshift_data/)

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
    # Returns type annotated aioboto3 RedshiftDataAPIService client
    redshift_data_client = session.redshift_data.client()
    redshift_data_client: types_aiobotocore_redshift_data.client.RedshiftDataAPIServiceClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_redshift_data.client import RedshiftDataAPIServiceClient
except ImportError:
    RedshiftDataAPIServiceClient = object  # type: ignore[misc,assignment]


class RedshiftDataAPIServiceService(
    ServiceFactory[RedshiftDataAPIServiceClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "redshift-data"
    _SERVICE_PROP = "redshift_data"
