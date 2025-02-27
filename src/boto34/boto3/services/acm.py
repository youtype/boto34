"""
Wrapper for boto3 ACM 1.37.1 service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_acm/)

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
    # Returns type annotated boto3 ACM client
    acm_client = session.acm.client()
    acm_client: types_boto3_acm.client.ACMClient

    # Type annotated shortcuts for boto3.Client.get_waiter
    # Initialize client first to use it

    acm_waiter = session.acm.get_waiters(acm_client).certificate_validated
    acm_waiter: types_boto3_acm.waiter.CertificateValidatedWaiter

    # Type annotated shortcuts for boto3.Client.get_paginator
    # Initialize client first to use it

    acm_paginator = session.acm.get_paginators(acm_client).list_certificates
    acm_paginator: types_boto3_acm.paginator.ListCertificatesPaginator```
"""

from __future__ import annotations

from types_boto3_acm.client import ACMClient
from types_boto3_acm.paginator import ListCertificatesPaginator
from types_boto3_acm.waiter import CertificateValidatedWaiter

from boto34.boto3.client_factory import ClientFactory
from boto34.boto3.service_factory import ServiceFactory


class ACMWaiterFactory(ClientFactory[ACMClient]):
    @property
    def certificate_validated(self) -> CertificateValidatedWaiter:
        return self._client.get_waiter("certificate_validated")


class ACMPaginatorFactory(ClientFactory[ACMClient]):
    @property
    def list_certificates(self) -> ListCertificatesPaginator:
        return self._client.get_paginator("list_certificates")


class ACMService(
    ServiceFactory[
        ACMClient,
        ACMWaiterFactory,
        ACMPaginatorFactory,
    ]
):
    SERVICE_NAME = "acm"
    _SERVICE_PROP = "acm"
    _WAITER_FACTORY_CLS = ACMWaiterFactory
    _PAGINATOR_FACTORY_CLS = ACMPaginatorFactory

    def get_waiters(self, client: ACMClient) -> ACMWaiterFactory:
        return self._get_waiter_factory(client)

    def get_paginators(self, client: ACMClient) -> ACMPaginatorFactory:
        return self._get_paginator_factory(client)
