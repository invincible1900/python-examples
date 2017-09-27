str1 = 
"""
head:
[
item:
{
	"SERVICE_CODE" : "@netbar_wacode@",
	"SERVICE_ONLINE_STATUS" : "@service_online_status@",
	"DATA_ONLINE_STATUS" : "1",
	"EQUIPMENT_RUNNING_STATUS" : "1",
	"ACTIVE_PC" : "1",
	"REPORT_PC" : "1",
	"ONLINE_PERSON" : "1",
	"VITRUAL_NUM" : "@user_online_num@",
	"EXIT_IP" : "@host_wac_wan_ip@",
	"UPDATE_TIME" : "@now_year@-@now_month@-@now_day@ @now_hour@:@now_munite@:@now_second@"
}
tail:
]
"""

str2 = 
"""
序号	属性名						数据长度			允许为空Y/N	默认值	约束条件/说明
1		place_code					varchar(14)				N				场所编码
2		service_online_status		int(1)					N				服务在线状态
																			1.在线 2.离线
3		data_online_status			int(1)					N				数据在线状态
																			1.在线 2. 离线
4		equipment_running_status	int(1)					N				设备运行状态
																			工作状态
																			维护状态
																			异常状态
5		active_pc					int(10)					N			0	活动机器数
6		report_pc					int(10)					N			0	报装机器数
7		online_person				int(10)					N			0	在线人数
8		vitrual_num					int(10)					N			0	在线虚拟身份数
9		exit_ip						varchar(100)			N				出口ip 多个用逗号隔开
10		update_time					datetime				N				最后联系时间
																			Yyyy-MM-dd HH:mm:ss
"""

"""
从str2转换到str1
"""