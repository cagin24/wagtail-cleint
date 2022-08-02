from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.add_script_response_200 import AddScriptResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    name: Union[Unset, str] = UNSET,
    type: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/scripts".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if not isinstance(name, Unset):
        headers["name"] = name

    if not isinstance(type, Unset):
        headers["type"] = type

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[AddScriptResponse200]:
    if response.status_code == 200:
        response_200 = AddScriptResponse200.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[AddScriptResponse200]:
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
    type: Union[Unset, str] = UNSET,
) -> Response[AddScriptResponse200]:
    """Add Script

     Add Script

    Args:
        name (Union[Unset, str]):  Example: custom_script_js.
        type (Union[Unset, str]):  Example: node.

    Returns:
        Response[AddScriptResponse200]
    """

    kwargs = _get_kwargs(
        client=client,
        name=name,
        type=type,
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
    type: Union[Unset, str] = UNSET,
) -> Optional[AddScriptResponse200]:
    """Add Script

     Add Script

    Args:
        name (Union[Unset, str]):  Example: custom_script_js.
        type (Union[Unset, str]):  Example: node.

    Returns:
        Response[AddScriptResponse200]
    """

    return sync_detailed(
        client=client,
        name=name,
        type=type,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    name: Union[Unset, str] = UNSET,
    type: Union[Unset, str] = UNSET,
) -> Response[AddScriptResponse200]:
    """Add Script

     Add Script

    Args:
        name (Union[Unset, str]):  Example: custom_script_js.
        type (Union[Unset, str]):  Example: node.

    Returns:
        Response[AddScriptResponse200]
    """

    kwargs = _get_kwargs(
        client=client,
        name=name,
        type=type,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    name: Union[Unset, str] = UNSET,
    type: Union[Unset, str] = UNSET,
) -> Optional[AddScriptResponse200]:
    """Add Script

     Add Script

    Args:
        name (Union[Unset, str]):  Example: custom_script_js.
        type (Union[Unset, str]):  Example: node.

    Returns:
        Response[AddScriptResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
            name=name,
            type=type,
        )
    ).parsed
