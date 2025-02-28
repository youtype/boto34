"""
Wrapper for boto3 IoTSiteWise service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_iotsitewise/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_iotsitewise.client import IoTSiteWiseClient

from boto34.boto3.service_factory import ServiceFactory


class IoTSiteWiseService(ServiceFactory[IoTSiteWiseClient]):
    """
    IoTSiteWise service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_iotsitewise/)
    """
