############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 sum, min, max, len 함수를 사용하지 않습니다.
# 사용시 감점처리 되니 반드시 확인 바랍니다.
def get_row_col_maxsum(matrix):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    row_len = 0  # 행 길이
    col_len = 0  # 열 길이

    # 행 ==> 리스트 안에 리스트가 몇개?
    for r in matrix:
        row_len += 1
    # 열 ==> 리스트 안에 리스트가 있는데 그 리스트의 원소 갯수가 몇개?
    for c in matrix[0]:
        col_len += 1

    # 지금까지 내가 알고 있던 최대 합
    total_max = 0
    # 행 or 열
    res = ""

    # 가로 합
    # 행 인덱스 먼저 고정 => 열 인덱스 반복
    # 행 0 => 열 0,1,2,3,4,...,c-1
    # 행 1 => 열 0,1,2,3,4,...,c-1
    # ...
    # 행 r-1 => 열 0,1,2,3,4,...,c-1
    for r_i in range(row_len):
        # 새로 구한 합
        total = 0
        # r_i 번째 리스트의 합 구하기
        for c_i in range(col_len):
            total += matrix[r_i][c_i]

        # 큰 값인지 확인
        # 내가 지금까지 알고 있던 합보다 새로 구한 합이 더 크다면
        if total_max < total:
            # 갱신
            total_max = total
            res = "row"  # 가로가 크다고 일단 생각

    # 세로 합
    # 열 인덱스 먼저 고정 => 행 인덱스 반복
    # 열 0 => 행 0,1,2,3,4,...,c-1
    # 열 1 => 행 0,1,2,3,4,...,c-1
    # ..
    # 열 r-1 => 행 0,1,2,3,4,...,c-1
    for c_i in range(col_len):
        # 새로 구한 합
        total = 0
        # 모든 리스트의 c_i 번째 원소들의 합
        for r_i in range(row_len):
            total += matrix[r_i][c_i]

        # 큰 값인지 확인
        if total_max < total:
            # 갱신
            total_max = total
            res = "col"  # 세로가 크다.

    return res, total_max


# 아래 코드는 실행을 위한 코드입니다.
if __name__ == "__main__":
    example_matrix = [[1, 2, 3, 4],
                     [5, 6, 7, 8],
                       [9, 10, 11, 12],
                         [13, 14, 15, 16]]

    example_matrix2 = [[11, 5, 49, 20], [28, 16, 20, 33], [63, 17, 1, 15]]
    print(get_row_col_maxsum(example_matrix))  # => ('row', 58)
    print(get_row_col_maxsum(example_matrix2))  # => ('col', 102)
    # 아래에 추가 테스트를 위한 코드 작성 가능