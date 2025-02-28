"""
Wrapper for aiobotocore VPCLattice service.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_vpc_lattice/)

Copyright 2025 Vlad Emelianov
"""

from __future__ import annotations

from types_aiobotocore_vpc_lattice.client import VPCLatticeClient

from boto34.aiobotocore.service_factory import ServiceFactory


class VPCLatticeService(ServiceFactory[VPCLatticeClient]):
    """
    VPCLattice service wrapper.

    [Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_vpc_lattice/)
    """
