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

prime_factor.append(number)

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

# 20180420
# 10001번째 소수를 찾아라
# 소수를 10001개 만들고 마지막 꺼 부르면 되는거 아님?

def is_prime(n):

	number = 2
	prime_numbers = [2]
	ox = []

	while len(prime_numbers) < n:
		number = number + 1
		for i in prime_numbers:
			ox.append(number % i)
			if number % i == 0:
				break
		if 0 in ox:
			ox = []
			continue	
		else:
			prime_numbers.append(number)	
			

	print(prime_numbers[n-1])	

is_prime(10001)

# 진짜 말이 안 된다. 이거 푸는데 왜 이렇게 오래걸렸지?
# 판별용으로 쓸 리스트를 하나 만들었다. ox 여기에 나머지를 넣어두는것
# 0이 있으면 나눠떨어졌단 뜻이므로 소수가 아님. 근데 연산 시간 너무 오래 걸린다.
# 중간에 효율 업!!

# 20180422
# 다음 천개의 숫자에서 이웃한 13개의 숫자의 곱 중 가장 큰 놈을 찾아라
# 1부터 13개 2부터 13개 이런식으로 만들고
# 죄다 슬라이싱 해서 리스트로 만들고
# 리스트에 0이 있으면 빼고
# 리스트 안의 수를 전부 곱하기

n = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
set1 = []
m = 0

while True:
	set1.append(str(n)[m:m+13])
	if len(str(n)[m:m+13]) != 13:break
	m = m+1

if len(set1[-1]) != 13:
	set1.pop()

set2 = []

for i in set1:
	if '0' in i : pass
	set2.append(int(i[0])*int(i[1])*int(i[2])*int(i[3])*int(i[4])*int(i[5])*int(i[6])*int(i[7])*int(i[8])*int(i[9])*int(i[10])*int(i[11])*int(i[12]))
print(max(set2))

#20180423
# 피타고라스 삼조 : a제곱 더하기 b제곱은 c제곱
# a+b+c = 1000이 되는 하나가 있는데 이거 찾으셈
from itertools import combinations

test = list(combinations(range(1,999),3))로 하기엔 경우의 수가 많음.

for (a,b,c) in test:
	if a**2 + b**2 == c**2 and a+b+c == 1000:
		print(a * b * c)

# 이것도 넘 느린데 일단은 맞음
#20180423-2
# 2백만 이하의 소수 합 구하기

number = 3
prime_numbers = [2, 3]
ox = []

while number < 2000000:
	number = number + 2
	for i in prime_numbers:
		ox.append(number % i)
		if number % i == 0:
			break
	if 0 in ox:
		ox = []
		continue	
	else:
		prime_numbers.append(number)

print(sum(prime_numbers))

# 아니 이 식이 맞긴 맞아...근데 계산이 진짜 말도 안 되게 오래 걸려
# 이거는 뭐 소수 판별식을 만들어놔서...

# 20180423-3
# 앞에꺼 아직 돌아가고 있으니까는...

import re
import bs4
import requests
from urllib.request import urlopen

url = 'https://projecteuler.net/problem=11'
html = requests.get(url).text
soup = bs4.BeautifulSoup(html, 'html.parser')
data = soup.find_all('p')
data = data[1].getText()
data = data.replace('\n', ' ')
data = data.split(' ')
del data[0]

# 클리닝 
# 꺼낼 때 int 써야함 (08 이런 애들이 있으니까)
# 복붙하면 깔끔하지 못하니까 여기서 데이터를 가지고

product = []

# 업 & 다운
for i in list(range(0, 339)):
	product.append(int(data[i])*int(data[i+20])*int(data[i+40])*int(data[60]))

# 왼쪽 & 오른쪽

for i in list(range(0, 399)):
	if re.match('\d*7$', str(i)) is not None or re.match('\d*8$', str(i)) is not None or re.match('\d*9$', str(i)) is not None:
		pass
	else:
		product.append(int(data[i])*int(data[i+1])*int(data[i+2])*int(data[i+3]))

# 대각선 두개
for i in list(range(0, 399)):
	if re.match('\d*7$', str(i)) is not None or re.match('\d*8$', str(i)) is not None or re.match('\d*9$', str(i)) is not None:
		pass
	elif i > 336:
		pass
	else:
		product.append(int(data[i])*int(data[i+21])*int(data[i+42])*int(data[i+63]))

for i in list(range(0, 399)):
	if re.match('\d*0$', str(i)) is not None or re.match('\d*1$', str(i)) is not None or re.match('\d*2$', str(i)) is not None:
		pass
	elif i > 340:
		pass
	else:
		product.append(int(data[i])*int(data[i+19])*int(data[i+38])*int(data[i+57]))

# 리.매치를 이용해서 정규표현식을 조건으로 넣는 걸 배웠는데 넘 복잡하다...
# 2차원 배열을 썼어야 했나...?흠

# 20180430

n = 0
triangle_number = 0
divisors = []

while n >= 0:
	n = n + 1
	triangle_number = n * (n+1) / 2
	for i in list(range(1,n+1)):
		if triangle_number % i == 0:
			divisors.append(i)
	if len(divisors) >= 500:
		print(triangle_number)
		break
	else:
		divisors = []

# 이게 식은 무조건 맞는데 너무 오래 걸린다. 
# 약수의 개수를 카운트 하는 함수는 소수 확인과 같음
# 수학적 원리를 찾아내야 한다 >> 실제로도 필요한가?는 다른 문제긴 함

from numpy import prod

def find_by_divisors(n):

	number = 1
	triangle_number = 1
	divisor = 2
	divisors = []
	divisors_cal = []

	while True:
		number = number + 1
		triangle_number = number * (number+1) / 2

		while triangle_number >= divisor:
			if triangle_number % divisor == 0:
				triangle_number = triangle_number / divisor
				divisors.append(divisor)
			else:
				divisor = divisor + 1
		
		divisor = 2
		
		for i in list(set(divisors)):
			divisors_cal.append(divisors.count(i) + 1)
		
		if prod(divisors_cal) >= n:
			print(prod(divisors))
			break
		else:
			divisors = []
			divisors_cal = []

find_by_divisors(500)

# triangle number 를 고쳐가면서 약수를 구했으니까 다시 triangle number를 구하려면 약수를 몽땅 곱해야함

# 20180509-2
# 50자리 숫자 100개의 합을 구한 후 앞에서부터 10개 숫자 구하라
# 이거 머 영어 해석도 못했음...

import re
import bs4
import requests
from urllib.request import urlopen

url = 'https://projecteuler.net/problem=13'
html = requests.get(url).text
soup = bs4.BeautifulSoup(html, 'html.parser')
data = soup.find_all('div')
data = data[10].getText()
data = data.replace('\n', '')

i = 0
j = 50
count = 0
result = []

while count != 100:
	count = count + 1
	result.append(int(data[i:j]))
	i = i + 50
	j = j + 50

str(sum(result))[0:10]

# 이건 뭐 어렵지 않았다.