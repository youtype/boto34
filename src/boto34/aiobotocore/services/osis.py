"""
Wrapper for aiobotocore OpenSearchIngestion service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_osis/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_osis.client import OpenSearchIngestionClient

from boto34.aiobotocore.service_factory import ServiceFactory


class OpenSearchIngestionService(ServiceFactory[OpenSearchIngestionClient]):
    """
    OpenSearchIngestion service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_osis/)
    """
