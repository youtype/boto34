"""
Wrapper for aioboto3 WorkDocs service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_workdocs/)

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
    # Returns type annotated aioboto3 WorkDocs client
    workdocs_client = session.workdocs.client()
    workdocs_client: types_aiobotocore_workdocs.client.WorkDocsClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_workdocs.client import WorkDocsClient

from boto34.aioboto3.service_factory import ServiceFactory


class WorkDocsService(ServiceFactory[WorkDocsClient]):
    SERVICE_NAME = "workdocs"
    _SERVICE_PROP = "workdocs"
