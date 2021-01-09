customer, city = map(int, input().split())

cost = dict()
for _ in range(city):
    money, n = map(int, input().split())
    cost[n] = money

