from typing import Any, Dict, Union

import httpx

from ...client import Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    node_id: Union[Unset, str] = UNSET,
    script_id: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/nodescripts".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if not isinstance(node_id, Unset):
        headers["node-id"] = node_id

    if not isinstance(script_id, Unset):
        headers["script-id"] = script_id

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _build_response(*, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    *,
    client: Client,
    node_id: Union[Unset, str] = UNSET,
    script_id: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Add Node Scripts

     Add Node Scripts

    Args:
        node_id (Union[Unset, str]):  Example: 1.
        script_id (Union[Unset, str]):  Example: 1.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        node_id=node_id,
        script_id=script_id,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    *,
    client: Client,
    node_id: Union[Unset, str] = UNSET,
    script_id: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Add Node Scripts

     Add Node Scripts

    Args:
        node_id (Union[Unset, str]):  Example: 1.
        script_id (Union[Unset, str]):  Example: 1.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        node_id=node_id,
        script_id=script_id,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
