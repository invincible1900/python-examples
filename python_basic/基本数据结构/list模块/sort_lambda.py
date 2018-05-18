# coding:utf-8
# 把字典a按照code name count的形式输出，并且根据count从大到小排序
a = {'TH': {'name': '泰国', 'count': 5}, 'JP': {'name': '日本', 'count': 373}, 'KR': {'name': '大韩民国', 'count': 286}, 'TW': {'name': '台湾', 'count': 792}, 'HK': {'name': '香港', 'count': 41}, 'BA': {'name': '波斯尼亚和黑山共和国', 'count': 1}, 'GB': {'name': '英国', 'count': 2}, 'IT': {'name': '意大利', 'count': 4}, 'NL': {'name': '荷兰', 'count': 1}, 'NZ': {'name': '新西兰', 'count': 9}, 'IN': {'name': '印度', 'count': 33}, 'US': {'name': '美国', 'count': 4}, 'AU': {'name': '澳大利亚', 'count': 9}, 'BD': {'name': '孟加拉', 'count': 16}, 'PK': {'name': '巴基斯坦', 'count': 20}, 'IR': {'name': '伊朗伊斯兰共和国', 'count': 1}, 'CZ': {'name': '捷克共和国', 'count': 2}, 'RU': {'name': '俄罗斯', 'count': 1}, 'KH': {'name': '柬埔寨', 'count': 3}, 'SG': {'name': '新加坡', 'count': 4}, 'ID': {'name': '印度尼西亚', 'count': 2}, 'CN': {'name': '中国', 'count': 3}, 'BR': {'name': '巴西', 'count': 2}, 'MY': {'name': '马来西亚', 'count': 1}, 'DE': {'name': '德国', 'count': 2}, 'HU': {'name': '匈牙利', 'count': 1}, 'FR': {'name': '法国', 'count': 1}, 'PL': {'name': '波兰', 'count': 1}}

ks = sorted(a.keys(), key=lambda x: int(a[x]['count']), reverse=True)
for k in ks:
    print(k, a[k]['name'], a[k]['count'])