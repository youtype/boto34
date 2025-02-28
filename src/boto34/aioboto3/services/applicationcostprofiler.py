"""
Wrapper for aioboto3 ApplicationCostProfiler service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_applicationcostprofiler/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_applicationcostprofiler.client import ApplicationCostProfilerClient

from boto34.aioboto3.service_factory import ServiceFactory


class ApplicationCostProfilerService(ServiceFactory[ApplicationCostProfilerClient]):
    """
    ApplicationCostProfiler service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_applicationcostprofiler/)
    """
