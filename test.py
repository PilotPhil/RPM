# -*- coding: utf-8 -*-

import rhinoscriptsyntax as rs

curveA = rs.GetObject("Select first curve", rs.filter.curve)
curveB = rs.GetObject("Select second curve", rs.filter.curve)

temp = rs.CurveBooleanIntersection(curveA, curveB)

arrResult = rs.CurveBooleanDifference(curveA, temp)

rs.DeleteObjects([curveA,curveB,temp])