from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.get_node_scripts_response_200_scripts_item import GetNodeScriptsResponse200ScriptsItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetNodeScriptsResponse200")


@attr.s(auto_attribs=True)
class GetNodeScriptsResponse200:
    """
    Attributes:
        script_count (Union[Unset, float]):  Example: 1.
        scripts (Union[Unset, List[GetNodeScriptsResponse200ScriptsItem]]):  Example: [{'id': 1, 'name':
            'custom_script_js', 'tenant': 'Default', 'type': 'node'}].
    """

    script_count: Union[Unset, float] = UNSET
    scripts: Union[Unset, List[GetNodeScriptsResponse200ScriptsItem]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        script_count = self.script_count
        scripts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.scripts, Unset):
            scripts = []
            for scripts_item_data in self.scripts:
                scripts_item = scripts_item_data.to_dict()

                scripts.append(scripts_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if script_count is not UNSET:
            field_dict["script-count"] = script_count
        if scripts is not UNSET:
            field_dict["scripts"] = scripts

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        script_count = d.pop("script-count", UNSET)

        scripts = []
        _scripts = d.pop("scripts", UNSET)
        for scripts_item_data in _scripts or []:
            scripts_item = GetNodeScriptsResponse200ScriptsItem.from_dict(scripts_item_data)

            scripts.append(scripts_item)

        get_node_scripts_response_200 = cls(
            script_count=script_count,
            scripts=scripts,
        )

        get_node_scripts_response_200.additional_properties = d
        return get_node_scripts_response_200

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
