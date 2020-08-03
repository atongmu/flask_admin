# -*- coding: utf-8 -*-
import os
from sqlalchemy import String, Column, Text
from app.models.BaseMixinsModel import BaseMixinsModel


class ImageDefault(BaseMixinsModel):
    """图片"""
    __tablename__ = "p_image_default"
    url = Column(Text(), comment=u"图片链接")
    path = Column(Text(), comment=u"图片地址")
    desc = Column(String(200), comment=u"描述")

    def __repr__(self):
        return self.desc

    def delete_file(self):
        if os.path.exists(self.file_path):  # 如果文件存在
            os.remove(self.file_path)
            self.is_delete()
            return True
        else:
            return False


class BannerDefault(BaseMixinsModel):
    """轮播图"""
    __tablename__ = "p_banner_default"
    name = Column(String(200), unique=True, nullable=False, comment=u"名称")
    url = Column(Text(), comment=u"图片链接")
    desc = Column(String(200), comment=u"描述")

    def __repr__(self):
        return self.name


class PostersDefault(BaseMixinsModel):
    """广告"""
    __tablename__ = "p_posters_default"
    name = Column(String(200), unique=True, nullable=False, comment=u"名称")
    url = Column(Text(), comment=u"图片链接")
    desc = Column(String(200), comment=u"描述")

    def __repr__(self):
        return self.name


class ConfigDefault(BaseMixinsModel):
    """站点配置"""
    __tablename__ = "b_config_default"
    title = Column(String(200), unique=True, nullable=False, comment=u"提示文本")
    name = Column(String(200), unique=True, nullable=False, comment=u"变量名称")
    value = Column(String(200), unique=True, nullable=False, comment=u"变量名称")

    def __repr__(self):
        return self.title
