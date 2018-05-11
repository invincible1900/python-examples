# coding:utf-8
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
import glob
import json
from lib.mytimer import MyTimer
import loghandler
LOGGER = loghandler.setup_logging()

class Json2ES:
    def __init__(self, index_settings, index_name, type_name, es_host='localhost:9200'):

        self._index = index_name
        self._type = type_name
        self._index_settings = index_settings
        self.es_host = es_host
        self.es = Elasticsearch(self.es_host)

        # 记录插入的总条数
        self.count = 0

        # 记录使用的总时间
        self.total_time = 0

        if not self.es.indices.exists(index=self._index):
            self.es.indices.create(index=self._index, body=self._index_settings)
            LOGGER.info(u'成功创建index: %s' % self._index)
        else:
            LOGGER.info(u'Index: %s已经存在' % self._index)

    def _bulk_insert(self, actions):
        try:
            with MyTimer() as timer:
                success, _ = bulk(self.es, actions, self._index)
                self.count += success
            self.total_time += timer.total
            LOGGER.info(u'成功插入%d条数据，共用时%ss' % (self.count, str(self.total_time)[:6]))
            return True
        except:
            LOGGER.exception(u'插入数据异常')
            return False

    def insert_from_multifiles(self, doc_dir='.', file_reg='*.json', bulk_size=5000):
        """
        读取多个Json文件并插入到数据库：
        读取doc_dir下的所有符合file_reg文件，并读取其中的数据，并批量插入Elasticsearch。
        要求json文件内容格式: {'data': []}。

        :param doc_dir: 目标json文件的父目录
        :param bulk_size: 一次批量插入的doc条数
        :param file_reg: json文件名的regex匹配表达式
        :return:
        """
        # 去掉路径两端的"\"
        doc_dir = doc_dir.strip('\\')
        file_reg = file_reg.strip('\\')

        # 保存批量插入的action
        _actions = []

        # 读取目标JSON文件列表
        try:
            flist = sorted(glob.glob(doc_dir + '\\' + file_reg)[:10])
            if not flist:
                LOGGER.exception(u'文件列表为空，请检查file_reg参数：%s是否正确' % file_reg)
            else:
                LOGGER.info(u'共读取到%d个目标json文件' % len(flist))
        except:
            LOGGER.exception(u'读取文件列表异常')
            return

        # 遍历文件列表
        for fname in flist:
            LOGGER.info(u'读取%s文件数据' % fname)
            with open(fname, 'r') as f:
                try:
                    data = json.loads(f.read())['data']
                except Exception as e:
                    LOGGER.exception(u'文件%s读取失败' % fname)
                    continue

                for doc in data:
                    action = {
                        "_index": self._index,
                        "_type": self._type,
                        "_source": doc
                    }
                    _actions.append(action)
                    if len(_actions) == bulk_size:
                        self._bulk_insert(_actions)
                        _actions = []

        # 将剩余的不足bulk_size的actions插入
        self._bulk_insert(_actions)

    def insert_json(self, json_data):
        self.es.index(index=self._index, doc_type=self._type, body=json_data)


if __name__ == '__main__':
    # 设置ES参数
    index_name = '你的index名称'
    type_name = '你的type名称'
    index_settings = {
        "mappings": {
            type_name: {
                "properties": {
                    "full_html": {
                        "type": "keyword",  # 用于将html全文作为keyword保存
                        "ignore_above": 1024,
                    },
                    "full_title": {
                        "type": "keyword",  # 用于将title全文作为keyword保存
                        "ignore_above": 1024,
                    },
                    "full_server": {
                        "type": "keyword",  # 用于将headers.Server全文作为keyword保存
                        "ignore_above": 1024,
                    },
                    "url": {
                        "type": "keyword",
                        "ignore_above": 1024,
                    },
                    "title": {
                        "type": "text",  # title需要分词
                        "index": True,  # title需要分词
                        "analyzer": "smartcn",  # 使用smartcn分词器
                        "store": True,
                        "copy_to": "full_title"  # 全文保存到full_title
                    },
                    "headers": {
                        "type": "object",
                        "properties": {
                            "Server":
                                {
                                    "type": "text",  # headers.Server需要分词
                                    "index": True,
                                    "analyzer": "smartcn",  # 使用smartcn分词器
                                    "store": True,
                                    "copy_to": "full_server"  # 全文保存到full_server
                                },
                        }
                    },
                    "html": {
                        "type": "text",  # html需要分词
                        "index": True,
                        "analyzer": "smartcn",  # 使用smartcn分词器
                        # "store": True,
                        "copy_to": "full_html"  # 全文保存到full_server
                    },
                    "res_code": {
                        "type": "integer"
                    },
                    "time": {
                        "type": "keyword"
                    },
                    "ip": {
                        "type": "keyword"
                    },
                    "port": {
                        "type": "integer"
                    }
                }
            }
        }
    }

    # 创建j2es对象(在ES中创建index，type并设置mapping)
    j2es = Json2ES(index_settings, index_name, type_name)

    # 指定目标文件插入Elasticsearch
    j2es.insert_from_multifiles(doc_dir=r"文件父目录，默认当前目录",
                                file_reg=r'默认以.json为后缀的文件', bulk_size=5000)
