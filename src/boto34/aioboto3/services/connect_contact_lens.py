"""
Wrapper for aioboto3 ConnectContactLens service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_connect_contact_lens/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_connect_contact_lens.client import ConnectContactLensClient

from boto34.aioboto3.service_factory import ServiceFactory


class ConnectContactLensService(ServiceFactory[ConnectContactLensClient]):
    """
    ConnectContactLens service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_connect_contact_lens/)
    """
