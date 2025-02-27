"""
Wrapper for aioboto3 Redshift service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_redshift/)

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
    # Returns type annotated aioboto3 Redshift client
    redshift_client = session.redshift.client()
    redshift_client: types_aiobotocore_redshift.client.RedshiftClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_redshift.client import RedshiftClient

from boto34.aioboto3.service_factory import ServiceFactory


class RedshiftService(ServiceFactory[RedshiftClient]):
    SERVICE_NAME = "redshift"
    _SERVICE_PROP = "redshift"
