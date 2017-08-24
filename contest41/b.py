class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        start_stack = []
        res = [0]*n
        for alog in logs:
            id, act, time = alog.split(':')
            id = int(id)
            time = int(time)
            if act == "start":
                start_stack.append((id,time))
            elif act == "end":
                i,start_time = start_stack.pop()
                res[i] += time - start_time + 1

                if start_stack:
                    j, _ = start_stack[-1]
                    res[j] -= time - start_time + 1

        return res
s = Solution()
print s.exclusiveTime(8,
["0:start:0","1:start:5","2:start:6","3:start:9","4:start:11",
 "5:start:12","6:start:14","7:start:15","1:start:24","1:end:29",
 "7:end:34","6:end:37","5:end:39","4:end:40","3:end:45","0:start:49",
 "0:end:54","5:start:55","5:end:59","4:start:63","4:end:66",
 "2:start:69","2:end:70","2:start:74","6:start:78","0:start:79",
 "0:end:80","6:end:85","1:start:89","1:end:93","2:end:96","2:end:100",
 "1:end:102","2:start:105","2:end:109","0:end:114"])