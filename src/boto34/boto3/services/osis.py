"""
Wrapper for boto3 OpenSearchIngestion service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_osis/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_osis.client import OpenSearchIngestionClient

from boto34.boto3.service_factory import ServiceFactory


class OpenSearchIngestionService(ServiceFactory[OpenSearchIngestionClient]):
    """
    OpenSearchIngestion service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_osis/)
    """
