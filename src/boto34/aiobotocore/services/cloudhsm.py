"""
Wrapper for aiobotocore CloudHSM service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudhsm/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_cloudhsm.client import CloudHSMClient

from boto34.aiobotocore.service_factory import ServiceFactory


class CloudHSMService(ServiceFactory[CloudHSMClient]):
    """
    CloudHSM service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_cloudhsm/)
    """
