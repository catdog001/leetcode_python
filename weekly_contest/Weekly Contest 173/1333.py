"""
problem： https://leetcode.com/contest/weekly-contest-173/problems/filter-restaurants-by-vegan-friendly-price-and-distance/
题目大意：
给定一个list[list[int]], 分别代表含义是[id, rating, veganFriendly, price, distance]，给定veganFriendly, maxprice, maxdistance
筛选出满足以下条件的id列表，并将id列表按rating、id降序排列：
veganFriendly=1，则veganFriendly相等且距离、价格不超过最大距离、最高价格
veganFriendly=1，则距离、价格不超过最大距离、最高价格
"""


class Solution(object):
    def filterRestaurants(self, restaurants, veganFriendly, maxPrice, maxDistance):
        """
        :type restaurants: List[List[int]]
        :type veganFriendly: int
        :type maxPrice: int
        :type maxDistance: int
        :rtype: List[int]
        """
        "[id=1, rating=4, veganFriendly=1, price=40, distance=10]"
        result = {}
        results = {}
        for restaurant in restaurants:
            if veganFriendly == 1 and restaurant[2] == veganFriendly and restaurant[3] <= maxPrice and  restaurant[4] <= maxDistance:
                result.update({restaurant[0]:restaurant[1]})
            if veganFriendly == 0 and restaurant[2] in [0,1] and restaurant[3] <= maxPrice and  restaurant[4] <= maxDistance:
                result.update({restaurant[0]:restaurant[1]})

        result_value = sorted(result.values())[::-1]
        for value in result_value:
            for key in result.keys():
                if result.get(key) == value:
                    "可能会产生同一个value对应的id"
                    results.update({key:value})

        """
        L = [(12, 12), (34, 13), (32, 15), (12, 24), (32, 64), (32, 11)]
        L.sort(key=lambda x: (x[0], -x[1]))
        
        student_1={
        'a':2,
        'b':4,
        'c':6,
        'd':8
        }

        student_1_sort = sorted(student_1.iteritems(), key=lambda d: d[1], reverse=True)
        print(student_1_sort)
        
        """
        results_sort = sorted(results.iteritems(), key=lambda x:(-x[1],-x[0]))
        return list([key[0] for key in results_sort])