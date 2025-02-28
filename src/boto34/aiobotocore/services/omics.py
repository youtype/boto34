"""
Wrapper for aiobotocore Omics service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_omics/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_omics.client import OmicsClient

from boto34.aiobotocore.service_factory import ServiceFactory


class OmicsService(ServiceFactory[OmicsClient]):
    """
    Omics service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_omics/)
    """
