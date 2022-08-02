from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.add_node_response_200 import AddNodeResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    name: Union[Unset, str] = UNSET,
    tenant: Union[Unset, str] = UNSET,
    type: Union[Unset, str] = UNSET,
    project_id: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/nodes".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if not isinstance(name, Unset):
        headers["name"] = name

    if not isinstance(tenant, Unset):
        headers["tenant"] = tenant

    if not isinstance(type, Unset):
        headers["type"] = type

    if not isinstance(project_id, Unset):
        headers["project-id"] = project_id

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[AddNodeResponse200]:
    if response.status_code == 200:
        response_200 = AddNodeResponse200.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[AddNodeResponse200]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    name: Union[Unset, str] = UNSET,
    tenant: Union[Unset, str] = UNSET,
    type: Union[Unset, str] = UNSET,
    project_id: Union[Unset, str] = UNSET,
) -> Response[AddNodeResponse200]:
    """Add Node

     Add Node

    Args:
        name (Union[Unset, str]):  Example: TestNode1.
        tenant (Union[Unset, str]):  Example: Default.
        type (Union[Unset, str]):  Example: custom-js.
        project_id (Union[Unset, str]):  Example: -1.

    Returns:
        Response[AddNodeResponse200]
    """

    kwargs = _get_kwargs(
        client=client,
        name=name,
        tenant=tenant,
        type=type,
        project_id=project_id,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    name: Union[Unset, str] = UNSET,
    tenant: Union[Unset, str] = UNSET,
    type: Union[Unset, str] = UNSET,
    project_id: Union[Unset, str] = UNSET,
) -> Optional[AddNodeResponse200]:
    """Add Node

     Add Node

    Args:
        name (Union[Unset, str]):  Example: TestNode1.
        tenant (Union[Unset, str]):  Example: Default.
        type (Union[Unset, str]):  Example: custom-js.
        project_id (Union[Unset, str]):  Example: -1.

    Returns:
        Response[AddNodeResponse200]
    """

    return sync_detailed(
        client=client,
        name=name,
        tenant=tenant,
        type=type,
        project_id=project_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    name: Union[Unset, str] = UNSET,
    tenant: Union[Unset, str] = UNSET,
    type: Union[Unset, str] = UNSET,
    project_id: Union[Unset, str] = UNSET,
) -> Response[AddNodeResponse200]:
    """Add Node

     Add Node

    Args:
        name (Union[Unset, str]):  Example: TestNode1.
        tenant (Union[Unset, str]):  Example: Default.
        type (Union[Unset, str]):  Example: custom-js.
        project_id (Union[Unset, str]):  Example: -1.

    Returns:
        Response[AddNodeResponse200]
    """

    kwargs = _get_kwargs(
        client=client,
        name=name,
        tenant=tenant,
        type=type,
        project_id=project_id,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    name: Union[Unset, str] = UNSET,
    tenant: Union[Unset, str] = UNSET,
    type: Union[Unset, str] = UNSET,
    project_id: Union[Unset, str] = UNSET,
) -> Optional[AddNodeResponse200]:
    """Add Node

     Add Node

    Args:
        name (Union[Unset, str]):  Example: TestNode1.
        tenant (Union[Unset, str]):  Example: Default.
        type (Union[Unset, str]):  Example: custom-js.
        project_id (Union[Unset, str]):  Example: -1.

    Returns:
        Response[AddNodeResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
            name=name,
            tenant=tenant,
            type=type,
            project_id=project_id,
        )
    ).parsed
