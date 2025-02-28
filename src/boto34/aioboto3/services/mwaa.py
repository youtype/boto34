"""
Wrapper for aioboto3 MWAA service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_mwaa/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_mwaa.client import MWAAClient

from boto34.aioboto3.service_factory import ServiceFactory


class MWAAService(ServiceFactory[MWAAClient]):
    """
    MWAA service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_mwaa/)
    """
