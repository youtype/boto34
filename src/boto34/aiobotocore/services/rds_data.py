"""
Wrapper for aiobotocore RDSDataService service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rds_data/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_rds_data.client import RDSDataServiceClient

from boto34.aiobotocore.service_factory import ServiceFactory


class RDSDataServiceService(ServiceFactory[RDSDataServiceClient]):
    """
    RDSDataService service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rds_data/)
    """
