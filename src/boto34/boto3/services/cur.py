"""
Wrapper for boto3 CostandUsageReportService service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cur/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.boto3 import Session

    # Wrapper for boto3.Session constructor
    # Returns boto34.Session inherited from boto3.Session
    session = Session()
    session: boto34.boto3.session.Session

    # Type annotated boto3.Client
    # Uses the same arguments as boto3.client method
    # Returns type annotated boto3 CostandUsageReportService client
    cur_client = session.cur.client()
    cur_client: types_boto3_cur.client.CostandUsageReportServiceClient
    ```
"""

from __future__ import annotations

from types_boto3_cur.client import CostandUsageReportServiceClient

from boto34.boto3.service_factory import ServiceFactory


class CostandUsageReportServiceService(ServiceFactory[CostandUsageReportServiceClient]):
    SERVICE_NAME = "cur"
    _SERVICE_PROP = "cur"
