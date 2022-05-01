import collections


def count_response(response):
    result = collections.Counter(response).keys()
    return len(result)

def or_resp(response):
    flat_response = [i for s in response for i in s]
    flatter_response = [i for s in flat_response for i in s]
    return count_response(flatter_response)

def count_response2(response):
    result = response[0]
    for i in response:
        result = list(set(result) & set(i))
    return len(result)
    
if __name__ == '__main__':
    count_response2(['abc', 'axc', 'a'])