#!flask/bin/python
from typing import List

from flask import Flask, jsonify
import models
from figures_switcher import FiguresSwitcher
from figure_enum import FigureEnum

app = Flask(__name__)


@app.errorhandler(500)
def internal_server_error(e):
    return jsonify({"error": "Internal Server Error)"}), 500


@app.route(
    "/api/v1/<string:chess_figure>/<string:current_field>", methods=["GET"]
)
def get_available_moves(chess_figure: str, current_field: str):
    error = None  # type: str
    available_moves: List[str] = []
    response_code = 500  # type: int

    if validate_figure_name(chess_figure) and validate_field(current_field):

        response_code = 200

        if chess_figure.lower() == "pawn" and current_field[1] == "1":
            error = "Figure cant be in that field"
        else:
            figure = get_figure_by_name(
                chess_figure, current_field
            )  # type: models.Figure
            available_moves = available_moves + figure.list_available_moves()
            if not available_moves:
                error = "Figure doesnt have available moves"

    elif not validate_figure_name(chess_figure):
        error = "Figure does not exist"
        response_code = 404

    elif not validate_field(current_field):
        error = "Field does not exist"
        response_code = 409

    return (
        jsonify(
            {
                "availableMoves": available_moves,
                "error": error,
                "figure": chess_figure,
                "current_field": current_field,
            }
        ),
        response_code,
    )


@app.route(
    "/api/v1/<string:chess_figure>/<string:current_field>/<string:dest_field>",
    methods=["GET"],
)
def get_move_validation(
    chess_figure: str, current_field: str, dest_field: str
):

    error = None  # type: str
    response_code = 500  # type: int
    move_validation = "invalid"  # type: str

    if not validate_figure_name(chess_figure):
        error = "Figure does not exist"
        response_code = 404

    elif not validate_field(current_field):
        error = "Current field does not exist"
        response_code = 409

    elif not validate_field(dest_field):
        error = "Destination field does not exist"
        response_code = 409

    elif (
        validate_figure_name(chess_figure)
        and validate_field(current_field)
        and validate_field(dest_field)
    ):
        figure = get_figure_by_name(
            chess_figure, current_field
        )  # type: models.Figure
        response_code = 200

        if current_field.upper() == dest_field.upper():
            error = "Current field and destination field are the same"
        elif chess_figure.lower() == "pawn" and current_field[1] == "1":
            error = "Figure cant be in that field"
        elif figure.validate_move(dest_field):
            move_validation = "valid"
        else:
            error = "Current move is not permitted."

    return (
        jsonify(
            {
                "move": move_validation,
                "figure": chess_figure,
                "error": error,
                "current_field": current_field,
                "destField": dest_field,
            }
        ),
        response_code,
    )


def get_figure_by_name(figure_name: str, current_field: str) -> models.Figure:
    figure_name = figure_name.lower()
    current_field = current_field.lower()
    s = FiguresSwitcher()
    return s.indirect(figure_name, current_field)


def get_column_number(field: str) -> int:
    column_number = ord(field[0].upper()) - 64  # type: int

    return column_number


def validate_field(field: str) -> bool:

    if len(field) == 2 and field[1].isdigit():
        column_number = get_column_number(field)  # type: int
        row_number = int(field[1])  # type: int

        if column_number < 1 or column_number > 8:
            return False

        if row_number < 1 or row_number > 8:
            return False

        return True
    else:
        return False


def validate_figure_name(figure_name: str) -> bool:
    figure_name = figure_name.lower()
    if FigureEnum.has_value(figure_name):
        return True
    else:
        return False


if __name__ == "__main__":
    app.run(debug=True, port=5500)
