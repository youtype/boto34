"""
Wrapper for aiobotocore ApplicationCostProfiler service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_applicationcostprofiler/)

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
    # Returns type annotated aiobotocore ApplicationCostProfiler client
    async with session.applicationcostprofiler.create_client() as applicationcostprofiler_client:
        applicationcostprofiler_client: (
            types_aiobotocore_applicationcostprofiler.client.ApplicationCostProfilerClient
        )
    ```
"""

from __future__ import annotations

from types_aiobotocore_applicationcostprofiler.client import ApplicationCostProfilerClient

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_applicationcostprofiler.client import ApplicationCostProfilerClient
except ImportError:
    ApplicationCostProfilerClient = object  # type: ignore[misc,assignment]


class ApplicationCostProfilerService(
    ServiceFactory[ApplicationCostProfilerClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "applicationcostprofiler"
    _SERVICE_PROP = "applicationcostprofiler"
