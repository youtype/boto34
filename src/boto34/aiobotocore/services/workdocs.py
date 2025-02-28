"""
Wrapper for aiobotocore WorkDocs service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workdocs/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_workdocs.client import WorkDocsClient

from boto34.aiobotocore.service_factory import ServiceFactory


class WorkDocsService(ServiceFactory[WorkDocsClient]):
    """
    WorkDocs service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workdocs/)
    """
