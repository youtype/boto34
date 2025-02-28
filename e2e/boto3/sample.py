"""
Copyright 2025 Vlad Emelianov
"""

from boto34.boto3 import Session


def main() -> None:
    session = Session()
    reveal_type(session)
    client = session.s3.client()
    reveal_type(client)
    resource = session.s3.resource()
    reveal_type(resource)
    waiter = client.get_waiter("object_exists")
    reveal_type(waiter)
    paginator = client.get_paginator("list_parts")
    reveal_type(paginator)
