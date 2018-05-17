# coding:utf-8
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

x = """<?xml version='1.0' encoding='UTF-8'?> <data> <country name="Liechtenstein"> <rank updated="yes">2</rank> <year>2008</year> <gdppc>141100</gdppc> <neighbor direction="E" name="Austria" /> <neighbor direction="W" name="Switzerland" /> </country> <country name="Singapore"> <rank updated="yes">5</rank> <year>2011</year> <gdppc>59900</gdppc> <neighbor direction="N" name="Malaysia" /> </country> </data> """
tree = ET.fromstring(x)  # 打开xml文档
root = tree.getroot()  # 获得root节点