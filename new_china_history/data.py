from datetime import *
from ttime_diff import *

DICT_SECRETRY = {}
DICT_SECRETRY[date(1921, 7, 1)] = '陈独秀'
DICT_SECRETRY[date(1928, 7, 1)] = '向忠发'
DICT_SECRETRY[date(1931, 7, 1)] = '王明'
DICT_SECRETRY[date(1934, 1, 1)] = '博古'
DICT_SECRETRY[date(1935, 1, 1)] = '张闻天'
DICT_SECRETRY[date(1945, 6, 19)] = '毛泽东'
DICT_SECRETRY[date(1976, 10, 7)] = '华国锋'
DICT_SECRETRY[date(1981, 6, 29)] = '胡耀邦'
DICT_SECRETRY[date(1987, 1, 16)] = '赵紫阳'
DICT_SECRETRY[date(1989, 6, 24)] = '江泽民'
DICT_SECRETRY[date(2002, 11, 15)] = '胡锦涛'
DICT_SECRETRY[date(2012, 11, 14)] = '习近平'

TUP_SECRETRY = (date(1921, 7, 1), \
             date(1928, 7, 1), \
                date(1931, 7, 1), \
                    date(1934, 1, 1), \
                        date(1935, 1, 1), \
                            date(1945, 6, 19), \
                                date(1976, 10, 7), \
                                    date(1981, 6, 29), \
                                        date(1987, 1, 16), \
                                            date(1989, 6, 24), \
                                                date(2002, 11, 15), \
                                                    date(2012, 11, 14), \
                                                        date(2032, 11, 14))

DICT_CHAIRMAN = {}
DICT_CHAIRMAN[date(1921, 7, 1)] = ''
DICT_CHAIRMAN[date(1931, 11, 27)] = '毛泽东'
DICT_CHAIRMAN[date(1937, 9, 6)] = ''
DICT_CHAIRMAN[date(1949, 9, 1)] = '毛泽东'
DICT_CHAIRMAN[date(1959, 4, 1)] = '刘少奇'
DICT_CHAIRMAN[date(1969, 11, 12)] = ''
DICT_CHAIRMAN[date(1983, 6, 1)] = '李先念'
DICT_CHAIRMAN[date(1988, 4, 1)] = '杨尚昆'
DICT_CHAIRMAN[date(1993, 3, 1)] = '江泽民'
DICT_CHAIRMAN[date(2003, 3, 1)] = '胡锦涛'
DICT_CHAIRMAN[date(2013, 3, 1)] = '习近平'
DUP_CHAIRMAN = (date(1921, 7, 1), \
                date(1931, 11, 27), \
                    date(1937, 9, 6), \
                        date(1949, 9, 1), \
                            date(1959, 4, 1), 
                                date(1969, 11, 12), \
                                    date(1983, 6, 1), \
                                        date(1988, 4, 1), \
                                            date(1993, 3, 1), \
                                                date(2003, 3, 1), \
                                                    date(2013, 3, 1), \
                                                        date(2033, 3, 1))

DICT_MILITARY = {}
DICT_MILITARY[date(1921, 7, 1)] = ''
DICT_MILITARY[date(1949, 10, 1)] = '毛泽东'
DICT_MILITARY[date(1976, 10, 1)] = '华国锋'
DICT_MILITARY[date(1981, 6, 1)] = '邓小平'
DICT_MILITARY[date(1990, 3, 19)] = '江泽民'
DICT_MILITARY[date(2005, 3, 8)] = '胡锦涛'
DICT_MILITARY[date(2013, 3, 14)] = '习近平'
DUP_MILITARY = (date(1921, 7, 1), \
                date(1949, 10, 1), \
                 date(1976, 10, 1), \
                 date(1981, 6, 1), \
                 date(1990, 3, 19), \
                 date(2005, 3, 8), \
                 date(2013, 3, 14),\
                date(2033, 3, 14))
DICT_PRIME = {}
DICT_PRIME[date(1921, 7, 1)] = ''
DICT_PRIME[date(1931, 11, 27)] = '毛泽东'
DICT_PRIME[date(1934, 2, 3)] = '张闻天'
DICT_PRIME[date(1937, 9, 6)] = ''
DICT_PRIME[date(1949, 10, 1)] = '周恩来'
DICT_PRIME[date(1976, 2, 2)] = '华国锋'
DICT_PRIME[date(1980, 9, 10)] = '赵紫阳'
DICT_PRIME[date(1987, 11, 24)] = '李鹏'
DICT_PRIME[date(1998, 3, 17)] = '朱镕基'
DICT_PRIME[date(2003, 3, 16)] = '温家宝'
DICT_PRIME[date(2013, 3, 15)] = '李克强'
DICT_PRIME[date(2023, 3, 11)] = '李强'
DUP_PRIME = (date(1921, 7, 1), \
             date(1931, 11, 27), \
                date(1934, 2, 3),\
                    date(1937, 9, 6), \
                        date(1949, 10, 1), \
                            date(1976, 2, 2), \
                                date(1980, 9, 10), \
                                    date(1987, 11, 24), \
                                        date(1998, 3, 17), \
                                            date(2003, 3, 16), \
                                                date(2013, 3, 15), \
                                                   date(2023, 3, 11), \
                                                        date(2033, 3, 11))
DICT_STATE = {}
DICT_STATE[date(1921, 7, 1)] = ''
DICT_STATE[date(1931, 11, 7)] = '中华苏维埃共和国'
DICT_STATE[date(1937, 9, 6)] = ''
DICT_STATE[date(1949, 10, 1)] = '中华人民共和国'
DUP_STATE = (date(1921, 7, 1), \
             date(1931, 11, 7), \
                date(1937, 9, 6), \
                    date(1949, 10, 1), \
                        date(2033, 3, 11))
color = ('red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'purple')

#历史的开始
begin = date(1921, 7, 1)
#现在
end = date(2023, 7, 1)