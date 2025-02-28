"""
Wrapper for aiobotocore ParallelComputingService service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pcs/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_pcs.client import ParallelComputingServiceClient

from boto34.aiobotocore.service_factory import ServiceFactory


class ParallelComputingServiceService(ServiceFactory[ParallelComputingServiceClient]):
    """
    ParallelComputingService service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_pcs/)
    """
