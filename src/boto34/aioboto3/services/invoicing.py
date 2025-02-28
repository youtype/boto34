"""
Wrapper for aioboto3 Invoicing service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_invoicing/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_invoicing.client import InvoicingClient

from boto34.aioboto3.service_factory import ServiceFactory


class InvoicingService(ServiceFactory[InvoicingClient]):
    """
    Invoicing service wrapper.

    [Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_invoicing/)
    """
