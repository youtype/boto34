"""
Wrapper for aioboto3 RDSDataService service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_rds_data/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_rds_data.client import RDSDataServiceClient

from boto34.aioboto3.service_factory import ServiceFactory


class RDSDataServiceService(ServiceFactory[RDSDataServiceClient]):
    """
    RDSDataService service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_rds_data/)
    """
