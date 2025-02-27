"""
Wrapper for aiobotocore RedshiftServerless service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_redshift_serverless/)

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
    # Returns type annotated aiobotocore RedshiftServerless client
    async with session.redshift_serverless.create_client() as redshift_serverless_client:
        redshift_serverless_client: (
            types_aiobotocore_redshift_serverless.client.RedshiftServerlessClient
        )
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_redshift_serverless.client import RedshiftServerlessClient
except ImportError:
    RedshiftServerlessClient = object  # type: ignore[misc,assignment]


class RedshiftServerlessService(
    ServiceFactory[RedshiftServerlessClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "redshift-serverless"
    _SERVICE_PROP = "redshift_serverless"
