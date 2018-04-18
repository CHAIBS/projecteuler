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

#20180411
#소인수분해 : 나누어 떨어지게 하는 소수를 찾아라.
#600851475143의 소인수 중 가장 큰 수는?
#우선 600851475143 자연수로 나눠서 나머지가 0인 수를 찾고
#그 중에서 소수만 추려 : 소수는 자기 자신과 1로만 나눠지는 수
#가장 큰 수를 뽑아낸다.

number = 600851475143
n = 2
#prime_factor = []

while number > n:
	if number % n == 0:
		number = number/n
#		prime_factor.append(n)
	else:
		n = n + 1

print(number)

# 끝나고 남은 넘버 출력하면 그게 소수임.

# 20180412
# palindromic number를 만들어라(000 * 000)으로 

from itertools import combinations

three_digit_number = list(combinations(range(100,999),2))
result = []
palindromic_number = []

#100-999 조합찾기 '콤비네이션'

for (i, j) in three_digit_number:
	result.append(i * j)

for i in result:
	if str(i)[0:3] == ''.join(reversed(str(i)[3:6])):
		palindromic_number.append(i)
	else:
		pass

# str로 만들어진 문자열을 ''에 넣어(join) 다시 문자열을 만들었네
# 여기는 좀 검색해서 했음. 대칭수를 찾기 위해 문자처리 > 슬라이신 > 뒤집어서 일치하는지 확인
# s[:: -1] 이것도 있든데...

print(max(palindromic_number))


# 20180413
# 1부터 20까지 모든 수로 나눠떨어지는 가장 최소의 숫자를 구하시오

n = 1

while n > 0:
	 if n%2==0 and n%3==0 and n%4==0 and n%5==0 and n%6==0 and n%7==0 and n%8==0 and n%9==0 and n%10==0 and n%11==0 and n%12==0 and n%13==0 and n%14==0 and n%15==0 and n%16==0 and n%17==0 and n%18==0 and n%19==0 and n%20==0:
	 	print(n)
	 	break
	 else:
	 	n = n+1


# 아니 쉽게 풀긴 했는데, 이거 연산에 시간이 좀 걸리네. 이게 요구하는 답은 아닐 수도.
# 코드 작성하는데 사람이 쓴 시간을 고려하면 역시 이게 맞을수도 있다.

# 20180416
# 제곱의 합 - 합의 제곱 구하기
# 1-100으로 구하라

sum_of_squares = []

for i in list(range(1,101)):
	sum_of_squares.append(i ** 2)

sum(list(range(1,101))) ** 2 - sum(sum_of_squares)

# range(1,100)으로 해야 1 - 100까지의 집합이 된다. 

# 20180416-2
# 10001번째 소수를 찾아라
# 소수를 10001개 만들고 마지막 꺼 부르면 되는거 아님?

n = 2
prime_numbers = [2]


while len(prime_numbers) < 10002:
	for i in prime_numbers:
		n = n + 1 
		if n % i == 0 : continue
	
	prime_numbers.append(n)
			

print(prime_numbers[-1])	


# 소수인지 확인하고
# 프라임 넘버로 나눠지면 패스
# 끝까지 돌았는데도 안나눠지면 어펜드
# 소수면 어펜드

# 소수면 나눠 떨어지는 수가 둘이니까 집합 만들면 len이 2일듯

# 컨티뉴 문을 쓸 수 있지 않을까?
