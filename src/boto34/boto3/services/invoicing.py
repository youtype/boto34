"""
Wrapper for boto3 Invoicing service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_invoicing/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.boto3 import Session

    # Wrapper for boto3.Session constructor
    # Returns boto34.Session inherited from boto3.Session
    session = Session()
    session: boto34.boto3.session.Session

    # Type annotated boto3.Client
    # Uses the same arguments as boto3.client method
    # Returns type annotated boto3 Invoicing client
    invoicing_client = session.invoicing.client()
    invoicing_client: types_boto3_invoicing.client.InvoicingClient
    ```
"""

from __future__ import annotations

from types_boto3_invoicing.client import InvoicingClient

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_invoicing.client import InvoicingClient
except ImportError:
    InvoicingClient = object  # type: ignore[misc,assignment]


class InvoicingService(
    ServiceFactory[InvoicingClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "invoicing"
    _SERVICE_PROP = "invoicing"
