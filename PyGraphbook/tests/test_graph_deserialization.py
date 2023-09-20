import pytest
import json

from src import graph

sample_graph = """
{
    "name": "contain",
    "primitive_name": "contain",
    "aliases": [
        "exist",
        "find"
    ],
    "type": "PRIMITIVE_OPERATION",
    "inputs": [
        {
            "name": "target",
            "primitive_name": "target",
            "type": "DECIMAL",
            "shape": []
        },
        "check_against"
    ],
    "outputs": [
        "is_contain"
    ],
    "assertions": [
        "{target}_data_type_is_the_same_as_{check_against}",
        "{check_against}_is_array",
        "{is_contain}_data_type_is_boolean",
        "{target}_shape_is_the_same_as_{is_contain}"
    ],
    "description": [
        "Check whether each element of `target` is in `check_against`"
    ],
    "examples": [
        {
            "inputs": [
                {
                    "name": "target",
                    "data": [
                        1,
                        2,
                        3,
                        4,
                        5,
                        6
                    ],
                    "type": "INTEGER"
                },
                {
                    "name": "check_against",
                    "data": [
                        2,
                        5,
                        11
                    ],
                    "type": "INTEGER"
                }
            ],
            "outputs": [
                {
                    "name": "is_contain",
                    "primitive_name": "is_contain",
                    "data": [
                        false,
                        true,
                        false,
                        false,
                        true,
                        false
                    ],
                    "type": "BOOLEAN",
                    "shape": [
                        6
                    ]
                }
            ]
        },
        {
            "inputs": [
                {
                    "name": "target",
                    "data": [
                        [
                            0.3,
                            0.2,
                            1.3
                        ],
                        [
                            8.4,
                            5.5,
                            9.0
                        ]
                    ],
                    "type": "DECIMAL"
                },
                {
                    "name": "check_against",
                    "data": [
                        0.3,
                        1.3,
                        9.0,
                        4.2
                    ],
                    "type": "DECIMAL"
                }
            ],
            "outputs": [
                {
                    "name": "is_contain",
                    "primitive_name": "is_contain",
                    "data": [
                        [
                            true,
                            false,
                            true
                        ],
                        [
                            false,
                            false,
                            true
                        ]
                    ],
                    "type": "BOOLEAN",
                    "shape": [
                        2,
                        3
                    ]
                }
            ]
        },
        {
            "inputs": [
                {
                    "name": "target",
                    "data": [
                        [
                            "foo",
                            "bar",
                            "foo1"
                        ],
                        [
                            "bar1",
                            "foo2",
                            "bar2"
                        ]
                    ],
                    "type": "TEXT"
                },
                {
                    "name": "check_against",
                    "data": [
                        "bar",
                        "foo2",
                        "bar2"
                    ],
                    "type": "TEXT"
                }
            ],
            "outputs": [
                {
                    "name": "is_contain",
                    "primitive_name": "is_contain",
                    "data": [
                        [
                            false,
                            true,
                            false
                        ],
                        [
                            false,
                            true,
                            true
                        ]
                    ],
                    "type": "BOOLEAN",
                    "shape": [
                        2,
                        3
                    ]
                }
            ]
        }
    ]
}
"""

@pytest.mark.parametrize(
    "graph_string",
    [
        sample_graph,
    ],
)
def test_graph_deserialization(graph_string):

    graph_json = json.loads(graph_string)

    graph_object = graph.Operation.model_validate(graph_json)


    print(graph_object)