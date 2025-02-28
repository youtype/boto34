"""
Wrapper for aioboto3 QBusiness service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_qbusiness/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_qbusiness.client import QBusinessClient

from boto34.aioboto3.service_factory import ServiceFactory


class QBusinessService(ServiceFactory[QBusinessClient]):
    """
    QBusiness service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_qbusiness/)
    """
