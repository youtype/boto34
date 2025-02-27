"""
Wrapper for boto3 NetworkFirewall service.

[Documentation](https://youtype.github.io/types_boto3_docs/types_boto3_network_firewall/)

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
    # Returns type annotated boto3 NetworkFirewall client
    network_firewall_client = session.network_firewall.client()
    network_firewall_client: types_boto3_network_firewall.client.NetworkFirewallClient
    ```
"""

from __future__ import annotations

from boto34.boto3.service_factory import ServiceFactory

try:
    from types_boto3_network_firewall.client import NetworkFirewallClient
except ImportError:
    NetworkFirewallClient = object  # type: ignore[misc,assignment]


class NetworkFirewallService(
    ServiceFactory[NetworkFirewallClient]  # type: ignore[misc,assignment]
):
    SERVICE_NAME = "network-firewall"
    _SERVICE_PROP = "network_firewall"
