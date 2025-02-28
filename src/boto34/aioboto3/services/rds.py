"""
Wrapper for aioboto3 RDS service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_rds/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_rds.client import RDSClient

from boto34.aioboto3.service_factory import ServiceFactory


class RDSService(ServiceFactory[RDSClient]):
    """
    RDS service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_rds/)
    """
