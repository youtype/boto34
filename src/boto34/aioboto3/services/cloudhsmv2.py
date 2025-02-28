"""
Wrapper for aioboto3 CloudHSMV2 service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_cloudhsmv2/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_cloudhsmv2.client import CloudHSMV2Client

from boto34.aioboto3.service_factory import ServiceFactory


class CloudHSMV2Service(ServiceFactory[CloudHSMV2Client]):
    """
    CloudHSMV2 service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_cloudhsmv2/)
    """
