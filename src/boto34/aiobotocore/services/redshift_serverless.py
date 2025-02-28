"""
Wrapper for aiobotocore RedshiftServerless service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_redshift_serverless/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_redshift_serverless.client import RedshiftServerlessClient

from boto34.aiobotocore.service_factory import ServiceFactory


class RedshiftServerlessService(ServiceFactory[RedshiftServerlessClient]):
    """
    RedshiftServerless service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_redshift_serverless/)
    """
