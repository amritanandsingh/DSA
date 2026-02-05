class Solution:
    def fun(self,matrix,index,lastIndex):
        if index < 0:
            return 0
        fighting = 0
        running= 0
        stealth=0

        if lastIndex != 0:
            running = self.fun(matrix,index-1,0) + matrix[index][0]
        if lastIndex != 1:
            stealth = self.fun(matrix,index-1,1 ) + matrix[index][1]
        if lastIndex != 2:
            fighting = self.fun(matrix,index-1 , 2) + matrix[index][2]
        return max(running,stealth,fighting)
        
    def ninjaTraining(self, matrix):
        return self.fun(matrix,len(matrix)-1,-1)


obj=Solution()

from typing import List, Tuple
import random
from functools import lru_cache

# ---------- Oracles (expected answer calculators) ----------

def expected_dp(matrix: List[List[int]]) -> int:
    """Trusted O(n*3) DP oracle."""
    n = len(matrix)
    prev = matrix[0][:]  # [run, stealth, fight]
    for i in range(1, n):
        cur = [0, 0, 0]
        cur[0] = matrix[i][0] + max(prev[1], prev[2])
        cur[1] = matrix[i][1] + max(prev[0], prev[2])
        cur[2] = matrix[i][2] + max(prev[0], prev[1])
        prev = cur
    return max(prev)

def expected_bruteforce(matrix: List[List[int]]) -> int:
    """Exact oracle for small n by trying all valid schedules (no same consecutive)."""
    n = len(matrix)

    @lru_cache(None)
    def dfs(day: int, last: int) -> int:
        if day == n:
            return 0
        best = 0
        for act in range(3):
            if act != last:
                best = max(best, matrix[day][act] + dfs(day + 1, act))
        return best

    return dfs(0, -1)

def expected_oracle(matrix: List[List[int]]) -> int:
    """Use brute for small sizes, DP for larger sizes."""
    return expected_bruteforce(matrix) if len(matrix) <= 12 else expected_dp(matrix)


# ---------- Test Runner ----------

def check_case(obj, matrix: List[List[int]], expected: int, name: str = "") -> bool:
    got = obj.ninjaTraining(matrix)
    ok = (got == expected)
    prefix = f"[{name}] " if name else ""
    print(f"{prefix}Expected={expected}, Got={got}  ->  {'✅ Correct' if ok else '❌ Wrong'}")
    return ok

def run_all_tests(obj):
    # ----- Deterministic test suite (hand-picked) -----
    tests: List[Tuple[str, List[List[int]], int]] = [
        ("sample_1", [[10, 40, 70], [20, 50, 80], [30, 60, 90]], 210),
        ("sample_2", [[70, 40, 10], [180, 20, 5], [200, 60, 30]], 290),

        # "Now your turn!" from prompt
        ("prompt_quiz", [[20, 10, 10], [20, 10, 10], [20, 30, 10]], 60),

        # Edge: n=1
        ("n1_simple", [[5, 1, 4]], 5),
        ("n1_all_zero", [[0, 0, 0]], 0),
        ("n1_max", [[1000, 999, 998]], 1000),

        # Edge: n=2
        ("n2_choose_diff", [[10, 1, 1], [10, 1, 1]], 11),  # 10 + 1
        ("n2_all_equal", [[7, 7, 7], [7, 7, 7]], 14),

        # All zeros
        ("zeros_5days", [[0, 0, 0]] * 5, 0),

        # Always best is same activity -> must alternate with second best
        ("force_alternate", [[100, 1, 1], [100, 1, 1], [100, 1, 1]], 201),  # 100+1+100

        # Ties & symmetry
        ("ties_symmetry", [[5, 5, 1], [5, 5, 1], [5, 5, 1], [5, 5, 1]], 20),

        # Mixed, encourages switching
        ("mixed_1", [[8, 2, 6], [1, 9, 3], [7, 4, 5]], expected_oracle([[8,2,6],[1,9,3],[7,4,5]])),
        ("mixed_2", [[3, 10, 3], [10, 3, 3], [3, 3, 10], [10, 3, 3]], expected_oracle([[3,10,3],[10,3,3],[3,3,10],[10,3,3]])),

        # Large values, avoid consecutive traps
        ("trap_consecutive", [[1000, 0, 0], [1000, 1, 1], [1000, 0, 0]], 2001),
    ]

    passed = 0
    for name, matrix, expected in tests:
        passed += check_case(obj, matrix, expected, name)

    print(f"\nDeterministic: {passed}/{len(tests)} passed\n")

    # ----- Random small tests (validated by brute force) -----
    random.seed(0)
    rand_passed = 0
    R = 200
    for i in range(R):
        n = random.randint(1, 10)
        matrix = [[random.randint(0, 30) for _ in range(3)] for _ in range(n)]
        expected = expected_bruteforce(matrix)
        got = obj.ninjaTraining(matrix)
        ok = (got == expected)
        rand_passed += ok
        if not ok:
            print(f"❌ Random test failed at #{i}")
            print("matrix =", matrix)
            print("expected =", expected, "got =", got)
            break

    print(f"Random(bruteforce-checked): {rand_passed}/{R} passed")


# ---------- Example usage ----------
# class Solution:
#     def ninjaTraining(self, matrix: List[List[int]]) -> int:
#         ...
#
# obj = Solution()
run_all_tests(obj)
