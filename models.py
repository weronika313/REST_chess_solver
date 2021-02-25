from typing import List


class Figure(object):
    def __init__(self, current_field: str) -> None:
        self.currentField = current_field

    def list_available_moves(self) -> List[str]:
        pass

    def validate_move(self, dest_field: str) -> bool:
        pass


class King(Figure):
    def list_available_moves(self) -> List[str]:
        list_of_available_moves: List[str] = []
        current_column = get_column_number(self.currentField)  # type: int
        current_row = int(self.currentField[1])  # type: int
        column: int
        row: int
        search_depth_min = -1  # type: int
        search_depth_max = 2  # type: int

        for column in range(search_depth_min, search_depth_max):
            for row in range(search_depth_min, search_depth_max):
                if not (column == 0 and row == 0):

                    neighbour_square_column = (
                            current_column + column
                    )  # type: int
                    neighbour_square_row = current_row + row  # type: int

                    if square_is_legal(
                            neighbour_square_column, neighbour_square_row
                    ):
                        list_of_available_moves.append(
                            get_square_index(
                                neighbour_square_column, neighbour_square_row
                            )
                        )

        return list_of_available_moves

    def validate_move(self, dest_field: str) -> bool:
        current_column = get_column_number(self.currentField)  # type: int
        current_row = int(self.currentField[1])  # type: int
        destination_column = get_column_number(dest_field)  # type: int
        destination_row = int(dest_field[1])  # type: int

        columns_difference = current_column - destination_column  # type: int
        rows_difference = current_row - destination_row  # type: int

        if (
                abs(columns_difference) <= 1
                and abs(rows_difference) <= 1
                and square_is_legal(destination_column, destination_row)
        ):
            return True
        else:
            return False


class Rook(Figure):
    def list_available_moves(self) -> List[str]:
        current_column = get_column_number(self.currentField)  # type: int
        current_row = int(self.currentField[1])  # type: int
        list_of_available_moves = get_vertical_moves(
            current_row, current_column
        ) + get_horizontal_moves(
            current_row, current_column
        )  # type: List[str]

        return list_of_available_moves

    def validate_move(self, dest_field: str) -> bool:
        current_column = get_column_number(self.currentField)  # type: int
        current_row = int(self.currentField[1])  # type: int
        destination_column = get_column_number(dest_field)  # type: int
        destination_row = int(dest_field[1])  # type: int

        if validate_vertical_and_horizontal_move(
                current_row, current_column, destination_row, destination_column
        ):
            return True
        else:
            return False


class Bishop(Figure):
    def list_available_moves(self) -> List[str]:
        current_column = get_column_number(self.currentField)  # type: int
        current_row = int(self.currentField[1])  # type: int
        list_of_available_moves = (
                get_right_down_diagonal_moves(current_row, current_column)
                + get_right_up_diagonal_moves(current_row, current_column)
                + get_left_up_diagonal_moves(current_row, current_column)
                + get_left_down_diagonal_moves(current_row, current_column)
        )  # type: List[str]

        return list_of_available_moves

    def validate_move(self, dest_field: str) -> bool:
        current_column = get_column_number(self.currentField)  # type: int
        current_row = int(self.currentField[1])  # type: int
        destination_column = get_column_number(dest_field)  # type: int
        destination_row = int(dest_field[1])  # type: int
        columns_difference = current_column - destination_column  # type: int
        rows_difference = current_row - destination_row  # type: int

        if validate_diagonal_move(rows_difference, columns_difference):
            return True
        else:
            return False


class Queen(Figure):
    def list_available_moves(self) -> List[str]:
        current_column = get_column_number(self.currentField)  # type: int
        current_row = int(self.currentField[1])  # type: int
        list_of_available_moves = (
                get_right_down_diagonal_moves(current_row, current_column)
                + get_right_up_diagonal_moves(current_row, current_column)
                + get_left_up_diagonal_moves(current_row, current_column)
                + get_left_down_diagonal_moves(current_row, current_column)
                + get_vertical_moves(current_row, current_column)
                + get_horizontal_moves(current_row, current_column)
        )  # type: List[str]

        return list_of_available_moves

    def validate_move(self, dest_field: str) -> bool:
        current_column = get_column_number(self.currentField)  # type: int
        current_row = int(self.currentField[1])  # type: int
        destination_column = get_column_number(dest_field)  # type: int
        destination_row = int(dest_field[1])  # type: int
        columns_difference = current_column - destination_column  # type: int
        rows_difference = current_row - destination_row  # type: int

        if validate_vertical_and_horizontal_move(
                current_row, current_column, destination_row, destination_column
        ) or validate_diagonal_move(rows_difference, columns_difference):
            return True
        else:
            return False


class Knight(Figure):
    def list_available_moves(self) -> List[str]:
        list_of_available_moves: List[str] = []
        current_column = get_column_number(self.currentField)  # type: int
        current_row = int(self.currentField[1])  # type: int
        moves = [
            (-1, 2),
            (1, 2),
            (-2, 1),
            (-2, -1),
            (-1, -2),
            (1, -2),
            (2, 1),
            (2, -1),
        ]  # type: List[tuple]
        move_column: int
        move_row: int
        for move_column, move_row in moves:
            destination_square_column = (
                    current_column + move_column
            )  # type: int
            destination_square_row = current_row + move_row
            if square_is_legal(
                    destination_square_column, destination_square_row
            ):
                list_of_available_moves.append(
                    get_square_index(
                        destination_square_column, destination_square_row
                    )
                )

        return list_of_available_moves

    def validate_move(self, dest_field: str) -> bool:
        current_column = get_column_number(self.currentField)  # type: int
        current_row = int(self.currentField[1])  # type: int
        destination_column = get_column_number(dest_field)  # type: int
        destination_row = int(dest_field[1])  # type: int
        columns_difference = current_column - destination_column  # type: int
        rows_difference = current_row - destination_row  # type: int

        if (abs(columns_difference) == 1 and abs(rows_difference) == 2) or (
                abs(columns_difference) == 2 and abs(rows_difference) == 1
        ):
            return True
        else:
            return False


class Pawn(Figure):
    def list_available_moves(self) -> List[str]:
        list_of_available_moves: List[str] = []
        current_column = get_column_number(self.currentField)  # type: int
        current_row = int(self.currentField[1])  # type: int
        if square_is_legal(current_column, current_row+1):
            list_of_available_moves.append(
                get_square_index(current_column, current_row + 1)
            )
        if self.is_in_the_start_position():
            list_of_available_moves.append(
                get_square_index(current_column, current_row + 2)
            )

        return list_of_available_moves

    def validate_move(self, dest_field: str) -> bool:
        current_column = get_column_number(self.currentField)  # type: int
        current_row = int(self.currentField[1])  # type: int
        destination_column = get_column_number(dest_field)  # type: int
        destination_row = int(dest_field[1])  # type: int
        rows_difference = destination_row - current_row  # type: int

        if square_is_legal(destination_column, destination_row) and current_column == destination_column and (
                rows_difference == 1
                or (rows_difference == 2 and self.is_in_the_start_position())
        ):
            return True
        else:
            return False

    def is_in_the_start_position(self):
        if self.currentField[1] == "2":
            return True
        else:
            return False


def get_column_number(current_field: str) -> int:
    column_number = ord(current_field[0].upper()) - 64  # type: int

    return column_number


def get_horizontal_moves(
        current_row_number: int, current_column_number: int
) -> List[str]:
    list_of_available_moves: List[str] = []
    search_depth_min = 1  # type: int
    search_depth_max = 9  # type: int
    column: int

    for column in range(search_depth_min, search_depth_max):
        if not column == current_column_number:
            list_of_available_moves.append(
                get_square_index(column, current_row_number)
            )

    return list_of_available_moves


def get_vertical_moves(
        current_row_number: int, current_column_number: int
) -> List[str]:
    list_of_available_moves: List[str] = []
    search_depth_min = 1  # type: int
    search_depth_max = 9  # type: int
    row: int

    for row in range(search_depth_min, search_depth_max):
        if not row == current_row_number:
            list_of_available_moves.append(
                get_square_index(current_column_number, row)
            )

    return list_of_available_moves


def validate_vertical_and_horizontal_move(
        current_row: int, current_column: int, dest_row: int, dest_column: int
):
    if (
            current_row == dest_row or current_column == dest_column
    ) and square_is_legal(dest_column, dest_row):
        return True
    else:
        return False


def validate_diagonal_move(rows_difference: int, columns_difference: int):
    if abs(rows_difference) == abs(columns_difference):
        return True
    else:
        return False


def get_right_down_diagonal_moves(
        current_row_number: int, current_column_number: int
) -> List[str]:
    list_of_available_moves: List[str] = []
    column = current_column_number  # type: int
    search_depth_max = column - 1  # type: int
    search_depth_min = 0  # type: int
    row = current_row_number - 1  # type: int

    for column in range(search_depth_max, search_depth_min, (-1)):
        list_of_available_moves.append(get_square_index(column, row))
        row = row - 1
        if row < 1:
            break

    return list_of_available_moves


def get_right_up_diagonal_moves(
        current_row_number: int, current_column_number: int
) -> List[str]:
    list_of_available_moves: List[str] = []
    column = current_column_number  # type: int
    search_depth_min = column + 1  # type: int
    search_depth_max = 9  # type: int
    row = current_row_number + 1  # type: int

    for column in range(search_depth_min, search_depth_max):
        list_of_available_moves.append(get_square_index(column, row))
        row = row + 1
        if row > 8:
            break

    return list_of_available_moves


def get_left_down_diagonal_moves(
        current_row_number: int, current_column_number: int
) -> List[str]:
    list_of_available_moves: List[str] = []
    column = current_column_number  # type: int
    search_depth_max = 9  # type: int
    search_depth_min = column + 1  # type: int
    row = current_row_number - 1  # type: int

    for column in range(search_depth_min, search_depth_max):
        list_of_available_moves.append(get_square_index(column, row))
        row = row - 1
        if row < 1:
            break

    return list_of_available_moves


def get_left_up_diagonal_moves(
        current_row_number: int, current_column_number: int
) -> List[str]:
    list_of_available_moves: List[str] = []
    column = current_column_number  # type: int
    search_depth_min = 0  # type: int
    search_depth_max = column - 1  # type: int
    row = current_row_number + 1  # type: int

    for column in range(search_depth_max, search_depth_min, (-1)):
        list_of_available_moves.append(get_square_index(column, row))
        row = row + 1
        if row > 8:
            break

    return list_of_available_moves


def get_square_index(column_number: int, row_number: int) -> str:
    column_letter = chr(column_number + 64)  # type: str
    square_index = column_letter + str(row_number)  # type: str

    return square_index


def square_is_legal(column: int, row: int) -> bool:
    if column < 1 or column > 8:
        return False

    if row < 1 or row > 8:
        return False

    return True
