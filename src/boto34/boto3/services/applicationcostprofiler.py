"""
Wrapper for boto3 ApplicationCostProfiler service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_applicationcostprofiler/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_applicationcostprofiler.client import ApplicationCostProfilerClient

from boto34.boto3.service_factory import ServiceFactory


class ApplicationCostProfilerService(ServiceFactory[ApplicationCostProfilerClient]):
    """
    ApplicationCostProfiler service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_applicationcostprofiler/)
    """
