"""
Wrapper for aiobotocore Redshift service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_redshift/)

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
    # Returns type annotated aiobotocore Redshift client
    async with session.redshift.create_client() as redshift_client:
        redshift_client: types_aiobotocore_redshift.client.RedshiftClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_redshift.client import RedshiftClient

from boto34.aiobotocore.service_factory import ServiceFactory


class RedshiftService(ServiceFactory[RedshiftClient]):
    SERVICE_NAME = "redshift"
    _SERVICE_PROP = "redshift"
