"""
Wrapper for boto3 Batch service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_batch/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_batch.client import BatchClient

from boto34.boto3.service_factory import ServiceFactory


class BatchService(ServiceFactory[BatchClient]):
    """
    Batch service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_batch/)
    """
