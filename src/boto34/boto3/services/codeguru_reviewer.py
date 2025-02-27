"""
Wrapper for boto3 CodeGuruReviewer service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_codeguru_reviewer/)

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
    # Returns type annotated boto3 CodeGuruReviewer client
    codeguru_reviewer_client = session.codeguru_reviewer.client()
    codeguru_reviewer_client: types_boto3_codeguru_reviewer.client.CodeGuruReviewerClient
    ```
"""

from __future__ import annotations

from types_boto3_codeguru_reviewer.client import CodeGuruReviewerClient

from boto34.boto3.service_factory import ServiceFactory


class CodeGuruReviewerService(ServiceFactory[CodeGuruReviewerClient]):
    SERVICE_NAME = "codeguru-reviewer"
    _SERVICE_PROP = "codeguru_reviewer"
