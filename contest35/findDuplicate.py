class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        from collections import defaultdict
        contents_to_path = defaultdict(list);
        for item in paths:
            l = item.split()
            path = l[0]
            for files in l[1:]:
                l2 = files.split('(')
                file_name = l2[0]
                file_content = l2[1][:-1]
                contents_to_path[file_content].append(path+'/'+file_name)

        ret = []
        for foo, file_list in contents_to_path.iteritems():
            if len(file_list) > 1:
                ret.append(file_list)
        return ret



s = Solution()
print s.findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"])