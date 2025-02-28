"""
Wrapper for aiobotocore SsmSap service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ssm_sap/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_ssm_sap.client import SsmSapClient

from boto34.aiobotocore.service_factory import ServiceFactory


class SsmSapService(ServiceFactory[SsmSapClient]):
    """
    SsmSap service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_ssm_sap/)
    """
