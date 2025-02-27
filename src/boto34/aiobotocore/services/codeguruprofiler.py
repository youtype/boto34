"""
Wrapper for aiobotocore CodeGuruProfiler service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeguruprofiler/)

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
    # Returns type annotated aiobotocore CodeGuruProfiler client
    async with session.codeguruprofiler.create_client() as codeguruprofiler_client:
        codeguruprofiler_client: types_aiobotocore_codeguruprofiler.client.CodeGuruProfilerClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_codeguruprofiler.client import CodeGuruProfilerClient
except ImportError:
    CodeGuruProfilerClient = object  # type: ignore[misc,assignment]


class CodeGuruProfilerService(
    ServiceFactory[CodeGuruProfilerClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "codeguruprofiler"
    _SERVICE_PROP = "codeguruprofiler"
