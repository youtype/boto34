"""
Wrapper for aiobotocore WorkDocs service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workdocs/)

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
    # Returns type annotated aiobotocore WorkDocs client
    async with session.workdocs.create_client() as workdocs_client:
        workdocs_client: types_aiobotocore_workdocs.client.WorkDocsClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_workdocs.client import WorkDocsClient

from boto34.aiobotocore.service_factory import ServiceFactory


class WorkDocsService(ServiceFactory[WorkDocsClient]):
    SERVICE_NAME = "workdocs"
    _SERVICE_PROP = "workdocs"
