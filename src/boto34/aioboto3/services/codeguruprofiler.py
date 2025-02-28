"""
Wrapper for aioboto3 CodeGuruProfiler service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_codeguruprofiler/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_codeguruprofiler.client import CodeGuruProfilerClient

from boto34.aioboto3.service_factory import ServiceFactory


class CodeGuruProfilerService(ServiceFactory[CodeGuruProfilerClient]):
    """
    CodeGuruProfiler service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_codeguruprofiler/)
    """
