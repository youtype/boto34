"""
Wrapper for aiobotocore CostandUsageReportService service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cur/)

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
    # Returns type annotated aiobotocore CostandUsageReportService client
    async with session.cur.create_client() as cur_client:
        cur_client: types_aiobotocore_cur.client.CostandUsageReportServiceClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_cur.client import CostandUsageReportServiceClient

from boto34.aiobotocore.service_factory import ServiceFactory


class CostandUsageReportServiceService(ServiceFactory[CostandUsageReportServiceClient]):
    SERVICE_NAME = "cur"
    _SERVICE_PROP = "cur"
