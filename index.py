class Solution:
    def romanToInt(self, s: str):
        try:
            if 1 <= len(s) <= 15:
                numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                           'C': 100, 'D': 500, 'M': 1000}
                result = list(map(numbers.get, s))
                for i in range(len(result) - 1):
                    if result[i] == 1 and result[i + 1] == 5:
                        result[i + 1] = 3
                    elif result[i] == 1 and result[i + 1] == 10:
                        result[i + 1] = 8
                    elif result[i] == 10 and result[i + 1] == 50:
                        result[i + 1] = 30
                    elif result[i] == 10 and result[i + 1] == 100:
                        result[i + 1] = 80
                    elif result[i] == 100 and result[i + 1] == 500:
                        result[i + 1] = 300
                    elif result[i] == 100 and result[i + 1] == 1000:
                        result[i + 1] = 800
                if 0 < sum(result) < 4000:
                    return sum(result)
                else:
                    return 'Ой, большое число'
            else:
                return 'Недопустимая длина строки'
        except TypeError:
            return 'Используйте символы IVXLCDM'


string = input()
result = Solution()
print(result.romanToInt(string))
