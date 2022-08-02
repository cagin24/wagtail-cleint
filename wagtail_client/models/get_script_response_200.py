from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetScriptResponse200")


@attr.s(auto_attribs=True)
class GetScriptResponse200:
    """
    Attributes:
        content (Union[Unset, str]):  Example: {var CustomNode = function ()
            {
              this._serviceName = 'custom-node'
              this._eventName = 'custom-event'
            }

            CustomNode.prototype.OnAudio = function (channelIndex, samples, sampleCount)
            {
            }

            CustomNode.prototype.OnEvent = function (channelIndex, serviceName, eventName, data)
            {
              var return_data = { 'data': 1 }
              var event = new EventInformation(channelIndex, this._serviceName, this._eventName,
            JSON.stringify(return_data));
              nodeCustom.SendEvent(event);
            }

            CreateNode = function ()
            {
              return new CustomNode();
            }
            }.
        id (Union[Unset, float]):  Example: 1.
        name (Union[Unset, str]):  Example: custom_script_js.
        tenant (Union[Unset, str]):  Example: Default.
        type (Union[Unset, str]):  Example: node.
    """

    content: Union[Unset, str] = UNSET
    id: Union[Unset, float] = UNSET
    name: Union[Unset, str] = UNSET
    tenant: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        content = self.content
        id = self.id
        name = self.name
        tenant = self.tenant
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if content is not UNSET:
            field_dict["content"] = content
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if tenant is not UNSET:
            field_dict["tenant"] = tenant
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        content = d.pop("content", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        tenant = d.pop("tenant", UNSET)

        type = d.pop("type", UNSET)

        get_script_response_200 = cls(
            content=content,
            id=id,
            name=name,
            tenant=tenant,
            type=type,
        )

        get_script_response_200.additional_properties = d
        return get_script_response_200

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
