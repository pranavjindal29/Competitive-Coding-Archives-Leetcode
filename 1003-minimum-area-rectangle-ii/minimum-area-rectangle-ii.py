class Solution:
  def minAreaFreeRect(self, points: List[List[int]]) -> float:
    """ O(N^2) """
    min_area = float("inf")
    seen = dict()
    for i, (x1,y1) in enumerate(points):
      for x2,y2 in points[i+1:]:
        cx = (x1+x2)/2
        cy = (y1+y2)/2
        d = (x1-x2)**2 + (y1-y2)**2

        for xi,yi in seen.setdefault((cx,cy,d),[]):
          side1 = (x1-xi)**2 + (y1-yi)**2
          side2 = (x2-xi)**2 + (y2-yi)**2
          min_area = min(min_area, (side1*side2)**0.5)
        seen.setdefault((cx,cy,d),[]).append((x1,y1))
    return 0 if min_area == float("inf") else min_area

  def minAreaFreeRect_v1(self, points: List[List[int]]) -> float:
    """ O(N^4) """
    min_area = float("inf")
    for x1,y1 in points:
      for x2,y2 in points:
        if [x2,y2] == [x1,y1]:
          continue
        for x3,y3 in points:
          if [x3,y3] in [[x1,y1],[x2,y2]]:
            continue
          P = (x1-x2)**2 + (y1-y2)**2
          B = (x1-x3)**2 + (y1-y3)**2
          H = (x2-x3)**2 + (y2-y3)**2
          if P + B == H:
            for x4,y4 in points:
              if [x4,y4] not in [[x1,y1],[x2,y2],[x3,y3]]:
                P2 = (x4-x2)**2 + (y4-y2)**2
                B2 = (x4-x3)**2 + (y4-y3)**2
                H2 = (x2-x3)**2 + (y2-y3)**2
                H3 = (x1-x4)**2 + (y1-y4)**2

                chk = (P == P2 and B==B2) or (P==B2 and B==P2) 
                chk = chk and H==H2==H3
                if chk and P2+B2 == H2:
                  min_area = min(min_area, (P*B)**0.5)

    return 0 if min_area == float("inf") else min_area