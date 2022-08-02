from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="AddProjectMultipartData")


@attr.s(auto_attribs=True)
class AddProjectMultipartData:
    """
    Attributes:
        content (Union[Unset, str]): Wagtail specific JSON format for project. Example: {
                "project":
                {
                        "name":"wasp",
                        "nodes":
                        [
                                {"type": "distributor", "id": "entry", "raw-audio-targets":["audio-separator-1"]},

                                {"type": "audio-channel-separator", "id": "audio-separator-1", "audio-targets":["channel-audio-1", "channel-
            audio-2"]},

                                {"type": "distributor", "id": "channel-audio-1", "audio-targets":["vad-1", "vad-for-language-1"]},
                                {"type": "distributor", "id": "channel-audio-2", "audio-targets":["vad-2", "vad-for-language-2"]},

                                {"type": "vad", "id": "vad-for-language-1", "config": {"sensitivity":0.99, "pre-speech-buffer-msec": 250,
            "post-speech-buffer-msec":250, "max-speech-duration-msec": 10000, "silence-trigger-msec": 500}, "event-
            targets":["language-identifier-1"], "audio-targets":["language-identifier-1"]},
                                {"type": "vad", "id": "vad-for-language-2", "config": {"sensitivity":0.99, "pre-speech-buffer-msec": 250,
            "post-speech-buffer-msec":250, "max-speech-duration-msec": 10000, "silence-trigger-msec": 500}, "event-
            targets":["language-identifier-2"], "audio-targets":["language-identifier-2"]},

                                {"type": "vad", "id": "vad-1", "config": {"sensitivity":0.99, "pre-speech-buffer-msec": 250, "post-speech-
            buffer-msec":250}, "event-targets":["sr-1", "emotion-1", "gender-1", "age-1"], "audio-targets":["sr-1",
            "emotion-1", "gender-1", "age-1"]},
                                {"type": "vad", "id": "vad-2", "config": {"sensitivity":4, "pre-speech-buffer-msec": 250, "post-speech-
            buffer-msec":250}, "event-targets":["sr-2", "emotion-2", "gender-2", "age-2"], "audio-targets":["sr-2",
            "emotion-2", "gender-2", "age-2"]},

                                {"type": "sr", "id": "sr-1", "config":{"address":"http://core-sr", "connection-timeout-msec": 5000,
                                        "model": {"tenant": "Default", "name": "TurkishGeneral", "version":"1"}}, "event-targets":["punctuation-1",
            "exit"]},
                                {"type": "sr", "id": "sr-2", "config":{"address":"http://core-sr", "connection-timeout-msec": 5000,
                                        "model": {"tenant": "Default", "name": "TurkishGeneral", "version":"1"}}, "event-targets":["punctuation-2",
            "exit"]},

                                {"type": "emotion", "id": "emotion-1", "config":{"address":"http://192.168.10.201:45679"}, "event-
            targets":["exit"]},
                                {"type": "emotion", "id": "emotion-2", "config":{"address":"http://192.168.10.201:45679"}, "event-targets":
            ["exit"]},

                                {"type": "gender", "id": "gender-1", "config":{"address":"http://192.168.10.128:45678", "confidence-
            threshold":0.8 }, "event-targets":["exit"]},
                                {"type": "gender", "id": "gender-2", "config":{"address":"http://192.168.10.128:45678"}, "event-targets":
            ["exit"]},

                                {"type": "age", "id": "age-1", "config":{"address":"http://192.168.10.128:45678"}, "event-targets":["exit"]},
                                {"type": "age", "id": "age-2", "config":{"address":"http://192.168.10.128:45678"}, "event-targets":["exit"]},

                                {"type": "language-identifier", "id": "language-identifier-1",
            "config":{"address":"http://192.168.10.203:5143"}, "event-targets":["exit"]},
                                {"type": "language-identifier", "id": "language-identifier-2",
            "config":{"address":"http://192.168.10.203:5143"}, "event-targets":["exit"]},

                                {"type": "punctuation", "id": "punctuation-1", "config":{"address": "http://punc.sestek.com:6081", "use-ssl":
            true}, "event-targets":["exit"]},
                                {"type": "punctuation", "id": "punctuation-2", "config":{"address": "http://punc.sestek.com:6081", "use-ssl":
            true}, "event-targets": ["exit"]},

                                {"type": "result-generator", "id": "exit"}
                        ]
                }
            }.
        diagram (Union[Unset, str]): Diagram specific JSON format for project. Giving '{}' is enuogh. Example: {}.
    """

    content: Union[Unset, str] = UNSET
    diagram: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        content = self.content
        diagram = self.diagram

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if content is not UNSET:
            field_dict["content"] = content
        if diagram is not UNSET:
            field_dict["diagram"] = diagram

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        content = self.content if isinstance(self.content, Unset) else (None, str(self.content).encode(), "text/plain")
        diagram = self.diagram if isinstance(self.diagram, Unset) else (None, str(self.diagram).encode(), "text/plain")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update({})
        if content is not UNSET:
            field_dict["content"] = content
        if diagram is not UNSET:
            field_dict["diagram"] = diagram

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        content = d.pop("content", UNSET)

        diagram = d.pop("diagram", UNSET)

        add_project_multipart_data = cls(
            content=content,
            diagram=diagram,
        )

        add_project_multipart_data.additional_properties = d
        return add_project_multipart_data

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
