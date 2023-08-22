import requests


primeAPI = "http://20.244.56.144/numbers/primes"
oddAPI = "http://20.244.56.144/numbers/odd"
randAPI = "http://20.244.56.144/numbers/rand"
fiboAPI = "http://20.244.56.144/numbers/fibo"


def numberManagement():
        res1 = requests.get(primeAPI)
        res2 = requests.get(oddAPI)
        res3 = requests.get(randAPI)
        res4 = requests.get(fiboAPI)
        result = []
        if res1.status_code == 200:
            data = res1.json()
            num = data.get("numbers", [])
            result.extend(num)
        if res2.status_code == 200:
            data = res2.json()
            num = data.get("numbers", [])
            result.extend(num)
        if res3.status_code == 200:
            data = res3.json()
            num = data.get("numbers", [])
            result.extend(num)
        if res4.status_code == 200:
            data = res4.json()
            num = data.get("numbers", [])
            result.extend(num)            
        else:
            print("error")
        x = set(result)
        result = list(x)
        result.sort()
        return {"number": result}

print(numberManagement())
