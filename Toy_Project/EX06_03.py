# EX06_03 : 게시판 페이징
a = int(input("게시물의 총 건수를 입력하세요: "))
b = int(input("한 페이지에 보여줄 게시물의 수를 입력하세요: "))

def getTotalPage(x, y):
    result = x // y + 1 # python3 에서는 몫을 구하려면 // 사용
    if (x % y == 0):
        result -= 1
    
    return result

print(f'페이지 수는 {getTotalPage(a, b)}입니다.')
