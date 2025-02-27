"""
Wrapper for aiobotocore VPCLattice service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_vpc_lattice/)

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
    # Returns type annotated aiobotocore VPCLattice client
    async with session.vpc_lattice.create_client() as vpc_lattice_client:
        vpc_lattice_client: types_aiobotocore_vpc_lattice.client.VPCLatticeClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_vpc_lattice.client import VPCLatticeClient

from boto34.aiobotocore.service_factory import ServiceFactory


class VPCLatticeService(ServiceFactory[VPCLatticeClient]):
    SERVICE_NAME = "vpc-lattice"
    _SERVICE_PROP = "vpc_lattice"
