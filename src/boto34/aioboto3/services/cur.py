"""
Wrapper for aioboto3 CostandUsageReportService service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_cur/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_cur.client import CostandUsageReportServiceClient

from boto34.aioboto3.service_factory import ServiceFactory


class CostandUsageReportServiceService(ServiceFactory[CostandUsageReportServiceClient]):
    """
    CostandUsageReportService service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_cur/)
    """
