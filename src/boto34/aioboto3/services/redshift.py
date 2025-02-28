"""
Wrapper for aioboto3 Redshift service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_redshift/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_redshift.client import RedshiftClient

from boto34.aioboto3.service_factory import ServiceFactory


class RedshiftService(ServiceFactory[RedshiftClient]):
    """
    Redshift service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_redshift/)
    """
