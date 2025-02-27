"""
Wrapper for aioboto3 CostandUsageReportService service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_cur/)

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
    # Returns type annotated aioboto3 CostandUsageReportService client
    cur_client = session.cur.client()
    cur_client: types_aiobotocore_cur.client.CostandUsageReportServiceClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_cur.client import CostandUsageReportServiceClient

from boto34.aioboto3.service_factory import ServiceFactory


class CostandUsageReportServiceService(ServiceFactory[CostandUsageReportServiceClient]):
    SERVICE_NAME = "cur"
    _SERVICE_PROP = "cur"
