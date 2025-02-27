"""
Wrapper for aioboto3 SFN service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_stepfunctions/)

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
    # Returns type annotated aioboto3 SFN client
    stepfunctions_client = session.stepfunctions.client()
    stepfunctions_client: types_aiobotocore_stepfunctions.client.SFNClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_stepfunctions.client import SFNClient

from boto34.aioboto3.service_factory import ServiceFactory


class SFNService(ServiceFactory[SFNClient]):
    SERVICE_NAME = "stepfunctions"
    _SERVICE_PROP = "stepfunctions"
