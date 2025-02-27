"""
Wrapper for aiobotocore GlueDataBrew service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_databrew/)

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
    # Returns type annotated aiobotocore GlueDataBrew client
    async with session.databrew.create_client() as databrew_client:
        databrew_client: types_aiobotocore_databrew.client.GlueDataBrewClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_databrew.client import GlueDataBrewClient

from boto34.aiobotocore.service_factory import ServiceFactory


class GlueDataBrewService(ServiceFactory[GlueDataBrewClient]):
    SERVICE_NAME = "databrew"
    _SERVICE_PROP = "databrew"
