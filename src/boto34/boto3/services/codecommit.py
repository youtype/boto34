"""
Wrapper for boto3 CodeCommit service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_codecommit/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_codecommit.client import CodeCommitClient

from boto34.boto3.service_factory import ServiceFactory


class CodeCommitService(ServiceFactory[CodeCommitClient]):
    """
    CodeCommit service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_codecommit/)
    """
