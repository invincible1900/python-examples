str1 = 
"""
[logtype]
total = 7

[type0]
input_cnt = 1
input_id0 = 
type = CSZL
name = 场所资料
desc = 场所基础信息
max_count = 1
max_time = 300
filename = @file_year@@file_month@@file_day@@file_hour@@file_munite@@file_second@@file_serial_03@_139_440304_050477528_001.log


[type1]
input_cnt = 1
input_id0 = 
type = CSZT
name = 场所状态
desc = 场所状态
max_count = 1
max_time = 300
filename = @file_year@@file_month@@file_day@@file_hour@@file_munite@@file_second@@file_serial_03@_139_440304_050477528_002.log



[type2]
input_cnt = 1
input_id0 = 
type = SBZL
name = 设备资料
desc = 设备资料
max_count = 1
max_time = 300
filename = @file_year@@file_month@@file_day@@file_hour@@file_munite@@file_second@@file_serial_03@_139_440304_050477528_003.log


[type3]
input_cnt = 1
input_id0 = 
type = TZRZ
name = 特征采集日志
desc = 特征采集日志
max_count = 1
max_time = 300
filename = @file_year@@file_month@@file_day@@file_hour@@file_munite@@file_second@@file_serial_03@_139_440304_050477528_004.log


[type4]
input_cnt = 1
input_id0 = 
type = APRZ
name = 被采集热点采集日志
desc = 被采集热点采集日志
max_count = 1
max_time = 300
filename = @file_year@@file_month@@file_day@@file_hour@@file_munite@@file_second@@file_serial_03@_139_440304_050477528_005.log


[type5]
input_cnt = 1
input_id0 = 
type = XWRZ
name = 上网日志
desc = 用户有上网行为时产生日志
max_count = 1
max_time = 300
filename = @file_year@@file_month@@file_day@@file_hour@@file_munite@@file_second@@file_serial_03@_139_440304_050477528_006.log


[type6]
input_cnt = 1
input_id0 = 
type = SJRZ
name = 终端上线日志
desc = 用户认证上线时产生日志
max_count = 1
max_time = 300
filename = @file_year@@file_month@@file_day@@file_hour@@file_munite@@file_second@@file_serial_03@_139_440304_050477528_007.log

[type7]
input_cnt = 1
input_id0 = 
type = SJRZ
name = 终端下线日志
desc = 用户认证下线时产生日志
max_count = 1
max_time = 300
filename = @file_year@@file_month@@file_day@@file_hour@@file_munite@@file_second@@file_serial_03@_139_440304_050477528_007.log


[type8]
input_cnt = 1
input_id0 = 
type = SGRZ
name = 搜索关键字
desc = 搜索关键字
max_count = 10
max_time = 300
filename = @file_year@@file_month@@file_day@@file_hour@@file_munite@@file_second@@file_serial_03@_139_440304_050477528_008.log


[type9]
input_cnt = 1
input_id0 = 
type = RZSJ
name = 认证数据
desc = 认证数据
max_count = 10
max_time = 300
filename = @file_year@@file_month@@file_day@@file_hour@@file_munite@@file_second@@file_serial_03@_139_440304_050477528_009.log



#对接日志类型配置
#input*:输入，即哪一类日志用于产生该类型的对接日志，来源于nm_match_rule.ini里所配置的规则的id
#type:日志类型，按对接文档里所规定的名称填写
#desc:描述，一般为日志的中文名
#max_count:该类型日志单个文件所存在的最大条数
#max_time:该类型的日志多长时间要传输一次，单位为秒
#filename:文件名格式，可带路径，可使用参数变量里nm_log_file_format里的变量，如"action/145-110000-@file_timestamp@-@file_serial_05@-WA_SOURCE_FJ_0002-0.bcp";
#	如果文件名里要用其他变量，则还需按如下格式进行配置：
#	item_count = 1
#	item0 = ap_id
#socket_mode:指定具体的发送方式，用于派博的对接，其值必须为tcp、udp、hbt中的一种，其中hbt仅用于发送心跳日志
#如：
#[type0]
#input_cnt = 1
#input_id0 = login
#type = WA_SOURCE_FJ_0001
#name = 终端上线日志
#desc = 终端上线日志，用户认证上线时发送一条日志
#max_count = 2000
#max_time = 300
#filename = 145-110000-@file_timestamp@-@file_serial_05@-WA_SOURCE_FJ_0001-0.bcp
#socket_mode = tcp

"""

str2=
"""
序号	数据类型			数据类型名称	数据类型编码
1		场所资料			CSZL				001
2		场所状态			CSZT				002
3		设备资料			SBZL				003
4		特征采集日志		TZRZ				004
5		被采集热点采集日志	APRZ				005
6		上网日志			XWRZ				006
7		终端上下线日志		SJRZ				007
8		搜索关键字			SGJZ				008
9		认证数据			RZSJ				009
"""

"""
从str2 到 str1 自动转换
"""