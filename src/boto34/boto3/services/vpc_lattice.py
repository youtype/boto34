"""
Wrapper for boto3 VPCLattice service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_vpc_lattice/)

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
    # Returns type annotated boto3 VPCLattice client
    vpc_lattice_client = session.vpc_lattice.client()
    vpc_lattice_client: types_boto3_vpc_lattice.client.VPCLatticeClient
    ```
"""

from __future__ import annotations

from types_boto3_vpc_lattice.client import VPCLatticeClient

from boto34.boto3.service_factory import ServiceFactory


class VPCLatticeService(ServiceFactory[VPCLatticeClient]):
    SERVICE_NAME = "vpc-lattice"
    _SERVICE_PROP = "vpc_lattice"
