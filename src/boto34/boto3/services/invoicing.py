"""
Wrapper for boto3 Invoicing service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_invoicing/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_boto3_invoicing.client import InvoicingClient

from boto34.boto3.service_factory import ServiceFactory


class InvoicingService(ServiceFactory[InvoicingClient]):
    """
    Invoicing service wrapper.

    [Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_invoicing/)
    """
