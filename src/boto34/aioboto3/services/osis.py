"""
Wrapper for aioboto3 OpenSearchIngestion service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_osis/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_osis.client import OpenSearchIngestionClient

from boto34.aioboto3.service_factory import ServiceFactory


class OpenSearchIngestionService(ServiceFactory[OpenSearchIngestionClient]):
    """
    OpenSearchIngestion service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_osis/)
    """
