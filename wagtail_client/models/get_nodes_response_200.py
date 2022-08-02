from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.get_nodes_response_200_nodes_item import GetNodesResponse200NodesItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetNodesResponse200")


@attr.s(auto_attribs=True)
class GetNodesResponse200:
    """
    Attributes:
        node_count (Union[Unset, float]):  Example: 1.
        nodes (Union[Unset, List[GetNodesResponse200NodesItem]]):  Example: [{'id': 1, 'name': 'SR-websocket', 'project-
            id': -1, 'specifications': '{}', 'tenant': 'Default', 'type': 'sr-websocket'}].
    """

    node_count: Union[Unset, float] = UNSET
    nodes: Union[Unset, List[GetNodesResponse200NodesItem]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        node_count = self.node_count
        nodes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.nodes, Unset):
            nodes = []
            for nodes_item_data in self.nodes:
                nodes_item = nodes_item_data.to_dict()

                nodes.append(nodes_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if node_count is not UNSET:
            field_dict["node-count"] = node_count
        if nodes is not UNSET:
            field_dict["nodes"] = nodes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        node_count = d.pop("node-count", UNSET)

        nodes = []
        _nodes = d.pop("nodes", UNSET)
        for nodes_item_data in _nodes or []:
            nodes_item = GetNodesResponse200NodesItem.from_dict(nodes_item_data)

            nodes.append(nodes_item)

        get_nodes_response_200 = cls(
            node_count=node_count,
            nodes=nodes,
        )

        get_nodes_response_200.additional_properties = d
        return get_nodes_response_200

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
