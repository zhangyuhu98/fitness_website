# coding:utf-8
from django.db import models


class Project(models.Model):
    projectid = models.CharField(max_length=128)
    projectname = models.CharField(max_length=128)
    level = models.CharField(max_length=16)
    time = models.DateField(default=0)
    interval = models.IntegerField(default=0)

    def __unicode__(self):
        return self.projectname


class People(models.Model):
    uid = models.AutoField(primary_key=True)  # 用户id
    name = models.CharField(max_length=128, unique=True)  # 名字
    age = models.IntegerField(default=12)  # 年龄
    hight = models.IntegerField(default=0)  # 身高
    weight = models.IntegerField(default=0)  # 体重
    aim = models.CharField(max_length=128)  # 目标
    birth = models.DateField()  # 出生日期
    projectid = models.ForeignKey(Project)  # 项目id
    city = models.CharField(max_length=128)  # 城市
    frequency = models.IntegerField(default=0)  # 次数
    followed = models.IntegerField(default=0)  # 被点赞
    like = models.IntegerField(default=0)  # 被关注
    fans = models.IntegerField(default=0)  # 粉丝数
    dynamic = models.CharField(max_length=512)  # 动态

    def __unicode__(self):
        return self.name


class Source(models.Model):
    uid = models.IntegerField(primary_key=True)
    picpath = models.CharField(max_length=128)
    text = models.CharField(max_length=512)
    sendtime = models.DateField()

    def __unicode__(self):
        return self.text
