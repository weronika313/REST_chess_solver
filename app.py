#!flask/bin/python
from flask import Flask, jsonify
import models
from figures_switcher import FiguresSwitcher

app = Flask(__name__)


def get_figure_by_name(figure_name: str, current_field: str) -> models.Figure:
    figure_name = figure_name.lower()
    current_field = current_field.lower()
    s = FiguresSwitcher()
    return s.indirect(figure_name, current_field)


@app.route('/api/v1/<string:chess_figure>/<string:current_field>', methods=['GET'])
def get_available_moves(chess_figure, current_field):
    figure = get_figure_by_name(chess_figure, current_field)  # type: models.Figure
    available_moves = figure.list_available_moves()

    return jsonify({'availableMoves': available_moves,
        'error': None,
        'figure': chess_figure,
        'current_field': current_field})


@app.route('/api/v1/<string:chess_figure>/<string:current_field>/<string:dest_field>', methods=['GET'])
def get_move_validation(chess_figure, current_field, dest_field):
    figure = get_figure_by_name(chess_figure, current_field)  # type: models.Figure
    move_validation = "invalid"  # type: str
    if figure.validate_move(dest_field):
        move_validation = "valid"

    return jsonify({'move': move_validation,
        'figure': chess_figure,
        'error': None,
        'current_field': current_field,
        'destField': dest_field})

if __name__ == '__main__':
    app.run(debug=True, port=5500)