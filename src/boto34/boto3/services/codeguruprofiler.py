"""
Wrapper for boto3 CodeGuruProfiler service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_codeguruprofiler/)

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
    # Returns type annotated boto3 CodeGuruProfiler client
    codeguruprofiler_client = session.codeguruprofiler.client()
    codeguruprofiler_client: types_boto3_codeguruprofiler.client.CodeGuruProfilerClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_codeguruprofiler.client import CodeGuruProfilerClient
except ImportError:
    CodeGuruProfilerClient = object  # type: ignore[misc,assignment]


class CodeGuruProfilerService(
    ServiceFactory[CodeGuruProfilerClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "codeguruprofiler"
    _SERVICE_PROP = "codeguruprofiler"
