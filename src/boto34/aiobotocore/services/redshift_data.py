"""
Wrapper for aiobotocore RedshiftDataAPIService service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_redshift_data/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_redshift_data.client import RedshiftDataAPIServiceClient

from boto34.aiobotocore.service_factory import ServiceFactory


class RedshiftDataAPIServiceService(ServiceFactory[RedshiftDataAPIServiceClient]):
    """
    RedshiftDataAPIService service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_redshift_data/)
    """
