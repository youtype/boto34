"""
Wrapper for aioboto3 Batch service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_batch/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_batch.client import BatchClient

from boto34.aioboto3.service_factory import ServiceFactory


class BatchService(ServiceFactory[BatchClient]):
    """
    Batch service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_batch/)
    """
