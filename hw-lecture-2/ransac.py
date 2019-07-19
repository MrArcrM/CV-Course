
import random

def ransacMatching(A, B, no_change_times):
    threshold = 3  # similarity threshold
    k = 2000  # iteration number
    inliers = random.sample([A, B], 4)
    outlier = A.remove(inliers)

    count = no_change_times
    while k>0 and count>0:
        model = findHomography(inliers)  # calculate homography
        for p in outlier:
            value = model.cal(p)
            if value < threshold:
                inliers.append(p)
                outlier.remove(p)
                count = no_change_times
            else:
                count -= 1

def findHomography(inliers):
    print('findHomography')
