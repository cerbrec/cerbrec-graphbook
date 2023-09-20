import pytest
import json

from src import graph

sample_graph = """
{
    "name": "GELU",
    "title_is_latex": false,
    "type": "COMPOSITE_OPERATION",
    "inputs": [
        {
            "name": "Input",
            "primitive_name": "Input",
            "is_latex": false
        }
    ],
    "input_order": [
        0
    ],
    "subgraph_input_order": [
        0
    ],
    "outputs": [
        {
            "name": "Output",
            "primitive_name": "Output",
            "is_latex": false
        }
    ],
    "output_order": [
        0
    ],
    "subgraph_output_order": [
        0
    ],
    "operations": [
        {
            "name": "Broadcast Scalar to Shape of Array",
            "title_is_latex": false,
            "type": "COMPOSITE_OPERATION",
            "position": {
                "x": 557,
                "y": 158
            },
            "inputs": [
                {
                    "name": "Scalar",
                    "data": 0.5,
                    "shape": [],
                    "type": "DECIMAL",
                    "primitive_name": "Input",
                    "flow_state": "BOOT_SOURCE",
                    "is_latex": false
                },
                {
                    "name": "Array",
                    "primitive_name": "New Input",
                    "is_latex": false
                }
            ],
            "input_order": [
                0,
                1
            ],
            "subgraph_input_order": [
                0,
                1
            ],
            "outputs": [
                {
                    "name": "Output",
                    "primitive_name": "Output",
                    "is_latex": false
                }
            ],
            "output_order": [
                0
            ],
            "subgraph_output_order": [
                0,
                1
            ],
            "operations": [
                {
                    "name": "get_shape",
                    "title_is_latex": false,
                    "primitive_name": "get_shape",
                    "type": "PRIMITIVE_OPERATION",
                    "aliases": [
                        "shape",
                        "size",
                        "get_size"
                    ],
                    "position": {
                        "x": 601,
                        "y": 346
                    },
                    "inputs": [
                        {
                            "name": "input",
                            "primitive_name": "input",
                            "is_latex": false
                        }
                    ],
                    "input_order": [
                        0
                    ],
                    "outputs": [
                        {
                            "name": "shape",
                            "primitive_name": "shape",
                            "is_latex": false
                        }
                    ],
                    "output_order": [
                        0
                    ],
                    "assertions": [
                        "{input}_is_array",
                        "{shape}_data_type_is_integer",
                        "{shape}_is_greater_than_or_equal_to_zero",
                        "{shape}_has_one_dimension",
                        "{input}_shape_is_{shape}"
                    ]
                },
                {
                    "name": "broadcast_to_shape",
                    "title_is_latex": false,
                    "primitive_name": "broadcast_to_shape",
                    "type": "PRIMITIVE_OPERATION",
                    "aliases": [
                        "broadcast",
                        "tile",
                        "tile_to_shape"
                    ],
                    "position": {
                        "x": 1097,
                        "y": 42
                    },
                    "inputs": [
                        {
                            "name": "target",
                            "data": 0.5,
                            "shape": [],
                            "type": "DECIMAL",
                            "primitive_name": "target",
                            "flow_state": "BOOT_SINK",
                            "is_latex": false
                        },
                        {
                            "name": "shape",
                            "primitive_name": "shape",
                            "is_latex": false
                        }
                    ],
                    "input_order": [
                        0,
                        1
                    ],
                    "outputs": [
                        {
                            "name": "result",
                            "primitive_name": "result",
                            "is_latex": false
                        }
                    ],
                    "output_order": [
                        0
                    ],
                    "assertions": [
                        "{shape}_data_type_is_integer",
                        "{shape}_has_one_dimension",
                        "{target}_shape_size_is_less_than_or_equal_to_{shape}_size",
                        "every_dimension_size_of_{target}_is_less_than_or_equal_to_the_corresponding_value_of_array_{shape}",
                        "{result}_data_type_is_the_same_as_{target}",
                        "{result}_shape_is_{shape}",
                        "{target}_shape_size_is_less_than_or_equal_to_{result}_shape_size",
                        "every_dimension_size_of_{target}_is_less_than_or_equal_to_the_corresponding_dimension_size_of_{result}"
                    ]
                }
            ],
            "links": [
                {
                    "source": {
                        "operation": "this",
                        "data": "Array"
                    },
                    "sink": {
                        "operation": "get_shape",
                        "data": "input"
                    },
                    "control_points": [
                        {
                            "x": 427,
                            "y": 404
                        }
                    ]
                },
                {
                    "source": {
                        "operation": "this",
                        "data": "Scalar"
                    },
                    "sink": {
                        "operation": "broadcast_to_shape",
                        "data": "target"
                    },
                    "control_points": []
                },
                {
                    "source": {
                        "operation": "get_shape",
                        "data": "shape"
                    },
                    "sink": {
                        "operation": "broadcast_to_shape",
                        "data": "shape"
                    },
                    "control_points": []
                },
                {
                    "source": {
                        "operation": "broadcast_to_shape",
                        "data": "result"
                    },
                    "sink": {
                        "operation": "this",
                        "data": "Output"
                    },
                    "control_points": []
                }
            ]
        },
        {
            "name": "element_wise_multiply",
            "title_is_latex": false,
            "primitive_name": "element_wise_multiply",
            "type": "PRIMITIVE_OPERATION",
            "aliases": [
                "mul"
            ],
            "position": {
                "x": 1268,
                "y": 46
            },
            "inputs": [
                {
                    "name": "left_array",
                    "primitive_name": "left_array",
                    "is_latex": false
                },
                {
                    "name": "right_array",
                    "primitive_name": "right_array",
                    "is_latex": false
                }
            ],
            "input_order": [
                0,
                1
            ],
            "outputs": [
                {
                    "name": "multiplied_array",
                    "primitive_name": "multiplied_array",
                    "is_latex": false
                }
            ],
            "output_order": [
                0
            ],
            "assertions": [
                "{left_array}_data_type_is_integer_or_decimal",
                "{right_array}_data_type_is_the_same_as_{left_array}",
                "{right_array}_shape_is_the_same_as_{left_array}",
                "{multiplied_array}_data_type_is_the_same_as_{right_array}",
                "{multiplied_array}_shape_is_the_same_as_{right_array}"
            ]
        },
        {
            "name": "element_wise_exponentiate",
            "title_is_latex": false,
            "primitive_name": "element_wise_exponentiate",
            "type": "PRIMITIVE_OPERATION",
            "aliases": [
                "exp",
                "pow",
                "power"
            ],
            "position": {
                "x": 498,
                "y": 514
            },
            "inputs": [
                {
                    "name": "base",
                    "data": 0.5,
                    "shape": [],
                    "type": "DECIMAL",
                    "primitive_name": "base",
                    "flow_state": "BOOT_SOURCE",
                    "is_latex": false
                },
                {
                    "name": "exponent",
                    "data": 0.5,
                    "shape": [],
                    "type": "DECIMAL",
                    "primitive_name": "exponent",
                    "flow_state": "BOOT_SOURCE",
                    "is_latex": false
                }
            ],
            "input_order": [
                0,
                1
            ],
            "outputs": [
                {
                    "name": "exponentiation",
                    "data": 0.7071067811865476,
                    "shape": [],
                    "type": "DECIMAL",
                    "primitive_name": "exponentiation",
                    "flow_state": "REF_SOURCE",
                    "is_latex": false
                }
            ],
            "output_order": [
                0
            ],
            "assertions": [
                "{base}_data_type_is_decimal",
                "{exponent}_data_type_is_decimal",
                "{exponentiation}_data_type_is_decimal",
                "{exponent}_shape_is_the_same_as_{base}",
                "{exponentiation}_shape_is_the_same_as_{exponent}"
            ]
        },
        {
            "name": "Broadcast Scalar to Shape of Array (1)",
            "title_is_latex": false,
            "type": "COMPOSITE_OPERATION",
            "position": {
                "x": 933,
                "y": 512
            },
            "inputs": [
                {
                    "name": "Scalar",
                    "data": 0.7071067811865476,
                    "shape": [],
                    "type": "DECIMAL",
                    "primitive_name": "Input",
                    "flow_state": "REF_SINK",
                    "is_latex": false
                },
                {
                    "name": "Array",
                    "primitive_name": "New Input",
                    "is_latex": false
                }
            ],
            "input_order": [
                0,
                1
            ],
            "subgraph_input_order": [
                0,
                1
            ],
            "outputs": [
                {
                    "name": "Output",
                    "primitive_name": "Output",
                    "is_latex": false
                }
            ],
            "output_order": [
                0
            ],
            "subgraph_output_order": [
                0,
                1
            ],
            "operations": [
                {
                    "name": "get_shape",
                    "title_is_latex": false,
                    "primitive_name": "get_shape",
                    "type": "PRIMITIVE_OPERATION",
                    "aliases": [
                        "shape",
                        "size",
                        "get_size"
                    ],
                    "position": {
                        "x": 601,
                        "y": 346
                    },
                    "inputs": [
                        {
                            "name": "input",
                            "primitive_name": "input",
                            "is_latex": false
                        }
                    ],
                    "input_order": [
                        0
                    ],
                    "outputs": [
                        {
                            "name": "shape",
                            "primitive_name": "shape",
                            "is_latex": false
                        }
                    ],
                    "output_order": [
                        0
                    ],
                    "assertions": [
                        "{input}_is_array",
                        "{shape}_data_type_is_integer",
                        "{shape}_is_greater_than_or_equal_to_zero",
                        "{shape}_has_one_dimension",
                        "{input}_shape_is_{shape}"
                    ]
                },
                {
                    "name": "broadcast_to_shape",
                    "title_is_latex": false,
                    "primitive_name": "broadcast_to_shape",
                    "type": "PRIMITIVE_OPERATION",
                    "aliases": [
                        "broadcast",
                        "tile",
                        "tile_to_shape"
                    ],
                    "position": {
                        "x": 1097,
                        "y": 42
                    },
                    "inputs": [
                        {
                            "name": "target",
                            "data": 0.7071067811865476,
                            "shape": [],
                            "type": "DECIMAL",
                            "primitive_name": "target",
                            "flow_state": "REF_SINK",
                            "is_latex": false
                        },
                        {
                            "name": "shape",
                            "primitive_name": "shape",
                            "is_latex": false
                        }
                    ],
                    "input_order": [
                        0,
                        1
                    ],
                    "outputs": [
                        {
                            "name": "result",
                            "primitive_name": "result",
                            "is_latex": false
                        }
                    ],
                    "output_order": [
                        0
                    ],
                    "assertions": [
                        "{shape}_data_type_is_integer",
                        "{shape}_has_one_dimension",
                        "{target}_shape_size_is_less_than_or_equal_to_{shape}_size",
                        "every_dimension_size_of_{target}_is_less_than_or_equal_to_the_corresponding_value_of_array_{shape}",
                        "{result}_data_type_is_the_same_as_{target}",
                        "{result}_shape_is_{shape}",
                        "{target}_shape_size_is_less_than_or_equal_to_{result}_shape_size",
                        "every_dimension_size_of_{target}_is_less_than_or_equal_to_the_corresponding_dimension_size_of_{result}"
                    ]
                }
            ],
            "links": [
                {
                    "source": {
                        "operation": "this",
                        "data": "Array"
                    },
                    "sink": {
                        "operation": "get_shape",
                        "data": "input"
                    },
                    "control_points": [
                        {
                            "x": 427,
                            "y": 404
                        }
                    ]
                },
                {
                    "source": {
                        "operation": "this",
                        "data": "Scalar"
                    },
                    "sink": {
                        "operation": "broadcast_to_shape",
                        "data": "target"
                    },
                    "control_points": []
                },
                {
                    "source": {
                        "operation": "get_shape",
                        "data": "shape"
                    },
                    "sink": {
                        "operation": "broadcast_to_shape",
                        "data": "shape"
                    },
                    "control_points": []
                },
                {
                    "source": {
                        "operation": "broadcast_to_shape",
                        "data": "result"
                    },
                    "sink": {
                        "operation": "this",
                        "data": "Output"
                    },
                    "control_points": []
                }
            ]
        },
        {
            "name": "element_wise_multiply_1",
            "title_is_latex": false,
            "primitive_name": "element_wise_multiply",
            "type": "PRIMITIVE_OPERATION",
            "aliases": [
                "mul"
            ],
            "position": {
                "x": 1562,
                "y": 347
            },
            "inputs": [
                {
                    "name": "left_array",
                    "primitive_name": "left_array",
                    "is_latex": false
                },
                {
                    "name": "right_array",
                    "primitive_name": "right_array",
                    "is_latex": false
                }
            ],
            "input_order": [
                0,
                1
            ],
            "outputs": [
                {
                    "name": "multiplied_array",
                    "primitive_name": "multiplied_array",
                    "is_latex": false
                }
            ],
            "output_order": [
                0
            ],
            "assertions": [
                "{left_array}_data_type_is_integer_or_decimal",
                "{right_array}_data_type_is_the_same_as_{left_array}",
                "{right_array}_shape_is_the_same_as_{left_array}",
                "{multiplied_array}_data_type_is_the_same_as_{right_array}",
                "{multiplied_array}_shape_is_the_same_as_{right_array}"
            ]
        },
        {
            "name": "error_function",
            "title_is_latex": false,
            "primitive_name": "error_function",
            "type": "PRIMITIVE_OPERATION",
            "aliases": [
                "erf"
            ],
            "position": {
                "x": 2100,
                "y": 346
            },
            "inputs": [
                {
                    "name": "input",
                    "primitive_name": "input",
                    "is_latex": false
                }
            ],
            "input_order": [
                0
            ],
            "outputs": [
                {
                    "name": "output",
                    "primitive_name": "output",
                    "is_latex": false
                }
            ],
            "output_order": [
                0
            ],
            "assertions": [
                "{input}_data_type_is_decimal",
                "{output}_data_type_is_the_same_as_{input}",
                "{output}_shape_is_the_same_as_{input}"
            ]
        },
        {
            "name": "Broadcast Scalar to Shape of Array (2)",
            "title_is_latex": false,
            "type": "COMPOSITE_OPERATION",
            "position": {
                "x": 2656,
                "y": 502
            },
            "inputs": [
                {
                    "name": "Scalar",
                    "data": 1.0,
                    "shape": [],
                    "type": "DECIMAL",
                    "primitive_name": "Input",
                    "flow_state": "BOOT_SOURCE",
                    "is_latex": false
                },
                {
                    "name": "Array",
                    "primitive_name": "New Input",
                    "is_latex": false
                }
            ],
            "input_order": [
                0,
                1
            ],
            "subgraph_input_order": [
                0,
                1
            ],
            "outputs": [
                {
                    "name": "Output",
                    "primitive_name": "Output",
                    "is_latex": false
                }
            ],
            "output_order": [
                0
            ],
            "subgraph_output_order": [
                0,
                1
            ],
            "operations": [
                {
                    "name": "get_shape",
                    "title_is_latex": false,
                    "primitive_name": "get_shape",
                    "type": "PRIMITIVE_OPERATION",
                    "aliases": [
                        "shape",
                        "size",
                        "get_size"
                    ],
                    "position": {
                        "x": 601,
                        "y": 346
                    },
                    "inputs": [
                        {
                            "name": "input",
                            "primitive_name": "input",
                            "is_latex": false
                        }
                    ],
                    "input_order": [
                        0
                    ],
                    "outputs": [
                        {
                            "name": "shape",
                            "primitive_name": "shape",
                            "is_latex": false
                        }
                    ],
                    "output_order": [
                        0
                    ],
                    "assertions": [
                        "{input}_is_array",
                        "{shape}_data_type_is_integer",
                        "{shape}_is_greater_than_or_equal_to_zero",
                        "{shape}_has_one_dimension",
                        "{input}_shape_is_{shape}"
                    ]
                },
                {
                    "name": "broadcast_to_shape",
                    "title_is_latex": false,
                    "primitive_name": "broadcast_to_shape",
                    "type": "PRIMITIVE_OPERATION",
                    "aliases": [
                        "broadcast",
                        "tile",
                        "tile_to_shape"
                    ],
                    "position": {
                        "x": 1097,
                        "y": 42
                    },
                    "inputs": [
                        {
                            "name": "target",
                            "data": 1.0,
                            "shape": [],
                            "type": "DECIMAL",
                            "primitive_name": "target",
                            "flow_state": "BOOT_SINK",
                            "is_latex": false
                        },
                        {
                            "name": "shape",
                            "primitive_name": "shape",
                            "is_latex": false
                        }
                    ],
                    "input_order": [
                        0,
                        1
                    ],
                    "outputs": [
                        {
                            "name": "result",
                            "primitive_name": "result",
                            "is_latex": false
                        }
                    ],
                    "output_order": [
                        0
                    ],
                    "assertions": [
                        "{shape}_data_type_is_integer",
                        "{shape}_has_one_dimension",
                        "{target}_shape_size_is_less_than_or_equal_to_{shape}_size",
                        "every_dimension_size_of_{target}_is_less_than_or_equal_to_the_corresponding_value_of_array_{shape}",
                        "{result}_data_type_is_the_same_as_{target}",
                        "{result}_shape_is_{shape}",
                        "{target}_shape_size_is_less_than_or_equal_to_{result}_shape_size",
                        "every_dimension_size_of_{target}_is_less_than_or_equal_to_the_corresponding_dimension_size_of_{result}"
                    ]
                }
            ],
            "links": [
                {
                    "source": {
                        "operation": "this",
                        "data": "Array"
                    },
                    "sink": {
                        "operation": "get_shape",
                        "data": "input"
                    },
                    "control_points": [
                        {
                            "x": 427,
                            "y": 404
                        }
                    ]
                },
                {
                    "source": {
                        "operation": "this",
                        "data": "Scalar"
                    },
                    "sink": {
                        "operation": "broadcast_to_shape",
                        "data": "target"
                    },
                    "control_points": []
                },
                {
                    "source": {
                        "operation": "get_shape",
                        "data": "shape"
                    },
                    "sink": {
                        "operation": "broadcast_to_shape",
                        "data": "shape"
                    },
                    "control_points": []
                },
                {
                    "source": {
                        "operation": "broadcast_to_shape",
                        "data": "result"
                    },
                    "sink": {
                        "operation": "this",
                        "data": "Output"
                    },
                    "control_points": []
                }
            ]
        },
        {
            "name": "add",
            "title_is_latex": false,
            "primitive_name": "add",
            "type": "PRIMITIVE_OPERATION",
            "aliases": [
                "plus",
                "increment"
            ],
            "position": {
                "x": 3239,
                "y": 341
            },
            "inputs": [
                {
                    "name": "left_operand",
                    "primitive_name": "left_operand",
                    "is_latex": false
                },
                {
                    "name": "right_operand",
                    "primitive_name": "right_operand",
                    "is_latex": false
                }
            ],
            "input_order": [
                0,
                1
            ],
            "outputs": [
                {
                    "name": "added_result",
                    "primitive_name": "added_result",
                    "is_latex": false
                }
            ],
            "output_order": [
                0
            ],
            "assertions": [
                "{added_result}_shape_is_the_same_as_{right_operand}",
                "{added_result}_data_type_is_the_same_as_{right_operand}",
                "{right_operand}_data_type_is_the_same_as_{left_operand}",
                "{left_operand}_shape_is_the_same_as_{right_operand}",
                "{left_operand}_data_type_is_integer_or_decimal"
            ]
        },
        {
            "name": "element_wise_multiply_2",
            "title_is_latex": false,
            "primitive_name": "element_wise_multiply",
            "type": "PRIMITIVE_OPERATION",
            "aliases": [
                "mul"
            ],
            "position": {
                "x": 3782,
                "y": 47
            },
            "inputs": [
                {
                    "name": "left_array",
                    "primitive_name": "left_array",
                    "is_latex": false
                },
                {
                    "name": "right_array",
                    "primitive_name": "right_array",
                    "is_latex": false
                }
            ],
            "input_order": [
                0,
                1
            ],
            "outputs": [
                {
                    "name": "multiplied_array",
                    "primitive_name": "multiplied_array",
                    "is_latex": false
                }
            ],
            "output_order": [
                0
            ],
            "assertions": [
                "{left_array}_data_type_is_integer_or_decimal",
                "{right_array}_data_type_is_the_same_as_{left_array}",
                "{right_array}_shape_is_the_same_as_{left_array}",
                "{multiplied_array}_data_type_is_the_same_as_{right_array}",
                "{multiplied_array}_shape_is_the_same_as_{right_array}"
            ]
        }
    ],
    "links": [
        {
            "source": {
                "operation": "this",
                "data": "Input"
            },
            "sink": {
                "operation": "element_wise_multiply",
                "data": "left_array"
            },
            "control_points": []
        },
        {
            "source": {
                "operation": "this",
                "data": "Input"
            },
            "sink": {
                "operation": "Broadcast Scalar to Shape of Array",
                "data": "Array"
            },
            "control_points": []
        },
        {
            "source": {
                "operation": "Broadcast Scalar to Shape of Array",
                "data": "Output"
            },
            "sink": {
                "operation": "element_wise_multiply",
                "data": "right_array"
            },
            "control_points": []
        },
        {
            "source": {
                "operation": "element_wise_exponentiate",
                "data": "exponentiation"
            },
            "sink": {
                "operation": "Broadcast Scalar to Shape of Array (1)",
                "data": "Scalar"
            },
            "control_points": []
        },
        {
            "source": {
                "operation": "Broadcast Scalar to Shape of Array (1)",
                "data": "Output"
            },
            "sink": {
                "operation": "element_wise_multiply_1",
                "data": "right_array"
            },
            "control_points": []
        },
        {
            "source": {
                "operation": "element_wise_multiply",
                "data": "multiplied_array"
            },
            "sink": {
                "operation": "element_wise_multiply_2",
                "data": "left_array"
            },
            "control_points": []
        },
        {
            "source": {
                "operation": "this",
                "data": "Input"
            },
            "sink": {
                "operation": "element_wise_multiply_1",
                "data": "left_array"
            },
            "control_points": [
                {
                    "x": 262,
                    "y": 401
                }
            ]
        },
        {
            "source": {
                "operation": "this",
                "data": "Input"
            },
            "sink": {
                "operation": "Broadcast Scalar to Shape of Array (1)",
                "data": "Array"
            },
            "control_points": [
                {
                    "x": 387,
                    "y": 695
                },
                {
                    "x": 855,
                    "y": 695
                }
            ]
        },
        {
            "source": {
                "operation": "element_wise_multiply_1",
                "data": "multiplied_array"
            },
            "sink": {
                "operation": "error_function",
                "data": "input"
            },
            "control_points": []
        },
        {
            "source": {
                "operation": "Broadcast Scalar to Shape of Array (2)",
                "data": "Output"
            },
            "sink": {
                "operation": "add",
                "data": "right_operand"
            },
            "control_points": []
        },
        {
            "source": {
                "operation": "add",
                "data": "added_result"
            },
            "sink": {
                "operation": "element_wise_multiply_2",
                "data": "right_array"
            },
            "control_points": []
        },
        {
            "source": {
                "operation": "error_function",
                "data": "output"
            },
            "sink": {
                "operation": "Broadcast Scalar to Shape of Array (2)",
                "data": "Array"
            },
            "control_points": []
        },
        {
            "source": {
                "operation": "error_function",
                "data": "output"
            },
            "sink": {
                "operation": "add",
                "data": "left_operand"
            },
            "control_points": []
        },
        {
            "source": {
                "operation": "element_wise_multiply_2",
                "data": "multiplied_array"
            },
            "sink": {
                "operation": "this",
                "data": "Output"
            },
            "control_points": []
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
def test_composite_deserialization(graph_string: str):
    """ Test primitive deserialization. """
    graph_json = json.loads(graph_string)

    graph_obj = graph.Operation.model_validate(graph_json)

    assert graph_obj is not None
    assert graph_obj.name == "GELU"
    assert graph_obj.type == "COMPOSITE_OPERATION"

    assert len(graph_obj.links) == 14
    assert len(graph_obj.operations) == 9

    assert len(graph_obj.operations[0].links) == 4
    assert len(graph_obj.operations[0].operations) == 2
