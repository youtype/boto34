"""
Wrapper for boto3 CodeGuruReviewer service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_codeguru_reviewer/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_codeguru_reviewer.client import CodeGuruReviewerClient

from boto34.boto3.service_factory import ServiceFactory


class CodeGuruReviewerService(ServiceFactory[CodeGuruReviewerClient]):
    """
    CodeGuruReviewer service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_codeguru_reviewer/)
    """
