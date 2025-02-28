"""
Wrapper for aiobotocore Proton service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_proton.client import ProtonClient

from boto34.aiobotocore.service_factory import ServiceFactory


class ProtonService(ServiceFactory[ProtonClient]):
    """
    Proton service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_proton/)
    """
