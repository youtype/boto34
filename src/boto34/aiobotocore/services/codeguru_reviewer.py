"""
Wrapper for aiobotocore CodeGuruReviewer service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeguru_reviewer/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aiobotocore import get_session

    # Wrapper for aiobotocore.get_session function
    # Returns boto34.Session inherited from aiobotocore.Session
    session = get_session()
    session: boto34.aiobotocore.session.Session

    # Type annotated aiobotocore.AioBaseClient
    # Uses the same arguments as aiobotocore.create_client method
    # Returns type annotated aiobotocore CodeGuruReviewer client
    async with session.codeguru_reviewer.create_client() as codeguru_reviewer_client:
        codeguru_reviewer_client: types_aiobotocore_codeguru_reviewer.client.CodeGuruReviewerClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_codeguru_reviewer.client import CodeGuruReviewerClient
except ImportError:
    CodeGuruReviewerClient = object  # type: ignore[misc,assignment]


class CodeGuruReviewerService(
    ServiceFactory[CodeGuruReviewerClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "codeguru-reviewer"
    _SERVICE_PROP = "codeguru_reviewer"
