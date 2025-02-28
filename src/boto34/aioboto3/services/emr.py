"""
Wrapper for aioboto3 EMR service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_emr/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_emr.client import EMRClient

from boto34.aioboto3.service_factory import ServiceFactory


class EMRService(ServiceFactory[EMRClient]):
    """
    EMR service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_emr/)
    """
