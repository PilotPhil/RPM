# -*- coding: utf-8 -*-

###########################
#   RhinoPythonModelling
#   犀牛脚本建模
#   Pilot.Phil
#   632913013@qq.com
#   2020-12-15


import rhinoscriptsyntax as rs
import sys
import xlrd
import xdrlib

# 选择路径
def ChoosePath():
    path=rs.OpenFileName("选择一个文件")
    if path!=None:
        return path
    else:
        print('未选择文件或其他错误')


# 加载excel表格
def LoadXls(path,sheetIndex=0):
    try:
        excel=xlrd.open_workbook(path)
        print('已加载表格文件【%s】' %path)
        workSheet=excel.sheet_by_index(sheetIndex)
        row=workSheet.nrows
        col=workSheet.ncols
        print("表格有%d行，%d列" %(row,col))
        xlsData={'sheet':workSheet,'rowNum':row,'colNum':col}
        return xlsData

    except:
        print('无法打开表格文件，检查文件格式与内容')

# 从表格中获取所有点数据
def GetAllPointsFromXls(xlsData):
    points=[]
    rowNum=xlsData['rowNum']
    workSheet=xlsData['sheet']

    for i in range(0,rowNum):
        x=float(workSheet.cell(i,0).value)
        y=float(workSheet.cell(i,1).value)
        z=float(workSheet.cell(i,2).value)

        points.append([x,y,z])

    return points

# 多点连成线
def ConnectPoints2Lines(model=0):
    pointsId = rs.GetObjects("选取多个点", rs.filter.point)
    if model==0:
        rs.AddInterpCurve(pointsId)
    elif model==1:
        rs.AddCurve(pointsId)
    else:
        pass



if __name__=='__main__':
    path=ChoosePath()
    xlsData=LoadXls(path,0)
    points=GetAllPointsFromXls(xlsData)
    rs.AddPoints(points)
