import time


data = [
    {"id": 102, "name": "User102"}, {"id": 103, "name": "User103"}, {"id": 104, "name": "User104"},
    {"id": 105, "name": "User105"}, {"id": 106, "name": "User106"}, {"id": 107, "name": "User107"},
    {"id": 108, "name": "User108"}, {"id": 109, "name": "User109"}, {"id": 110, "name": "User110"},
    {"id": 111, "name": "User111"}, {"id": 112, "name": "User112"}, {"id": 113, "name": "User113"},
    {"id": 114, "name": "User114"}, {"id": 115, "name": "User115"}, {"id": 116, "name": "User116"},
    {"id": 117, "name": "User117"}, {"id": 118, "name": "User118"}, {"id": 119, "name": "User119"},
    {"id": 120, "name": "User120"}, {"id": 121, "name": "User121"}, {"id": 122, "name": "User122"},
    {"id": 123, "name": "User123"}, {"id": 124, "name": "User124"}, {"id": 125, "name": "User125"},
    {"id": 126, "name": "User126"}, {"id": 127, "name": "User127"}, {"id": 128, "name": "User128"},
    {"id": 129, "name": "User129"}, {"id": 130, "name": "User130"}, {"id": 131, "name": "User131"},
    {"id": 132, "name": "User132"}, {"id": 133, "name": "User133"}, {"id": 134, "name": "User134"},
    {"id": 135, "name": "User135"}, {"id": 136, "name": "User136"}, {"id": 137, "name": "User137"},
    {"id": 138, "name": "User138"}, {"id": 139, "name": "User139"}, {"id": 140, "name": "User140"},
    {"id": 141, "name": "User141"}, {"id": 142, "name": "User142"}, {"id": 143, "name": "User143"},
    {"id": 144, "name": "User144"}, {"id": 145, "name": "User145"}, {"id": 146, "name": "User146"},
    {"id": 147, "name": "User147"}, {"id": 148, "name": "User148"}, {"id": 149, "name": "User149"},
    {"id": 150, "name": "User150"}, {"id": 151, "name": "User151"}, {"id": 152, "name": "User152"},
    {"id": 153, "name": "User153"}, {"id": 154, "name": "User154"}, {"id": 155, "name": "User155"},
    {"id": 156, "name": "User156"}, {"id": 157, "name": "User157"}, {"id": 158, "name": "User158"},
    {"id": 159, "name": "User159"}, {"id": 160, "name": "User160"}, {"id": 161, "name": "User161"},
    {"id": 162, "name": "User162"}, {"id": 163, "name": "User163"}, {"id": 164, "name": "User164"},
    {"id": 165, "name": "User165"}, {"id": 166, "name": "User166"}, {"id": 167, "name": "User167"},
    {"id": 168, "name": "User168"}, {"id": 169, "name": "User169"}, {"id": 170, "name": "User170"},
    {"id": 171, "name": "User171"}, {"id": 172, "name": "User172"}, {"id": 173, "name": "User173"},
    {"id": 174, "name": "User174"}, {"id": 175, "name": "User175"}, {"id": 176, "name": "User176"},
    {"id": 177, "name": "User177"}, {"id": 178, "name": "User178"}, {"id": 179, "name": "User179"},
    {"id": 180, "name": "User180"}, {"id": 181, "name": "User181"}, {"id": 182, "name": "User182"},
    {"id": 183, "name": "User183"}, {"id": 184, "name": "User184"}, {"id": 185, "name": "User185"},
    {"id": 186, "name": "User186"}, {"id": 187, "name": "User187"}, {"id": 188, "name": "User188"},
    {"id": 189, "name": "User189"}, {"id": 190, "name": "User190"}, {"id": 191, "name": "User191"},
    {"id": 192, "name": "User192"}, {"id": 193, "name": "User193"}, {"id": 194, "name": "User194"},
    {"id": 195, "name": "User195"}, {"id": 196, "name": "User196"}, {"id": 197, "name": "User197"},
    {"id": 198, "name": "User198"}, {"id": 199, "name": "User199"}, {"id": 200, "name": "User200"},
    {"id": 201, "name": "User201"}
]


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        elapsed_time_ms = (end - start) * 1000 
        print(f"Time taken for {func.__name__} is {elapsed_time_ms:.4f} ms")
        return result
    
    return wrapper

@timer
def binary_search_by_id(data: list[dict], id: int) -> int:
    l = 0
    r = len(data) - 1

    while l <= r:
        mid = (l + r) // 2
        
        # if id is found, return the index
        if data[mid]["id"] == id:
            return mid
        
        # if id is less than the mid, search the right half
        elif data[mid]["id"] < id:
            l = mid + 1

        # if id is greater than the mid, search the left half
        else:
            r = mid - 1

    return -1

@timer
def linear_search_by_id(data: list[dict], id: int) -> int:
    for i, item in enumerate(data):
        if item["id"] == id:
            return i
    return -1

if __name__ == "__main__":
    query_idx = int(input("ID: "))

    idx = binary_search_by_id(data, query_idx)
    linear_search_by_id(data, query_idx)
    if idx != -1:
        print(f"Found element on index {idx}")
        print(data[idx])

    else:
        print(f"No object with id {query_idx} found")
