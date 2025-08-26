class Solution:
    def largestGoodInteger(self, num: str) -> str:
        datasets = ['000', '111', '222', '333', '444', '555', '666', '777', '888', '999']

        result = ""

        for data in datasets:
            if data in num:
                result = data
        
        return result