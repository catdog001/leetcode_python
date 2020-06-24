"""
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。

注意：你不能在买入股票前卖出股票。

示例 1:
输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。

示例 2:
输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""
解题思路：
dp[i]表示第i天获取的最大利润，其中，i为状态，dp[i]为状态变量
在第i天，有两个选择：卖或者不卖
如果卖的话，  获取的利润即为当前价格prices[i] - 在这一天之前的最低价格min_price
如果不卖的话， 获取的利润是前一天的利润，即为dp[i-1]
第i天获取的最大利润 = max(前一天的利润, 当前价格prices[i] - 在这一天之前的最低价格min_price)，这个就是最主要的状态转移方程。
那么现在问题就是，如何求解在第i天之前的最低价格min_price呢？
设置一个变量不断迭代就好了
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # dp[i]表示到第i天的最大利润是多少
        dp = [0 for _ in range(len(prices))]
        if not prices or len(prices) == 0:
            return 0
        min_price = float("inf")
        len_prices = len(prices)
        for buy in range(len_prices):
            min_price = min(min_price, prices[buy])
            dp[buy] = max(dp[buy-1], prices[buy] - min_price)
        return max(dp)
