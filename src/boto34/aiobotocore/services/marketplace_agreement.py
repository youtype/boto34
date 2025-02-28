"""
Wrapper for aiobotocore AgreementService service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_marketplace_agreement/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_marketplace_agreement.client import AgreementServiceClient

from boto34.aiobotocore.service_factory import ServiceFactory


class AgreementServiceService(ServiceFactory[AgreementServiceClient]):
    """
    AgreementService service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_marketplace_agreement/)
    """
