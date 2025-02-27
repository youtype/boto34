"""
Wrapper for aiobotocore Invoicing service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_invoicing/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto34.aiobotocore import get_session

    # Wrapper for aiobotocore.get_session function
    # Returns boto34.Session inherited from aiobotocore.Session
    session = get_session()
    session: boto34.aiobotocore.session.Session

    # Type annotated aiobotocore.AioBaseClient
    # Uses the same arguments as aiobotocore.create_client method
    # Returns type annotated aiobotocore Invoicing client
    async with session.invoicing.create_client() as invoicing_client:
        invoicing_client: types_aiobotocore_invoicing.client.InvoicingClient
    ```
"""

from __future__ import annotations

from boto34.aiobotocore.service_factory import ServiceFactory

try:
    from types_aiobotocore_invoicing.client import InvoicingClient
except ImportError:
    InvoicingClient = object  # type: ignore[misc,assignment]


class InvoicingService(
    ServiceFactory[InvoicingClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "invoicing"
    _SERVICE_PROP = "invoicing"
