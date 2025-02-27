import pytest
from botocore.exceptions import UnknownServiceError
from moto import mock_aws

from boto34.boto3 import Session


def get_session() -> Session:
    return Session(
        aws_access_key_id="foo",
        aws_secret_access_key="bar",
        region_name="us-east-1",
    )


def test_session_client(moto_server_url: str) -> None:
    session = get_session()
    s3_client = session.s3.client(endpoint_url=moto_server_url)
    s3_client.create_bucket(Bucket="test-bucket")
    s3_client.put_object(Bucket="test-bucket", Key="test-key", Body="test-body")
    assert s3_client.get_object(Bucket="test-bucket", Key="test-key")["Body"].read() == b"test-body"


def test_session_resource(moto_server_url: str) -> None:
    session = get_session()
    s3_resource = session.s3.resource(endpoint_url=moto_server_url)
    s3_resource.create_bucket(Bucket="test-bucket")
    s3_resource.Bucket("test-bucket").put_object(Key="test-key", Body="test-body")
    assert s3_resource.Bucket("test-bucket").Object("test-key").get()["Body"].read() == b"test-body"


@mock_aws
def test_session_proxy_methods() -> None:
    session = get_session()
    assert len(session.s3.get_available_regions())


@mock_aws
def test_session_invalid_service(moto_server_url: str) -> None:
    session = get_session()
    s3_session = session.s3
    s3_session.SERVICE_NAME = "invalid"
    with pytest.raises(UnknownServiceError):
        s3_session.client(endpoint_url=moto_server_url)
