"""
Wrapper for aioboto3 CodeGuruProfiler service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_codeguruprofiler/)

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
    # Returns type annotated aioboto3 CodeGuruProfiler client
    codeguruprofiler_client = session.codeguruprofiler.client()
    codeguruprofiler_client: types_aiobotocore_codeguruprofiler.client.CodeGuruProfilerClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_codeguruprofiler.client import CodeGuruProfilerClient

from boto34.aioboto3.service_factory import ServiceFactory


class CodeGuruProfilerService(ServiceFactory[CodeGuruProfilerClient]):
    SERVICE_NAME = "codeguruprofiler"
    _SERVICE_PROP = "codeguruprofiler"
