"""
Wrapper for aiobotocore CodeGuruProfiler service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeguruprofiler/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_codeguruprofiler.client import CodeGuruProfilerClient

from boto34.aiobotocore.service_factory import ServiceFactory


class CodeGuruProfilerService(ServiceFactory[CodeGuruProfilerClient]):
    """
    CodeGuruProfiler service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeguruprofiler/)
    """
