"""
Wrapper for aiobotocore RedshiftDataAPIService service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_redshift_data/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aiobotocore import get_session

    # Wrapper for aiobotocore.get_session function
    # Returns boto34.Session inherited from aiobotocore.Session
    session = get_session()
    session: boto34.aiobotocore.session.Session

    # Type annotated aiobotocore.AioBaseClient
    # Uses the same arguments as aiobotocore.create_client method
    # Returns type annotated aiobotocore RedshiftDataAPIService client
    async with session.redshift_data.create_client() as redshift_data_client:
        redshift_data_client: types_aiobotocore_redshift_data.client.RedshiftDataAPIServiceClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_redshift_data.client import RedshiftDataAPIServiceClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_redshift_data.client import RedshiftDataAPIServiceClient
except ImportError:
    RedshiftDataAPIServiceClient = object  # type: ignore[misc,assignment]


class RedshiftDataAPIServiceService(
    ServiceFactory[RedshiftDataAPIServiceClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "redshift-data"
    _SERVICE_PROP = "redshift_data"
