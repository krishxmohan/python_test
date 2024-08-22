class Queries:

    def __init__(self, dictionary, queries):
        self.dictionary = dictionary
        self.queries = queries

    def sol_query(self):
        results = [self.dictionary[query] for query in self.queries if query in self.dictionary]
        return results


if __name__ == "__main__":
    get_dict = {1: "abc", 2: "cde", 3: "fgh"}
    query = [2, 3, 4]
    que = Queries(get_dict, query)
    result = que.sol_query()
    print(result)
