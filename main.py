from matrix_io import get_matrix, print_results
from matrix_logic import check_zero_columns, check_decreasing_rows


def main():
    try:
        matrix = get_matrix()
        result1 = check_zero_columns(matrix)
        result2 = check_decreasing_rows(matrix)
        print_results(result1, result2)
    except ValueError as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()