class LogSystem(object):
    def __init__(self):
        self.data = []
        self.time_map = dict(Year=0,
                        Month=1,
                        Day=2,
                        Hour=3,
                        Minute=4,
                        Second=5)

    def put(self, id, timestamp):
        """
        :type id: int
        :type timestamp: str
        :rtype: void
        """
        self.data.append((timestamp, id))

    def retrieve(self, s, e, gra):
        """
        :type s: str
        :type e: str
        :type gra: str
        :rtype: List[int]
        """
        s_split = s.split(':')
        e_split = e.split(':')

        index = self.time_map[gra]
        new_s = ':'.join(s_split[0:index+1])
        new_e = ':'.join(e_split[0:index+1])

        # self.data.sort()
        ret = []
        for timestamp, id in self.data:
            timestamp_split = timestamp.split(':')
            new_timestamp = ':'.join(timestamp_split[0:index + 1])
            if new_s <= new_timestamp <= new_e:
                ret.append(id)

        return ret

s= LogSystem()
s.put(1, "2017:01:01:23:59:59")
s.put(2, "2017:01:01:22:59:59")
s.put(3, "2016:01:01:00:00:00")
print s.retrieve("2016:01:01:01:01:01","2017:01:01:23:00:00","Year")
print s.retrieve("2016:01:01:01:01:01","2017:01:01:23:00:00","Hour")