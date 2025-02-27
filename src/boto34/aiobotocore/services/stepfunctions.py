"""
Wrapper for aiobotocore SFN service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_stepfunctions/)

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
    # Returns type annotated aiobotocore SFN client
    async with session.stepfunctions.create_client() as stepfunctions_client:
        stepfunctions_client: types_aiobotocore_stepfunctions.client.SFNClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_stepfunctions.client import SFNClient

from boto34.aiobotocore.service_factory import ServiceFactory


class SFNService(ServiceFactory[SFNClient]):
    SERVICE_NAME = "stepfunctions"
    _SERVICE_PROP = "stepfunctions"
