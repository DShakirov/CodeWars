

class Dictionary:

    
    def __init__(self, words):
        self.words = words

    @staticmethod
    def levenshtein_distance(str1, str2):
        len_str1 = len(str1)
        len_str2 = len(str2)
        
        matrix = [[0 for _ in range(len_str2 + 1)] for _ in range(len_str1 + 1)]
        
        for i in range(len_str1 + 1):
            matrix[i][0] = i
        for j in range(len_str2 + 1):
            matrix[0][j] = j
            
        for i in range(1, len_str1 + 1):
            for j in range(1, len_str2 + 1):
                cost = 0 if str1[i-1] == str2[j-1] else 1
                matrix[i][j] = min(matrix[i-1][j] + 1,
                                matrix[i][j-1] + 1,
                                matrix[i-1][j-1] + cost)
        
        return matrix[len_str1][len_str2]

    def find_most_similar(self, term):
        res = {}
        for word in self.words:
            x = self.levenshtein_distance(term, word)
            res[x] = word
        min_dict_key = min(res.keys())
        return res[min_dict_key]
        

fruits = Dictionary(['cherry', 'pineapple', 'melon', 'strawberry', 'raspberry'])
print(fruits.find_most_similar('berry'))