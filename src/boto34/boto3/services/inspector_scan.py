"""
Wrapper for boto3 Inspectorscan service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_inspector_scan/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_inspector_scan.client import InspectorscanClient

from boto34.boto3.service_factory import ServiceFactory


class InspectorscanService(ServiceFactory[InspectorscanClient]):
    """
    Inspectorscan service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_inspector_scan/)
    """
