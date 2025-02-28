"""
Wrapper for aiobotocore CodeCommit service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codecommit/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_codecommit.client import CodeCommitClient

from boto34.aiobotocore.service_factory import ServiceFactory


class CodeCommitService(ServiceFactory[CodeCommitClient]):
    """
    CodeCommit service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codecommit/)
    """
