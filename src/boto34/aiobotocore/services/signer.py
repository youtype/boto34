"""
Wrapper for aiobotocore Signer service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_signer/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_signer.client import SignerClient

from boto34.aiobotocore.service_factory import ServiceFactory


class SignerService(ServiceFactory[SignerClient]):
    """
    Signer service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_signer/)
    """
