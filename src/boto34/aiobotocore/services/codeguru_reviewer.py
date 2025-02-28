"""
Wrapper for aiobotocore CodeGuruReviewer service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeguru_reviewer/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_codeguru_reviewer.client import CodeGuruReviewerClient

from boto34.aiobotocore.service_factory import ServiceFactory


class CodeGuruReviewerService(ServiceFactory[CodeGuruReviewerClient]):
    """
    CodeGuruReviewer service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeguru_reviewer/)
    """
