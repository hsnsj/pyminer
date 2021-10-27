# map_blocks = {'01-beijing': [1505],
#                '02-shanghai': [171, 56, 10, 512, 10, 45, 25, 11, 9],
#                '03-tianjin': [1280, 6],
#                '04-chongqing': [5552],
#                '05-heilongjiang': [7192],
#                '06-neimeng': [11665],
#                '07-xinjiang': [8599],
#                '08-jilin': [5108, 10, 10, 8, 15, 11],
#                '09-gansu': [10478, 96, 24],
#                '10-liaoning': [5281, 11, 6, 11, 16, 8, 8, 6, 9, 8, 7, 11, 7, 11, 12, 12, 9, 26, 20, 11, 9, 8, 10,
#                                9, 9, 15, 8, 9, 7, 22, 9, 8, 9, 113, 16, 11, 6, 8, 9, 10, 9, 8, 9, 13, 40, 5, 10,
#                                9, 13, 5, 4, 6, 8, 21, 17, 10, 14, 11, 10, 11, 15, 61, 13, 23, 17, 9, 8, 9, 48,
#                                18, 9, 16, 16, 14, 10, 47, 14, 10, 20, 14, 32, 9, 12, 53, 16, 12, 11, 22, 15,
#                                33, 7, 10, 12, 9, 20, 9, 14, 11, 6, 6, 5, 9],
#                '11-hebei': [7303, 319, 9, 13, 13, 7, 11, 6, 7, 8, 27, 8, 11, 7, 11, 8, 6, 8, 8, 13, 8, 10, 8, 8, 19],
#                '12-shanxi': [4056],
#                '13-shan3xi': [6633],
#                '14-ningxia': [3752, 96, 24],
#                '15-qinghai': [10868],
#                '16-shandong': [17, 21, 17, 29, 11, 6756, 17, 15, 9, 28, 11, 7, 8, 16, 7, 4, 13, 7, 10, 8, 9, 13,
#                                23, 8, 8, 11, 8, 9, 9, 11, 13, 12, 12, 20, 9, 8, 21, 20, 18, 31, 17, 5, 16, 14,
#                                10, 17, 10, 21, 29, 11, 11, 10, 9, 9, 11, 7, 11, 23, 11, 13, 10, 10, 9, 13, 12,
#                                5, 5, 14, 18, 11, 11, 10, 12, 13, 6, 15, 8, 13, 18, 10, 11, 10, 10, 12, 24, 12,
#                                9, 11, 9, 4, 13, 8, 11, 17, 12, 12, 13, 16, 12, 9, 24, 10, 10, 6, 17, 12, 14,
#                                11, 14, 18, 31, 11, 8, 9, 11, 9, 9],
#                '17-henan': [6050, 14, 18],
#                '18-xizang': [9027],
#                '19-jiangsu': [5734, 8, 7, 14, 8, 9, 42, 60],
#                '20-anhui': [7298],
#                '21-sichuan': [9923],
#                '22-hubei': [7100, 18, 14, 19],
#                '23-zhejiang': [3456, 12, 11, 11, 10, 16, 9, 9, 9, 10, 9, 8, 9, 8, 36, 14, 16, 8, 8, 11, 15, 12,
#                                9, 9, 13, 8, 12, 10, 10, 8, 6, 9, 6, 10, 11, 9, 11, 7, 7, 10, 9, 10, 6, 9, 6, 8,
#                                11, 9, 7, 7, 7, 7, 63, 10, 13, 10, 8, 9, 8, 7, 25, 48, 11, 8, 7, 7, 7, 12, 51,
#                                22, 8, 8, 8, 7, 7, 7, 9, 11, 6, 8, 9, 8, 9, 8, 8, 15, 20, 10, 16, 26, 114, 9,
#                                10, 9, 9, 11, 18, 10, 8, 35, 7, 10, 20, 26, 8, 12, 9, 11, 13, 7, 9, 55, 8, 19,
#                                14, 10, 8, 12, 17, 11, 35, 12, 17, 8, 7, 10, 59, 10, 26, 11, 9, 20, 8, 6, 5,
#                                13, 11, 7, 11, 9, 9, 8, 9, 13, 9, 10, 12, 9, 10, 9, 9, 9, 8, 8, 13, 31, 10,
#                                10, 9, 26, 13, 9, 15, 43, 8, 26, 12, 26, 20, 11, 20, 10, 5, 5, 11, 5, 4, 16,
#                                5, 21, 4, 13, 14, 15, 6, 5, 8, 17, 6, 20, 9, 14, 5, 5, 6, 15, 10, 5, 8, 16,
#                                12, 5, 4, 4, 6, 9, 12, 4, 17, 5, 5, 6, 68, 16, 4, 9, 13, 16, 4, 5, 21, 14,
#                                28, 35, 20, 8, 6, 30, 43, 10, 34, 8, 11, 8, 7, 15, 12, 10, 10, 8, 10, 12,
#                                18, 14, 11, 27, 10, 12, 12, 11, 5, 5, 5, 5, 4, 5, 16, 10, 40, 10, 12, 14,
#                                22, 10, 8, 27, 21, 5, 5, 5, 6],
#                '24-jiangxi': [4601],
#                '25-hunan': [6281, 69, 19, 16],
#                '26-guizhou': [4845, 16, 69],
#                '27-yunnan': [6872],
#                '28-fujian': [5761, 8, 10, 8, 11, 10, 9, 15, 10, 11, 18, 16, 10, 29, 12, 12, 26, 6, 5, 11, 15,
#                              9, 5, 10, 10, 9, 14, 22, 10, 7, 10, 16, 8, 9, 20, 13, 8, 25, 10, 12, 15, 44, 10,
#                              14, 7, 10, 10, 6, 26, 11, 27, 5, 5, 12, 7, 11, 12, 40, 13, 5, 7, 10, 6, 14, 7,
#                              11, 8, 9, 11, 6, 14, 5, 5, 10, 27, 35, 23, 6, 6, 12, 30, 9, 5, 12, 8, 6, 10,
#                              12, 6, 6, 7, 8, 6, 9, 226, 25, 29, 6, 13, 21, 7, 6, 6, 6, 12, 7, 8, 6, 10, 7,
#                              8, 8, 9, 6, 6, 7, 11, 6, 9, 13, 9, 23, 8, 6, 6, 14, 7, 25, 6, 6, 8, 5, 8, 12,
#                              7, 9, 9, 7, 96, 6, 7, 6, 8, 8, 7, 9, 7, 6, 7, 6, 7, 43, 8, 9, 9, 8, 6, 9, 10,
#                              9, 7, 13, 10, 6, 7, 8, 120, 9, 7, 35, 6, 5, 26, 10, 39, 17, 6, 19, 9, 13, 6,
#                              10, 6, 6, 9, 6, 8, 7, 6, 7, 7, 4, 6, 11, 9, 9, 6, 9],
#                '29-guangxi': [5952, 20, 6, 33, 21, 7, 6, 11, 30, 10],
#                '30-guangdong': [7371, 16, 12, 7, 5, 10, 9, 75, 8, 8, 4, 9, 9, 8, 7, 8, 9, 8, 10, 12, 6, 10, 9,
#                                 9, 8, 9, 6, 9, 20, 6, 47, 14, 5, 9, 8, 7, 9, 7, 9, 9, 9, 8, 7, 10, 10, 10, 10,
#                                 10, 9, 13, 10, 8, 9, 9, 10, 7, 7, 14, 17, 8, 9, 5, 7, 9, 8, 8, 20, 8, 8, 11,
#                                 34, 18, 9, 10, 7, 9, 13, 8, 79, 9, 69, 14, 16, 11, 7, 10, 9, 7, 11, 7, 14, 12,
#                                 8, 9, 8, 11, 25, 11, 12, 9, 9, 9, 9, 8, 18, 18, 14, 9, 26, 7, 19, 9, 7, 7, 9,
#                                 7, 18, 9, 9, 21, 55, 7, 14, 15, 8, 8, 6, 18, 8, 5, 22, 33, 13, 7, 9, 9, 8, 14,
#                                 10, 9, 8, 9, 9, 9, 13, 9, 154, 9, 8, 11, 11, 8, 9, 102, 12, 11, 21, 8, 9, 8,
#                                 11, 17, 8, 10, 8, 14, 10, 14, 8, 6, 7, 9, 6, 8, 9, 9, 9, 9, 8, 9, 8, 11, 81,
#                                 11, 11, 18, 11, 8, 15, 16, 50, 5, 17, 5, 75, 10, 9, 9, 11, 16, 14, 11, 11, 9,
#                                 46, 9, 10, 7, 21, 24],
#                '31-taiwan': [9, 10, 9, 10, 10, 10, 7, 9, 7, 12, 11, 894, 7, 21, 19, 8, 8, 32, 12, 8, 14, 143,
#                              7, 18, 46, 8, 22, 28, 15, 18, 9, 16, 9, 23, 13, 20, 8, 10, 9, 16, 5, 12, 6, 20,
#                              8, 12, 17, 12, 17, 9, 21, 22, 18, 20, 15, 39, 16, 8, 8],
#                '32-xianggang': [1523, 5, 62, 21, 9, 22, 36, 8, 12, 23, 8, 8, 12, 9, 16, 8, 63, 15, 8, 23, 46,
#                                 24, 9, 426, 6, 17, 9, 14, 8, 11, 8, 10, 27, 34, 12, 230, 24, 8, 9, 10, 9, 10,
#                                 13, 15, 12, 25, 28, 19, 129, 8, 8, 6, 8, 45, 8, 11, 13, 11, 19, 6, 25, 7, 45,
#                                 7, 7, 32],
#                '33-aomen': [79, 269, 10],
#                '34-hainan': [1379, 14, 8, 15, 8, 8, 9, 10, 28, 8, 10, 15, 14, 15, 10, 16, 7, 5, 6, 9, 10, 11,
#                              9, 5, 8, 8, 8, 7, 8, 9, 58, 13, 32, 24, 15, 14, 13, 18, 19, 16, 9, 8, 39, 8, 16,
#                              7, 21, 8, 23, 13, 27, 12, 12, 10, 37, 27, 59, 64, 15, 29, 12, 36, 11, 13, 12, 8,
#                              8, 8, 14, 7, 8, 10, 7, 6, 7, 6, 10, 81, 9, 9, 11, 133, 13, 11, 9, 11, 12, 13, 6,
#                              11, 19, 8, 11, 14, 18, 8, 8, 8, 14, 11, 12, 25, 19, 20, 13, 12, 15, 9, 11, 18, 7,
#                              8, 16, 18, 10, 9, 8, 9, 11, 13, 10, 12, 16, 9, 9, 11, 25, 15, 10, 14, 14, 32, 8,
#                              14, 11, 10, 11, 11, 10, 24, 12, 12, 12, 14, 8, 30, 10, 31, 10, 14, 14, 14, 44, 13,
#                              17, 11, 11, 12, 10, 8, 11, 11, 14, 12, 12, 10, 14, 12, 34, 10, 12, 13, 12, 7, 7,
#                              7, 20, 14, 11, 9, 8, 10, 9, 7, 13, 13, 8, 10, 16, 23, 21, 8, 12, 20, 13, 16, 17,
#                              13, 28, 11, 23, 30, 23, 8, 19, 22, 40, 33, 16, 23, 37, 15, 14, 17, 8, 8, 10, 38,
#                              76, 21, 23, 21, 36, 29, 13, 15, 13, 29, 11, 50, 18, 10, 16, 10, 11, 13, 21, 9, 15,
#                              39, 9, 15, 9, 12, 9, 13, 7, 10, 8, 10, 7, 14, 10, 13, 13, 9, 10, 28, 24, 22],
#                '39-jiuduan': [2, 2, 27, 27, 20, 26, 26, 25, 24, 20]}
#
# city_name={'beijing': '北京', 'shanghai': '上海', 'tianjin': '天津', 'chongqing': '重庆',
#            'heilongjiang': '黑龙江', 'neimenggu': '内蒙古', 'xinjiang': '新疆', 'jilin': '吉林',
#            'gansu': '甘肃', 'liaoning': '辽宁', 'hebei': '河北', 'shanxi': '山西',
#            'shan3xi': '陕西', 'ningxia': '宁夏', 'qinghai': '青海', 'shandong': '山东',
#            'henan': '河南', 'xizang': '西藏', 'jiangsu': '江苏', 'anhui': '安徽',
#            'sichuan': '四川', 'hubei': '湖北', 'zhejiang': '浙江', 'jiangxi': '江西',
#            'hunan': '湖南', 'guizhou': '贵州', 'yunnan': '云南', 'fujian': '福建',
#            'guangxi': '广西', 'guangdong': '广东', 'taiwan': '台湾', 'xianggang': '香港',
#            'aomen': '澳门', 'hainan': '海南'}

from json import loads, load, dump
from pandas import Series
from numpy import random, append, linspace
from matplotlib import cm


def get_lvl_i(data, ncnt=10):
    '''数据在分级后的哪一级'''
    nid = []
    d_min, d_max = min(data), max(data)
    levels = linspace(d_min, d_max, ncnt + 1)
    levels[0] -= 0.1
    levels[-1] += 0.1
    for dt in data:
        nl = append(levels, dt)
        nl = Series(nl).sort_values().tolist()
        nid.append((nl.index(dt) - 1) / ncnt)
    return nid


dat1 = random.randint(0, 1000, 31)
with open('map_var.json', 'r') as f:
    mv = load(f)

if dat1.shape[0] > 34:
    data = dat1[:33]
    data_num = 33
else:
    data = dat1
    data_num = dat1.shape[0]
city_file_name = list(mv['map_blocks'].keys())[:data_num]
city_data = {}
lvl_n = 10
new_colors = cm.get_cmap('spring_r', lvl_n)
cid = get_lvl_i(data)
for i, cfn in enumerate(city_file_name):
    city_data[cfn] = new_colors(cid[i])

print('01-beijing' in city_data.keys())


