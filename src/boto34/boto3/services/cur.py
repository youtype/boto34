"""
Wrapper for boto3 CostandUsageReportService service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cur/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_cur.client import CostandUsageReportServiceClient

from boto34.boto3.service_factory import ServiceFactory


class CostandUsageReportServiceService(ServiceFactory[CostandUsageReportServiceClient]):
    """
    CostandUsageReportService service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_cur/)
    """
