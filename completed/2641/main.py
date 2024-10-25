from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        node_id = 0
        parent_id = -1
        depth = 0
        level_sums = defaultdict(int)
        level_sums[depth] = root.val
        level_db = defaultdict(int)
        level_db[(depth, parent_id)] = root.val
        q = deque([(root, depth, node_id, parent_id)])
        #print(level_sums, level_db)
        while q:
            node, depth, current_node_id, parent_id = q.popleft()
            #print(current_node_id)
            #print(level_sums[depth], level_db[(depth, parent_id)], depth, node_id, parent_id)
            node.val = level_sums[depth] - level_db[(depth, parent_id)]
            #print(node.val)
            parent_id = current_node_id
            #print(node.val)
            if node.left:
                node_id += 1
                q.append((node.left, depth + 1, node_id, parent_id))
                level_db[(depth + 1, parent_id)] += node.left.val
                level_sums[depth + 1] += node.left.val
            if node.right:
                node_id += 1
                q.append((node.right, depth + 1, node_id, parent_id))
                level_db[(depth + 1, parent_id)] += node.right.val
                level_sums[depth + 1] += node.right.val
        print(binary_tree_to_bfs_list(root))
        return root

if __name__ == '__main__':
    sol = Solution()
    input1 = bfs_list_to_binary_tree([5,4,9,1,10,null,7])  # [0,0,0,7,7,null,11]
    input2 = bfs_list_to_binary_tree([3,1,2])  # [0,0,0]
    input3 = bfs_list_to_binary_tree([33,37,42,null,null,null,46])  # [0,0,0,null,null,null,0]
    input4 = bfs_list_to_binary_tree([5319,2884,9195,4221,3939,5083,7127,238,8779,null,null,3034,5047,6666,2672,null,null,6724,5916,4862,190,3802,8669,8201,7507,8898,4167,232,9924,4664,3877,3805,null,8092,4725,8552,7622,2285,null,9680,4481,306,762,2096,5269,null,null,5606,8594,4365,7981,8547,8903,8146,null,3976,6713,2141,2858,8423,null,2846,9714,7515,2974,null,2719,7003,3437,8262,6556,7296,9277,2886,9370,null,2188,3192,9943,8613,null,null,null,null,7807,1410,7099,null,null,null,null,null,null,6604,9051,8122,null,5490,898,2681,5022,8070,2322,null,1245,null,1686,5506,5809,2177,7026,null,null,2396,8679,8330,4565,4548,491,9315,3873,9083,6583,2481,305,9116,4976,5813,5503,null,9940,4006,null,null,null,8883,null,null,2135,null,3484,null,null,3473,1309,null,null,null,null,null,null,4273,null,null,null,null,8387,3169,4849,7500,196,5501,null,null,82,9761,9337,8628,5933,8459,null,null,6762,null,5854,7512,2709,9627,2648,null,null,5000,4181,4579,6384,1615,4206,null,null,946,3661,4238,2408,2395,2582,9908,3848,7569,null,6518,8095,2754,1379,9568,839,null,null,982,7040,null,null,null,null,null,null,null,null,5562,5039,8332,818,null,9780,null,null,null,null,null,7983,null,5692,2333,7267,null,null,null,null,8318,8,809,6125,7828,null,null,null,null,null,null,7549,4364,null,null,null,9848,1585,6418,8178,null,6034,3757,8847,8131,null,9014,8021,725,9597,4301,9175,6104,1999,9694,9973,8471,7284,6846,3420,7527,5684,4569,null,3499,3691,7173,9314,4337,3863,null,3197,9347,8138,9002,9463,null,null,7935,1204,1192,null,null,null,5725,null,1166,9161,3643,null,null,null,null,8970,null,null,null,1813,null,7038,null,5073,null,null,1389,8468,null,null,278,3137,null,2493,239,null,null,null,null,null,null,null,null,788,null,1183,3506,null,431,8787,null,null,null,null,1121,null,null,null,null,3141,null,null,null,null,3429,4564,5028,null,8778,2790,5818,1749,2326,6257,3862,2205,2399,8652,9240,3231,9272,1808,4068,9273,8707,2624,null,null,5175,9424,5857,2177,7261,1461,3078,3694,null,3960,4883,7223,null,null,4105,null,833,4738,9900,null,5037,null,5166,500,null,5242,4550,7609,null,null,null,null,null,null,null,null,null,null,null,null,null,null,1431,null,null,null,151,9513,5172,4888,null,9283,7890,null,1896,7189,null,null,null,null,7272,null,null,null,6617,5047,7510,null,null,null,null,null,null,3728,null,null,null,null,null,null,null,5586,9052,9899,5347,2308,467,5261,248,7931,5401,8829,5961,7427,1136,null,700,null,3224,null,5013,5534,2663,5299,2029,8040,4195,null,2863,8544,7745,null,null,null,9936,null,6146,null,6652,2527,4083,1311,1565,9253,178,4856,null,2623,null,null,null,6124,1351,null,9791,8507,null,null,null,2494,9602,1226,null,1845,null,7973,3157,5466,9687,5429,null,null,null,null,5556,551,null,null,null,9605,5229,null,6839,3104,null,9145,null,6110,null,null,null,null,8296,7122,null,null,4307,7563,7751,2718,9558,null,null,null,7189,null,211,3031,null,4411,9453,1974,5461,7142,534,9063,178,9724,8550,3476,7259,5785,7282,1677,7285,5116,null,null,3299,4322,null,null,57,null,null,4554,null,null,2958,null,5842,null,8857,9797,8557,6607,8655,194,null,null,3074,null,6872,null,null,null,7753,575,null,null,4332,4646,3171,null,9467,1372,2423,5653,null,null,null,null,5733,null,1678,5088,3075,null,null,null,null,3783,null,null,null,null,null,null,null,null,8709,null,null,null,null,null,null,null,null,null,null,5640,6887,6864,null,1578,null,null,null,4483,4706,9229,975,null,null,null,6895,6642,2302,null,null,6067,null,2771,1215,8272,null,null,743,null,5544,null,null,null,497,null,null,665,null,7077,9222,null,null,null,null,9788,744,4026,8000,2265,5971,7631,4394,3870,8116,5516,null,3667,4787,665,9453,8961,null,8696,3526,1933,null,null,6328,1255,7920,1245,3165,1477,7964,null,6976,4034,null,null,null,961,null,null,2313,null,null,7566,1648,8991,null,1463,null,9202,7075,1750,6797,6235,null,null,3461,null,null,6860,null,2423,null,7644,null,null,7108,null,null,4379,7465,5158,null,null,5702,4163,8879,3872,null,null,null,394,null,null,7630,null,null,9466,null,null,null,3259,null,null,null,null,4026,null,4603,158,8835,8405,null,null,null,7426,null,6302,8994,4731,null,null,null,null,1984,4130,null,null,381,null,6309,4999,null,null,null,9526,null,null,null,null,null,6114,null,null,8963,null,3657,2517,1560,3518,3029,null,3040,null,8750,5360,null,null,8031,9962,null,5339,5878,3233,4472,null,1384,null,1233,5687,null,null,null,1617,1241,8139,159,null,3219,1698,9979,6121,null,null,3067,3087,null,3558,null,7517,null,null,2523,null,6544,6653,null,null,null,null,null,null,null,null,7853,9248,null,7042,6075,3863,null,null,null,808,5017,null,null,null,3369,3209,8140,3463,null,7136,null,4508,null,null,null,7982,null,6053,null,null,4930,5650,7415,4351,null,null,919,null,8626,3469,null,null,null,null,8339,null,5395,8513,null,null,null,5687,null,null,6278,null,null,null,9827,8488,null,null,null,6060,null,null,5810,763,null,null,7576,null,null,null,9128,null,null,null,2548,6261,2148,null,null,null,null,8094,6234,1763,null,null,null,null,null,null,null,null,184,null,4270,null,null,null,null,null,null,null,null,null,9139,6586,null,1326,null,4838,7453,null,null,3755,7358,5667,null,null,3204,4561,null,null,null,5495,901,442,8674,3866,2882,5518,340,null,4579,2346,null,null,7141,null,null,null,null,null,null,null,null,null,null,null,null,7516,null,988,8938,null,null,null,null,1031,null,6165,null,4521,null,null,null,null,4995,null,null,null,null,null,8378,null,4708,1987,3459,null,null,null,8387,null,null,null,null,null,null,null,6764,5535,null,null,null,null,1756,null,null,null,null,null,null,null,6210,null,7398,null,null,null,null,null,8906,163,null,5191,9728,2758,1278,4582,9533,1778,null,null,1272,3163,5556,null,471,3832,null,null,null,null,2096,null,null,null,null,7983,3972,6546,null,1219,3400,2375,null,null,null,null,5301,8263,null,null,9789,2456,null,6031,null,565,null,null,null,690,null,null,null,null,1644,null,null,7598,null,null,null,null,null,null,null,null,7668,null,null,null,1298,null,null,null,null,null,4844,null,null,7099,null,7594,null,null,null,null,null,null,null,null,null,null,null,null,null,null,1022,null,6067,9182,null,null,1401,null,7898,null,null,null,null,null,null,5744,null,6069,3161,5640,null,7151,null,null,3639,7072,9756,5940,9554,null,2538,null,null,null,1802,8163,6590,9630,null,null,null,1911,null,null,null,null,null,null,null,null,null,null,null,7015,null,null,null,null,null,null,8442,null,null,null,8409,5791,3480,null,null,null,8735,null,null,null,9201,null,4696,6022,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,1807,null,null,4728,9690,null,8814,null,null,null,null,null,6342,null,null,null,2564,null,2744,null,null,null,null,null,null,4430,4471,9813,1643,null,null,null,8828,null,null,2933,7417,null,null,null,null,null,null,null,2434,7106,null,null,null,null,1279,null,null,178,null,5437,null,8369,906,null,4969,null,null,null,null,null,null,null,5140])
    input5 = bfs_list_to_binary_tree([436,623,376,117,698,467,818,52,543,880,577,700,568,361,null,616,null,232,656,565,12,null,95,null,null,null,389,830,null,276,null,715,null,144,null,317,null,null,91,null,null,null,null,null,null,129,362,487,272,275,null,null,908,559,null,null,null,null,null,862,null,null,null,null,68,63,null,467,null,274,null,null,null,null,null,920,null,300])
    print(sol.replaceValueInTree(input1))
    print(sol.replaceValueInTree(input2))
    print(sol.replaceValueInTree(input3))
    #print(sol.replaceValueInTree(input4))
    #print(sol.replaceValueInTree(input5))
