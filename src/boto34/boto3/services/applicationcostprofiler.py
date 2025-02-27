"""
Wrapper for boto3 ApplicationCostProfiler service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_applicationcostprofiler/)

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
    # Returns type annotated boto3 ApplicationCostProfiler client
    applicationcostprofiler_client = session.applicationcostprofiler.client()
    applicationcostprofiler_client: (
        types_boto3_applicationcostprofiler.client.ApplicationCostProfilerClient
    )
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_applicationcostprofiler.client import ApplicationCostProfilerClient
except ImportError:
    ApplicationCostProfilerClient = object  # type: ignore[misc,assignment]


class ApplicationCostProfilerService(
    ServiceFactory[ApplicationCostProfilerClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "applicationcostprofiler"
    _SERVICE_PROP = "applicationcostprofiler"
