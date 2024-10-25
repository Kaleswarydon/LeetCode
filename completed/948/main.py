from icecream import ic as print

class Solution:
    def dummy(self, tokens, power):
        tokens.sort()
        pointer_low = 0
        pointer_high = len(tokens) - 1
        max_score = 0
        score = 0
        while pointer_low <= pointer_high:
            if power >= tokens[pointer_low]:
                power -= tokens[pointer_low]
                score += 1
                if score > max_score:
                    max_score = score
                pointer_low += 1
            elif score > 0:
                power += tokens[pointer_high]
                score -= 1
                pointer_high -= 1
            else:
                break
            print(pointer_low, pointer_high, power, score)
        return max_score

if __name__ == '__main__':
    sol = Solution()
    input1 = [100], 50
    input2 = [200,100], 150
    input3 = [100,200,300,400], 200
    print(sol.dummy(*input1))
    print(sol.dummy(*input2))
    print(sol.dummy(*input3))
