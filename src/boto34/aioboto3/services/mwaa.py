"""
Wrapper for aioboto3 MWAA service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_mwaa/)

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
    # Returns type annotated aioboto3 MWAA client
    mwaa_client = session.mwaa.client()
    mwaa_client: types_aiobotocore_mwaa.client.MWAAClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_mwaa.client import MWAAClient

from boto34.aioboto3.service_factory import ServiceFactory


class MWAAService(ServiceFactory[MWAAClient]):
    SERVICE_NAME = "mwaa"
    _SERVICE_PROP = "mwaa"
