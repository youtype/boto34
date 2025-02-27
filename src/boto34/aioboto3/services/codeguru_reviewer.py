"""
Wrapper for aioboto3 CodeGuruReviewer service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_codeguru_reviewer/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aioboto3 import Session

    # Wrapper for aioboto3.Session constructor
    # Returns boto34.Session inherited from aioboto3.Session
    session = Session()
    session: boto34.aioboto3.session.Session

    # Type annotated aioboto3.Client
    # Uses the same arguments as aioboto3.client method
    # Returns type annotated aioboto3 CodeGuruReviewer client
    codeguru_reviewer_client = session.codeguru_reviewer.client()
    codeguru_reviewer_client: types_aiobotocore_codeguru_reviewer.client.CodeGuruReviewerClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_codeguru_reviewer.client import CodeGuruReviewerClient
except ImportError:
    CodeGuruReviewerClient = object  # type: ignore[misc,assignment]


class CodeGuruReviewerService(
    ServiceFactory[CodeGuruReviewerClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "codeguru-reviewer"
    _SERVICE_PROP = "codeguru_reviewer"
