from io import BytesIO
from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, File, FileJsonType, Unset

T = TypeVar("T", bound="MaestroMultipartData")


@attr.s(auto_attribs=True)
class MaestroMultipartData:
    """
    Attributes:
        audio (Union[Unset, File]): A wav file as audio.
        config (Union[Unset, str]): JSON for the configuration. Example: {
            "config":
            {
                "nodes":
                [
                        {
                                "id": "emotion-1",
                                "config":
                                {
                                        "enabled": false
                                }
                        }
                ]
            }
            }.
    """

    audio: Union[Unset, File] = UNSET
    config: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        audio: Union[Unset, FileJsonType] = UNSET
        if not isinstance(self.audio, Unset):
            audio = self.audio.to_tuple()

        config = self.config

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if audio is not UNSET:
            field_dict["audio"] = audio
        if config is not UNSET:
            field_dict["config"] = config

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        audio: Union[Unset, FileJsonType] = UNSET
        if not isinstance(self.audio, Unset):
            audio = self.audio.to_tuple()

        config = self.config if isinstance(self.config, Unset) else (None, str(self.config).encode(), "text/plain")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update({})
        if audio is not UNSET:
            field_dict["audio"] = audio
        if config is not UNSET:
            field_dict["config"] = config

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _audio = d.pop("audio", UNSET)
        audio: Union[Unset, File]
        if isinstance(_audio, Unset):
            audio = UNSET
        else:
            audio = File(payload=BytesIO(_audio))

        config = d.pop("config", UNSET)

        maestro_multipart_data = cls(
            audio=audio,
            config=config,
        )

        maestro_multipart_data.additional_properties = d
        return maestro_multipart_data

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
