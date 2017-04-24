import re



def validateTitle(title):
    """
    将标题中的特殊字符去掉(test_succeed)
    :param title: 带有特殊字符的标题
    :return: 去除特殊字符之后的标题
    """
    rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/\:*?"<>|'
    new_title = re.sub(rstr, "", title)
    return new_title

