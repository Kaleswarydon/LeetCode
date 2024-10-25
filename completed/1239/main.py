from icecream import ic as print

def print_matrix(m):
    for x in m:
        print(x)
class Solution:
    def maxLength(self, arr: list[str]) -> int:
        res = [{}]
        for x in arr:
            if not len(set(x)) < len(x):
                tmp = set(x)
                for tmp2 in res:
                    if not tmp.intersection(tmp2):
                        res.append(tmp.union(tmp2))
        return len(sorted(res, key=lambda y: len(y))[-1])

if __name__ == '__main__':
    sol = Solution()
    arr1 = ["un","iq","ue"]
    arr2 = ["cha","r","act","ers"]
    arr3 = ["abcdefghijklmnopqrstuvwxyz"]
    arr4 = ["aa","bb"]
    arr5 = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p"]
    arr6 = ["ab","ba","cd","dc","ef","fe","gh","hg","ij","ji","kl","lk","mn","nm","op","po"]
    arr7 = ["abcdefghijklm","bcdefghijklmn","cdefghijklmno","defghijklmnop","efghijklmnopq","fghijklmnopqr","ghijklmnopqrs","hijklmnopqrst","ijklmnopqrstu","jklmnopqrstuv","klmnopqrstuvw","lmnopqrstuvwx","mnopqrstuvwxy","nopqrstuvwxyz","opqrstuvwxyza","pqrstuvwxyzab"]
    arr8 = ["jnfbyktlrqumowxd","mvhgcpxnjzrdei"]
    arr9 = ["nytozalihusjd","mi"]
    arr10 = ["a", "abc", "d", "de", "def"]
    print(sol.maxLength(arr1))
    print(sol.maxLength(arr2))
    print(sol.maxLength(arr3))
    print(sol.maxLength(arr4))
    print(sol.maxLength(arr5))
    print(sol.maxLength(arr6))
    print(sol.maxLength(arr7))
    print(sol.maxLength(arr8))
    print(sol.maxLength(arr9))
    print(sol.maxLength(arr10))