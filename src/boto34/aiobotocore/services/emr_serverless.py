"""
Wrapper for aiobotocore EMRServerless service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_emr_serverless/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_emr_serverless.client import EMRServerlessClient

from boto34.aiobotocore.service_factory import ServiceFactory


class EMRServerlessService(ServiceFactory[EMRServerlessClient]):
    """
    EMRServerless service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_emr_serverless/)
    """
