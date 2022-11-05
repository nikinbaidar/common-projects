#!/usr/bin/env python

def pause():
    while cv.waitKey() != 27:
        continue
    cv.destroyAllWindows()
