"""
Wrapper for boto3 CodeGuruProfiler service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_codeguruprofiler/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_codeguruprofiler.client import CodeGuruProfilerClient

from boto34.boto3.service_factory import ServiceFactory


class CodeGuruProfilerService(ServiceFactory[CodeGuruProfilerClient]):
    """
    CodeGuruProfiler service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_codeguruprofiler/)
    """
