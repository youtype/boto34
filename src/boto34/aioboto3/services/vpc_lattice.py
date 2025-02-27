"""
Wrapper for aioboto3 VPCLattice service.

[Documentation](https://youtype.github.io/types_aioboto3_docs/types_aiobotocore_vpc_lattice/)

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
    # Returns type annotated aioboto3 VPCLattice client
    vpc_lattice_client = session.vpc_lattice.client()
    vpc_lattice_client: types_aiobotocore_vpc_lattice.client.VPCLatticeClient
    ```
"""

from __future__ import annotations

from types_aiobotocore_vpc_lattice.client import VPCLatticeClient

from boto34.aioboto3.service_factory import ServiceFactory


class VPCLatticeService(ServiceFactory[VPCLatticeClient]):
    SERVICE_NAME = "vpc-lattice"
    _SERVICE_PROP = "vpc_lattice"
