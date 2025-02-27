"""
Wrapper for aioboto3 ApplicationCostProfiler service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_applicationcostprofiler/)

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
    # Returns type annotated aioboto3 ApplicationCostProfiler client
    applicationcostprofiler_client = session.applicationcostprofiler.client()
    applicationcostprofiler_client: (
        types_aiobotocore_applicationcostprofiler.client.ApplicationCostProfilerClient
    )
    ```
"""

from __future__ import annotations

from types_aiobotocore_applicationcostprofiler.client import ApplicationCostProfilerClient

from boto34.aioboto3.service_factory import ServiceFactory


class ApplicationCostProfilerService(ServiceFactory[ApplicationCostProfilerClient]):
    SERVICE_NAME = "applicationcostprofiler"
    _SERVICE_PROP = "applicationcostprofiler"
