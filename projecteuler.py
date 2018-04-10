# 20180409
# Multiples of 3 and 5
# 1000 이하에서 3과 5의 배수를 찾아 합을 구하라.

result = []
n = 0

while n < 1000:
	if n % 3 == 0 or n % 5 == 0:
		result.append(n)
	else:
		pass
	n = n + 1


sum(result)

# while문에서 n을 그냥 써도 되는 줄 알앗듬...
# or 연산자 | 아니고 그냥 or
# 커밋 외않된대요...

# 20180410
# Even Fibonacci numbers
# 피보나치 수열 : 직전 두개를 더해서 다음 엘리먼트를 만든다. 1 2 3 5 8 ...
# 피보나치 수열을 만들고, 2로 나눠 떨어지는 것만 찾아서 더하다가 400만 전에 멈춤

fibonacci_numbers = [1, 2]
i = 0

while i > 4000000:
	i = fibonacci_numbers[len(fibonacci_numbers)-2] + fibonacci_numbers[len(fibonacci_numbers)-1]
	fibonacci_numbers.append(i)

even_number = []

for j in fibonacci_numbers:
	if j % 2 == 0:
		even_number.append(j)
	else:
		pass


print(sum(even_number))

# 맞긴 맞는데, 피보나치 수열에서 마지막 요소는 빠지는 게 맞음. 이거야 뭐 눈으로 보고 빼도 되는데...
# 코드가 이렇게 몇 줄 나오는 게 맞나...? 하는 생각은 잠깐 