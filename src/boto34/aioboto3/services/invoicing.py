"""
Wrapper for aioboto3 Invoicing service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_invoicing/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aioboto3 import Session

    # Wrapper for aioboto3.Session constructor
    # Returns boto34.Session inherited from aioboto3.Session
    session = Session()
    session: boto34.aioboto3.session.Session

    # Type annotated aioboto3.Client
    # Uses the same arguments as aioboto3.client method
    # Returns type annotated aioboto3 Invoicing client
    invoicing_client = session.invoicing.client()
    invoicing_client: types_aiobotocore_invoicing.client.InvoicingClient
    ```
"""

from __future__ import annotations

from boto34.aioboto3.service_factory import ServiceFactory

try:
    from types_aiobotocore_invoicing.client import InvoicingClient
except ImportError:
    InvoicingClient = object  # type: ignore[misc,assignment]


class InvoicingService(
    ServiceFactory[InvoicingClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "invoicing"
    _SERVICE_PROP = "invoicing"
