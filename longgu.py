# -*- coding: utf-8 -*-

import rhinoscriptsyntax as rs

def myOffset(of=3.0):
    crv1 = rs.GetObject("选择曲线", rs.filter.curve)
    line1 = rs.AddLine(rs.CurveStartPoint(crv1),rs.CurveEndPoint(crv1))
    
    crv2 = rs.OffsetCurve( crv1, [0,0,1], of)
    line2 = rs.AddLine(rs.CurveStartPoint(crv2),rs.CurveEndPoint(crv2))

    obj1 = rs.JoinCurves([crv1,line1])
    obj2 = rs.JoinCurves([crv2,line2])

    rs.DeleteObjects([crv1,line1])
    rs.DeleteObjects([crv2,line2])
    
    temp = rs.CurveBooleanIntersection(obj1, obj2)
    arrResult = rs.CurveBooleanDifference(obj1, temp)
    
    if arrResult:
        rs.DeleteObjects([obj1,obj2,temp])


if __name__ == '__main__':
    
    while True:
        myOffset(5000)

        flag = rs.GetString('continue---c, exit---e', 'c')
        if flag == 'E' or flag == 'e':
            break
