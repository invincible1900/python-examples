# coding:utf-8
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
import glob
import json
import os
from mytimer import MyTimer
import loghandler
LOGGER = loghandler.setup_logging()


class Json2ES:
    """
    json导入elasticsearch工具：
    1. 支持多文件批量导入
    2. 支持断点续传
    3. 支持单条json导入
    4. 支持远程es服务器
    5. 批量导入支持自由设置上传数据块大小
    """
    def __init__(self, index_settings, index_name, type_name, es_host='localhost:9200'):

        self._index = index_name
        self._type = type_name
        self._index_settings = index_settings
        self._es_host = es_host

        # es连接对象
        self._es = None

        # 记录插入的总条数
        self.count = 0

        # 记录使用的总时间
        self.total_time = 0

        # 记录已经读取的文件
        self.done_files = {}

        # 记录已经读取的文件路径
        self.done_file_name = '{}_{}_done_files.json'.format(index_name, type_name)

    def _create_index(self):
        if not self._es.indices.exists(index=self._index):
            self._es.indices.create(index=self._index, body=self._index_settings)
            LOGGER.info(u'成功创建index: %s' % self._index)
        else:
            LOGGER.info(u'Index: %s已经存在' % self._index)

    def _doc2action(self, doc):
        action = {
            "_index": self._index,
            "_type": self._type,
            "_id": doc['ip'] + "_" + str(doc['port']),  # 自定义ID
            "_source": doc
        }
        return action

    def _bulk_insert(self, actions):
        try:
            with MyTimer() as timer:
                success, _ = bulk(self._es, actions, self._index)
                self.count += success
            self.total_time += timer.total
            LOGGER.info(u'成功插入%d条数据，共用时%ss' % (self.count, str(self.total_time)[:6]))
            return True
        except:
            LOGGER.exception(u'数据插入失败')
            return False

    def _update_done_file(self):
        with open(self.done_file_name, 'w') as f:
            f.write(json.dumps(self.done_files, indent=2))

    def es_init(self):
        """
        初始化Elasticsearch
        :return:
        """
        try:
            # 连接到es服务器
            self._es = Elasticsearch(self._es_host)

            # 如果_index不存在则创建
            self._create_index()

            # 加载已经完成的文件记录
            if os.path.exists(self.done_file_name):
                with open(self.done_file_name, 'r') as f:
                    self.done_files = json.loads(f.read())

            return True
        except:
            LOGGER.exception(u'初始化失败')
            return False

    def insert_from_multifiles(self, flist, bulk_size=5000):
        """
        读取多个Json文件并插入到数据库：
        读取doc_dir下的所有符合file_reg文件，并读取其中的数据，并批量插入Elasticsearch。要求json文件内容格式: {'data': []}。

        :param flist: 目标json文件列表
        :param bulk_size: 一次批量插入的doc条数
        :return:
        """

        # 遍历文件列表
        for fname in flist:
            if fname in self.done_files.keys():
                LOGGER.info(u'文件%s已处理，处理结果: %d' % (fname, self.done_files[fname]))
            else:
                self.done_files[fname] = 1
                LOGGER.info(u'读取%s文件数据' % fname)
                with open(fname, 'r') as f:
                    try:
                        data = json.loads(f.read())['data']
                        for i in range(0, len(data), bulk_size):
                            _actions = [self._doc2action(d) for d in data[i: i + bulk_size]]
                            if not self._bulk_insert(_actions):
                                LOGGER.info(u'文件%s插入数据失败' % fname)
                                self.done_files[fname] = -1
                                break
                    except:
                        LOGGER.exception(u'文件%s读取失败' % fname)
                        self.done_files[fname] = -2
                        continue

                self._update_done_file()

    def insert_json(self, json_data):
        self._es.index(index=self._index, doc_type=self._type, body=json_data)


def get_file_list(doc_dir='.', file_reg='*.json'):
    """
    :param doc_dir: 目标json文件的父目录
    :param file_reg: json文件名的regex匹配表达式
    :return:
    """

    # 去掉路径两端的"\"
    doc_dir = doc_dir.strip('\\')
    file_reg = file_reg.strip('\\')

    # 读取目标JSON文件列表
    try:
        flist = glob.glob(doc_dir + '\\' + file_reg)

        if not flist:
            LOGGER.exception(u'文件列表为空，请检查file_reg参数：%s是否正确' % file_reg)
        else:
            LOGGER.info(u'共读取到%d个目标json文件' % len(flist))
            return flist
    except:
        LOGGER.exception(u'读取文件列表异常')
        return


if __name__ == '__main__':
    # 设置ES参数
    index_name = 'indexname'
    type_name = 'typename'
    index_settings = {
        "settings": {
            "index.mapping.total_fields.limit": 5000
         },
        "mappings": {
            type_name: {
                "date_detection": False,
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

    files = get_file_list(doc_dir=r".", file_reg=r'*.json')

    # 创建j2es对象
    j2es = Json2ES(index_settings, index_name, type_name)

    # 初始化j2es对象
    initiated = j2es.es_init()

    if initiated:
        j2es.insert_from_multifiles(files, bulk_size=100)
    else:
        LOGGER.info(u'Elasticsearch初始化失败')
