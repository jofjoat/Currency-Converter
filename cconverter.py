import requests

# Function that updates the cache

def cache_update(cache, currency):
    r = requests.get(f'http://www.floatrates.com/daily/{currency_from}.json')
    file = r.json()
    for c in currency:
        if c in file:
            cache[c] = file[c]['rate']

# Arguments for the function
cache = dict()
currency_from = str(input().lower())
cache_update(cache, ['usd', 'eur'])

while True:
    change_to = str(input().lower())
    if change_to == '':
        break
    amount = float(input())
    print('Checking the cache...')
    if change_to in cache:
        print('Oh! It is in the cache!')
        xe = cache[change_to]
    else:
        print('Sorry, but it is not in the cache!')
        cache_update(cache, [change_to])
        xe = cache[change_to]
    amount *= xe
    print(f'You received {amount} {change_to.upper()}')
