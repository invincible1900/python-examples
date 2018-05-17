# coding:utf-8

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

def parse_xml(path):
    """
    :param path: xml文件路径
    :return:
    """
    try:
        tree = ET.parse(path)  # 打开xml文档
        root = tree.getroot()  # 获得root节点
        namespace = ''
        for k in root.keys():
            if '{' in k and '}' in k:
                namespace = k[k.index('{'):k.index('}')+1]
        if not namespace:
            return None
    except:
        return None


    try:
        for application_tag in root.findall('application'):
            for activity_tag in application_tag.findall('activity'):
                for intentfilter_tag in activity_tag.findall('intent-filter'):
                    for action_tag in intentfilter_tag.findall('action'):
                        if "android.intent.action.MAIN" in action_tag.attrib.values():
                            for k in activity_tag.attrib:
                                if namespace + 'name' in k:
                                    return activity_tag.attrib[k]
    except:
        return None


if __name__ == '__main__':
    print(parse_xml('AndroidManifest.xml'))