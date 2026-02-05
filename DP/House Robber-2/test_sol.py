from sol import Solution
import sys

def test():
    s = Solution()
    
    # Test safe cases
    try:
        assert s.rob([2, 3, 2]) == 3
        print("Case [2, 3, 2] passed")
        assert s.rob([1, 2, 3, 1]) == 4
        print("Case [1, 2, 3, 1] passed")
        assert s.rob([1]) == 1
        print("Case [1] passed")
    except Exception as e:
        print(f"Failed on valid cases: {e}")

    # Test empty list
    try:
        res = s.rob([])
        print(f"Case [] passed with result: {res}")
    except IndexError:
        print("Caught expected IndexError on []")
    except Exception as e:
        print(f"Caught unexpected exception on []: {e}")

if __name__ == "__main__":
    test()
