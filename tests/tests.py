#!flask/bin/python
import pytest
import requests

url = 'http://127.0.0.1:5500/api/v1' # The root url of the flask app


def test_get_available_moves_for_correct_figure_name_and_position_check_status_code_equals_200():
    response = requests.get("http://127.0.0.1:5500/api/v1/rook/a1")
    assert response.status_code == 200


def test_get_available_moves_for_in_incorrect_position_check_status_code_equals_409():
    response = requests.get("http://127.0.0.1:5500/api/v1/rook/6h")
    assert response.status_code == 409


def test_get_available_moves_for_incorrect_figure_name_check_status_code_equals_409():
    response = requests.get("http://127.0.0.1:5500/api/v1/wieza/a1")
    assert response.status_code == 404


def test_get_available_moves_check_content_type_equals_json():
    response = requests.get("http://127.0.0.1:5500/api/v1/rook/a1")
    assert response.headers["Content-Type"] == "application/json"


def test_get_available_moves_for_rook_a1_check_content():
    response = requests.get("http://127.0.0.1:5500/api/v1/rook/a1")
    response_body = response.json()
    assert response_body["current_field"] == "a1"
    assert response_body["figure"] == "rook"
    assert response_body["error"] is None
    assert response_body["availableMoves"] == [
    "A2",
    "A3",
    "A4",
    "A5",
    "A6",
    "A7",
    "A8",
    "B1",
    "C1",
    "D1",
    "E1",
    "F1",
    "G1",
    "H1"
  ]


def test_get_available_moves_for_rook_h8_check_content():
    response = requests.get("http://127.0.0.1:5500/api/v1/rook/h8")
    response_body = response.json()
    assert response_body["current_field"] == "h8"
    assert response_body["figure"] == "rook"
    assert response_body["error"] is None
    assert response_body["availableMoves"] == [
        "H1",
        "H2",
        "H3",
        "H4",
        "H5",
        "H6",
        "H7",
        "A8",
        "B8",
        "C8",
        "D8",
        "E8",
        "F8",
        "G8"
    ]

def test_get_available_moves_for_rook_a0_check_content():
    response = requests.get("http://127.0.0.1:5500/api/v1/rook/a0")
    response_body = response.json()
    assert response_body["current_field"] == "a0"
    assert response_body["figure"] == "rook"
    assert response_body["error"] == "Field does not exist"
    assert response_body["availableMoves"] == []


def test_get_available_moves_for_rook_i9_check_content():
    response = requests.get("http://127.0.0.1:5500/api/v1/rook/i9")
    response_body = response.json()
    assert response_body["current_field"] == "i9"
    assert response_body["figure"] == "rook"
    assert response_body["error"] == "Field does not exist"
    assert response_body["availableMoves"] == []


def test_get_available_moves_for_rook_d5_check_content():
    response = requests.get("http://127.0.0.1:5500/api/v1/rook/d5")
    response_body = response.json()
    assert response_body["current_field"] == "d5"
    assert response_body["figure"] == "rook"
    assert response_body["error"] is None
    assert response_body["availableMoves"] == [ "D1",
    "D2",
    "D3",
    "D4",
    "D6",
    "D7",
    "D8",
    "A5",
    "B5",
    "C5",
    "E5",
    "F5",
    "G5",
    "H5"
]


def test_get_available_moves_for_queen_d5_check_content():
    response = requests.get("http://127.0.0.1:5500/api/v1/queen/d5")
    response_body = response.json()
    assert response_body["current_field"] == "d5"
    assert response_body["figure"] == "queen"
    assert response_body["error"] is None
    assert response_body["availableMoves"] == [ "C4",
    "B3",
    "A2",
    "E6",
    "F7",
    "G8",
    "C6",
    "B7",
    "A8",
    "E4",
    "F3",
    "G2",
    "H1",
    "D1",
    "D2",
    "D3",
    "D4",
    "D6",
    "D7",
    "D8",
    "A5",
    "B5",
    "C5",
    "E5",
    "F5",
    "G5",
    "H5"
  ]


def test_get_available_moves_for_queen_h8_check_content():
    response = requests.get("http://127.0.0.1:5500/api/v1/queen/h8")
    response_body = response.json()
    assert response_body["current_field"] == "h8"
    assert response_body["figure"] == "queen"
    assert response_body["error"] is None
    assert response_body["availableMoves"] == [
        "G7",
        "F6",
        "E5",
        "D4",
        "C3",
        "B2",
        "A1",
        "G9",
        "H1",
        "H2",
        "H3",
        "H4",
        "H5",
        "H6",
        "H7",
        "A8",
        "B8",
        "C8",
        "D8",
        "E8",
        "F8",
        "G8"

    ]

def test_get_available_moves_for_queen_a1_check_content():
    response = requests.get("http://127.0.0.1:5500/api/v1/queen/a1")
    response_body = response.json()
    assert response_body["current_field"] == "a1"
    assert response_body["figure"] == "queen"
    assert response_body["error"] is None
    assert response_body["availableMoves"] == [
        "B2",
        "C3",
        "D4",
        "E5",
        "F6",
        "G7",
        "H8",
        "B0",
        "A2",
        "A3",
        "A4",
        "A5",
        "A6",
        "A7",
        "A8",
        "B1",
        "C1",
        "D1",
        "E1",
        "F1",
        "G1",
        "H1"

    ]


def test_get_available_moves_for_queen_a0_check_content():
    response = requests.get("http://127.0.0.1:5500/api/v1/queen/a0")
    response_body = response.json()
    assert response_body["current_field"] == "a0"
    assert response_body["figure"] == "queen"
    assert response_body["error"] == "Field does not exist"
    assert response_body["availableMoves"] == []


def test_get_available_moves_for_rook_i9_check_content():
    response = requests.get("http://127.0.0.1:5500/api/v1/queen/i9")
    response_body = response.json()
    assert response_body["current_field"] == "i9"
    assert response_body["figure"] == "queen"
    assert response_body["error"] == "Field does not exist"
    assert response_body["availableMoves"] == []


def test_get_available_moves_for_knight_a1_check_content():
    response = requests.get("http://127.0.0.1:5500/api/v1/knight/a1")
    response_body = response.json()
    assert response_body["current_field"] == "a1"
    assert response_body["figure"] == "knight"
    assert response_body["error"] is None
    assert response_body["availableMoves"] == [
        "B3",
        "C2",
    ]


def test_get_available_moves_for_knight_h8_check_content():
    response = requests.get("http://127.0.0.1:5500/api/v1/knight/h8")
    response_body = response.json()
    assert response_body["current_field"] == "h8"
    assert response_body["figure"] == "knight"
    assert response_body["error"] is None
    assert response_body["availableMoves"] == [
        "F7",
        "G6",
    ]


def test_get_available_moves_for_knight_d5_check_content():
    response = requests.get("http://127.0.0.1:5500/api/v1/knight/d5")
    response_body = response.json()
    assert response_body["current_field"] == "d5"
    assert response_body["figure"] == "knight"
    assert response_body["error"] is None
    assert response_body["availableMoves"] == [
        "C7",
        "E7",
        "B6",
        "B4",
        "C3",
        "E3",
        "F6",
        "F4"
    ]


def test_get_available_moves_for_knight_a0_check_content():
    response = requests.get("http://127.0.0.1:5500/api/v1/knight/a0")
    response_body = response.json()
    assert response_body["current_field"] == "a0"
    assert response_body["figure"] == "knight"
    assert response_body["error"] == "Field does not exist"
    assert response_body["availableMoves"] == []


def test_get_available_moves_for_knight_i9_check_content():
    response = requests.get("http://127.0.0.1:5500/api/v1/knight/i9")
    response_body = response.json()
    assert response_body["current_field"] == "i9"
    assert response_body["figure"] == "knight"
    assert response_body["error"] == "Field does not exist"
    assert response_body["availableMoves"] == []


def test_get_available_moves_for_bishop_d5_check_content():
    response = requests.get("http://127.0.0.1:5500/api/v1/bishop/d5")
    response_body = response.json()
    assert response_body["current_field"] == "d5"
    assert response_body["figure"] == "bishop"
    assert response_body["error"] is None
    assert response_body["availableMoves"] == [
        "C4",
        "B3",
        "A2",
        "E6",
        "F7",
        "G8",
        "C6",
        "B7",
        "A8",
        "E4",
        "F3",
        "G2",
        "H1"
    ]


def test_get_available_moves_for_bishop_a1_check_content():
    response = requests.get("http://127.0.0.1:5500/api/v1/bishop/a1")
    response_body = response.json()
    assert response_body["current_field"] == "a1"
    assert response_body["figure"] == "bishop"
    assert response_body["error"] is None
    assert response_body["availableMoves"] == [
        "B2",
        "C3",
        "D4",
        "E5",
        "F6",
        "G7",
        "H8",
        "B0"
    ]

def test_get_available_moves_for_bishop_h8_check_content():
    response = requests.get("http://127.0.0.1:5500/api/v1/bishop/h8")
    response_body = response.json()
    assert response_body["current_field"] == "h8"
    assert response_body["figure"] == "bishop"
    assert response_body["error"] is None
    assert response_body["availableMoves"] == [
        "G7",
        "F6",
        "E5",
        "D4",
        "C3",
        "B2",
        "A1",
        "G9"

    ]


def test_get_available_moves_for_bishop_a0_check_content():
    response = requests.get("http://127.0.0.1:5500/api/v1/bishop/a0")
    response_body = response.json()
    assert response_body["current_field"] == "a0"
    assert response_body["figure"] == "bishop"
    assert response_body["error"] == "Field does not exist"
    assert response_body["availableMoves"] == []


def test_get_available_moves_for_bishop_i9_check_content():
    response = requests.get("http://127.0.0.1:5500/api/v1/bishop/i9")
    response_body = response.json()
    assert response_body["current_field"] == "i9"
    assert response_body["figure"] == "bishop"
    assert response_body["error"] == "Field does not exist"
    assert response_body["availableMoves"] == []


def test_get_available_moves_for_king_h8_check_content():
    response = requests.get("http://127.0.0.1:5500/api/v1/king/h8")
    response_body = response.json()
    assert response_body["current_field"] == "h8"
    assert response_body["figure"] == "king"
    assert response_body["error"] is None
    assert response_body["availableMoves"] == [
        "G7",
        "G8",
        "H7"

    ]


def test_get_available_moves_for_king_a1_check_content():
    response = requests.get("http://127.0.0.1:5500/api/v1/king/a1")
    response_body = response.json()
    assert response_body["current_field"] == "a1"
    assert response_body["figure"] == "king"
    assert response_body["error"] is None
    assert response_body["availableMoves"] == [
        "A2",
        "B1",
        "B2"

    ]


def test_get_available_moves_for_king_d5_check_content():
    response = requests.get("http://127.0.0.1:5500/api/v1/king/d5")
    response_body = response.json()
    assert response_body["current_field"] == "d5"
    assert response_body["figure"] == "king"
    assert response_body["error"] is None
    assert response_body["availableMoves"] == [
        "C4",
        "C5",
        "C6",
        "D4",
        "D6",
        "E4",
        "E5",
        "E6"

    ]


def test_get_available_moves_for_king_a0_check_content():
    response = requests.get("http://127.0.0.1:5500/api/v1/king/a0")
    response_body = response.json()
    assert response_body["current_field"] == "a0"
    assert response_body["figure"] == "king"
    assert response_body["error"] == "Field does not exist"
    assert response_body["availableMoves"] == []


def test_get_available_moves_for_king_i9_check_content():
    response = requests.get("http://127.0.0.1:5500/api/v1/king/i9")
    response_body = response.json()
    assert response_body["current_field"] == "i9"
    assert response_body["figure"] == "king"
    assert response_body["error"] == "Field does not exist"
    assert response_body["availableMoves"] == []


def test_get_available_moves_for_pawn_d5_check_content():
    response = requests.get("http://127.0.0.1:5500/api/v1/pawn/d5")
    response_body = response.json()
    assert response_body["current_field"] == "d5"
    assert response_body["figure"] == "pawn"
    assert response_body["error"] is None
    assert response_body["availableMoves"] == [
        "D6"

    ]

def test_get_available_moves_for_pawn_d8_check_content():
    response = requests.get("http://127.0.0.1:5500/api/v1/pawn/d8")
    response_body = response.json()
    assert response_body["current_field"] == "d8"
    assert response_body["figure"] == "pawn"
    assert response_body["error"] == "Figure doesnt have available moves"
    assert response_body["availableMoves"] == []


def test_get_available_moves_for_pawn_d2_check_content():
    response = requests.get("http://127.0.0.1:5500/api/v1/pawn/d2")
    response_body = response.json()
    assert response_body["current_field"] == "d2"
    assert response_body["figure"] == "pawn"
    assert response_body["error"] is None
    assert response_body["availableMoves"] == ["D3", "D4"]


def test_get_available_moves_for_pawn_a1_check_content():
    response = requests.get("http://127.0.0.1:5500/api/v1/pawn/a1")
    response_body = response.json()
    assert response_body["current_field"] == "a1"
    assert response_body["figure"] == "pawn"
    assert response_body["error"] == "Figure cant be in that field"
    assert response_body["availableMoves"] == []


def test_get_available_moves_for_pawn_a0_check_content():
    response = requests.get("http://127.0.0.1:5500/api/v1/pawn/a0")
    response_body = response.json()
    assert response_body["current_field"] == "a0"
    assert response_body["figure"] == "pawn"
    assert response_body["error"] == "Field does not exist"
    assert response_body["availableMoves"] == []


def test_get_available_moves_for_pawn_i9_check_content():
    response = requests.get("http://127.0.0.1:5500/api/v1/pawn/i9")
    response_body = response.json()
    assert response_body["current_field"] == "i9"
    assert response_body["figure"] == "pawn"
    assert response_body["error"] == "Field does not exist"
    assert response_body["availableMoves"] == []


def test_get_available_moves_for_incorrect_figures_name_check_content():
    response = requests.get("http://127.0.0.1:5500/api/v1/wieza/d5")
    response_body = response.json()
    assert response_body["current_field"] == "d5"
    assert response_body["figure"] == "wieza"
    assert response_body["error"] == "Figure does not exist"
    assert response_body["availableMoves"] == []


def test_get_move_validation_for_correct_figure_name_and_position_check_status_code_equals_200():
    response = requests.get("http://127.0.0.1:5500/api/v1/rook/a1/a2")
    assert response.status_code == 200


def test_get_move_validation_for_in_incorrect_curr_position_check_status_code_equals_409():
    response = requests.get("http://127.0.0.1:5500/api/v1/rook/6h/a6")
    assert response.status_code == 409


def test_get_move_validation_for_in_incorrect_dest_position_check_status_code_equals_409():
    response = requests.get("http://127.0.0.1:5500/api/v1/rook/a6/6h")
    assert response.status_code == 409


def test_get_move_validation_for_incorrect_figure_name_check_status_code_equals_409():
    response = requests.get("http://127.0.0.1:5500/api/v1/wieza/a1/a2")
    assert response.status_code == 404


def test_get_move_validation_check_content_type_equals_json():
    response = requests.get("http://127.0.0.1:5500/api/v1/rook/a1/a2")
    assert response.headers["Content-Type"] == "application/json"


def test_get_move_validation_for_rook_a1_a2_check_content():
    response = requests.get("http://127.0.0.1:5500/api/v1/rook/a1/a2")
    response_body = response.json()
    assert response_body["current_field"] == "a1"
    assert response_body["destField"] == "a2"
    assert response_body["figure"] == "rook"
    assert response_body["error"] is None
    assert response_body["move"] == "valid"


def test_get_move_validation_for_rook_a1_a8_check_content():
    response = requests.get("http://127.0.0.1:5500/api/v1/rook/a1/a8")
    response_body = response.json()
    assert response_body["current_field"] == "a1"
    assert response_body["destField"] == "a8"
    assert response_body["figure"] == "rook"
    assert response_body["error"] is None
    assert response_body["move"] == "valid"


def test_get_move_validation_for_rook_d5_b5_check_content():
    response = requests.get("http://127.0.0.1:5500/api/v1/rook/d5/b5")
    response_body = response.json()
    assert response_body["current_field"] == "d5"
    assert response_body["destField"] == "b5"
    assert response_body["figure"] == "rook"
    assert response_body["error"] is None
    assert response_body["move"] == "valid"


def test_get_move_validation_for_rook_d5_g5_check_content():
    response = requests.get("http://127.0.0.1:5500/api/v1/rook/d5/g5")
    response_body = response.json()
    assert response_body["current_field"] == "d5"
    assert response_body["destField"] == "g5"
    assert response_body["figure"] == "rook"
    assert response_body["error"] is None
    assert response_body["move"] == "valid"


def test_get_move_validation_for_rook_d5_d2_check_content():
    response = requests.get("http://127.0.0.1:5500/api/v1/rook/d5/d2")
    response_body = response.json()
    assert response_body["current_field"] == "d5"
    assert response_body["destField"] == "d2"
    assert response_body["figure"] == "rook"
    assert response_body["error"] is None
    assert response_body["move"] == "valid"


def test_get_move_validation_for_rook_invalid_move_check_content():
    response = requests.get("http://127.0.0.1:5500/api/v1/rook/a1/b2")
    response_body = response.json()
    assert response_body["current_field"] == "a1"
    assert response_body["destField"] == "b2"
    assert response_body["figure"] == "rook"
    assert response_body["error"] == "Current move is not permitted."
    assert response_body["move"] == "invalid"


def test_get_move_validation_for_bishop_a1_h8_check_content():
    response = requests.get("http://127.0.0.1:5500/api/v1/bishop/a1/h8")
    response_body = response.json()
    assert response_body["current_field"] == "a1"
    assert response_body["destField"] == "h8"
    assert response_body["figure"] == "bishop"
    assert response_body["error"] is None
    assert response_body["move"] == "valid"


def test_get_move_validation_for_bishop_a8_h1_check_content():
    response = requests.get("http://127.0.0.1:5500/api/v1/bishop/a8/h1")
    response_body = response.json()
    assert response_body["current_field"] == "a8"
    assert response_body["destField"] == "h1"
    assert response_body["figure"] == "bishop"
    assert response_body["error"] is None
    assert response_body["move"] == "valid"


def test_get_move_validation_for_bishop_h1_a8_check_content():
    response = requests.get("http://127.0.0.1:5500/api/v1/bishop/h1/a8")
    response_body = response.json()
    assert response_body["current_field"] == "h1"
    assert response_body["destField"] == "a8"
    assert response_body["figure"] == "bishop"
    assert response_body["error"] is None
    assert response_body["move"] == "valid"


def test_get_move_validation_for_bishop_d5_b3_check_content():
    response = requests.get("http://127.0.0.1:5500/api/v1/bishop/d5/b3")
    response_body = response.json()
    assert response_body["current_field"] == "d5"
    assert response_body["destField"] == "b3"
    assert response_body["figure"] == "bishop"
    assert response_body["error"] is None
    assert response_body["move"] == "valid"


def test_get_move_validation_for_bishop_h8_a1_check_content():
    response = requests.get("http://127.0.0.1:5500/api/v1/bishop/h8/a1")
    response_body = response.json()
    assert response_body["current_field"] == "h8"
    assert response_body["destField"] == "a1"
    assert response_body["figure"] == "bishop"
    assert response_body["error"] is None
    assert response_body["move"] == "valid"


def test_get_move_validation_for_bishop_invalid_move_check_content():
    response = requests.get("http://127.0.0.1:5500/api/v1/bishop/a1/a2")
    response_body = response.json()
    assert response_body["current_field"] == "a1"
    assert response_body["destField"] == "a2"
    assert response_body["figure"] == "bishop"
    assert response_body["error"] == "Current move is not permitted."
    assert response_body["move"] == "invalid"


def test_get_move_validation_for_queen_a1_a2_check_content():
    response = requests.get("http://127.0.0.1:5500/api/v1/queen/a1/a8")
    response_body = response.json()
    assert response_body["current_field"] == "a1"
    assert response_body["destField"] == "a8"
    assert response_body["figure"] == "queen"
    assert response_body["error"] is None
    assert response_body["move"] == "valid"


def test_get_move_validation_for_queen_a1_h1_check_content():
    response = requests.get("http://127.0.0.1:5500/api/v1/queen/a1/h1")
    response_body = response.json()
    assert response_body["current_field"] == "a1"
    assert response_body["destField"] == "h1"
    assert response_body["figure"] == "queen"
    assert response_body["error"] is None
    assert response_body["move"] == "valid"


def test_get_move_validation_for_queen_a1_h8_check_content():
    response = requests.get("http://127.0.0.1:5500/api/v1/queen/a1/h8")
    response_body = response.json()
    assert response_body["current_field"] == "a1"
    assert response_body["destField"] == "h8"
    assert response_body["figure"] == "queen"
    assert response_body["error"] is None
    assert response_body["move"] == "valid"


def test_get_move_validation_for_queen_invalid_move_check_content():
    response = requests.get("http://127.0.0.1:5500/api/v1/queen/a1/c2")
    response_body = response.json()
    assert response_body["current_field"] == "a1"
    assert response_body["destField"] == "c2"
    assert response_body["figure"] == "queen"
    assert response_body["error"] == "Current move is not permitted."
    assert response_body["move"] == "invalid"


def test_get_move_validation_for_king_valid_move_check_content():
    response = requests.get("http://127.0.0.1:5500/api/v1/king/a1/a2")
    response_body = response.json()
    assert response_body["current_field"] == "a1"
    assert response_body["destField"] == "a2"
    assert response_body["figure"] == "king"
    assert response_body["error"] is None
    assert response_body["move"] == "valid"


def test_get_move_validation_for_king_invalid_move_check_content():
    response = requests.get("http://127.0.0.1:5500/api/v1/king/a1/c2")
    response_body = response.json()
    assert response_body["current_field"] == "a1"
    assert response_body["destField"] == "c2"
    assert response_body["figure"] == "king"
    assert response_body["error"] == "Current move is not permitted."
    assert response_body["move"] == "invalid"


def test_get_move_validation_for_knight_valid_move_check_content():
    response = requests.get("http://127.0.0.1:5500/api/v1/knight/a1/b3")
    response_body = response.json()
    assert response_body["current_field"] == "a1"
    assert response_body["destField"] == "b3"
    assert response_body["figure"] == "knight"
    assert response_body["error"] is None
    assert response_body["move"] == "valid"


def test_get_move_validation_for_pawn_valid_move_check_content():
    response = requests.get("http://127.0.0.1:5500/api/v1/pawn/a3/a4")
    response_body = response.json()
    assert response_body["current_field"] == "a3"
    assert response_body["destField"] == "a4"
    assert response_body["figure"] == "pawn"
    assert response_body["error"] is None
    assert response_body["move"] == "valid"


def test_get_move_validation_for_pawn_valid_start_move_check_content():
    response = requests.get("http://127.0.0.1:5500/api/v1/pawn/a2/a4")
    response_body = response.json()
    assert response_body["current_field"] == "a2"
    assert response_body["destField"] == "a4"
    assert response_body["figure"] == "pawn"
    assert response_body["error"] is None
    assert response_body["move"] == "valid"


def test_get_move_validation_for_pawn_invalid_position_check_content():
    response = requests.get("http://127.0.0.1:5500/api/v1/pawn/a1/a2")
    response_body = response.json()
    assert response_body["current_field"] == "a1"
    assert response_body["destField"] == "a2"
    assert response_body["figure"] == "pawn"
    assert response_body["error"] == "Figure cant be in that field"
    assert response_body["move"] == "invalid"


def test_get_move_validation_for_pawn_invalid_move_check_content():
    response = requests.get("http://127.0.0.1:5500/api/v1/pawn/a2/c2")
    response_body = response.json()
    assert response_body["current_field"] == "a2"
    assert response_body["destField"] == "c2"
    assert response_body["figure"] == "pawn"
    assert response_body["error"] == "Current move is not permitted."
    assert response_body["move"] == "invalid"


def test_get_move_validation_for_knight_invalid_move_check_content():
    response = requests.get("http://127.0.0.1:5500/api/v1/knight/a1/c3")
    response_body = response.json()
    assert response_body["current_field"] == "a1"
    assert response_body["destField"] == "c3"
    assert response_body["figure"] == "knight"
    assert response_body["error"] == "Current move is not permitted."
    assert response_body["move"] == "invalid"


def test_get_move_validation_for_incorrect_dest_field_check_content():
    response = requests.get("http://127.0.0.1:5500/api/v1/rook/a1/a0")
    response_body = response.json()
    assert response_body["current_field"] == "a1"
    assert response_body["destField"] == "a0"
    assert response_body["figure"] == "rook"
    assert response_body["error"] == "Destination field does not exist"
    assert response_body["move"] == "invalid"


def test_get_move_validation_for_incorrect_curr_field_check_content():
    response = requests.get("http://127.0.0.1:5500/api/v1/rook/a0/a1")
    response_body = response.json()
    assert response_body["current_field"] == "a0"
    assert response_body["destField"] == "a1"
    assert response_body["figure"] == "rook"
    assert response_body["error"] == "Current field does not exist"
    assert response_body["move"] == "invalid"


def test_get_move_validation_for_same_field_check_content():
    response = requests.get("http://127.0.0.1:5500/api/v1/rook/a1/a1")
    response_body = response.json()
    assert response_body["current_field"] == "a1"
    assert response_body["destField"] == "a1"
    assert response_body["figure"] == "rook"
    assert response_body["error"] == "Current field and destination field are the same"
    assert response_body["move"] == "invalid"







