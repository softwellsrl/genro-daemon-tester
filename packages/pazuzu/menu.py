# encoding: utf-8
class Menu(object):
    def config(self,root,**kwargs):
        root.packageBranch(u"Test", tags="", pkg="test")
        root.packageBranch(u"Test 15", tags="", pkg="test15")

        root.packageBranch(u"Amministrazione", tags="admin", pkg="adm")
        root.packageBranch(u"Sistema", tags="sysadmin,_DEV_", pkg="sys")
