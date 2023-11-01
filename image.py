import os
import cv2
from numpy import mean
class Knn : 
    def __dict__(self):
        print("")

    def read_file(self, path = '/'):
        # read current path
        try: 
            files = os.listdir(path)
        except : 
            files = []
        
        for file in files:
            print(self.rgb_extraction(path + "/" + file))
        
        return files

    def rgb_extraction(self, fullpath) : 
        img = cv2.imread(fullpath)
        feature = self.rgb_feature(img)
        rgbmean = self.get_rgb_mean(feature)
        return rgbmean
    
    def first_order_extraction(self, fullpath) : 
        img = cv2.imread(fullpath)
        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # print(gray_image == gray_image2)
        histogram = cv2.calcHist([gray_image], [0], None, [256], [0, 256])
        shis = sum(histogram)
        h = histogram/shis
        i = [0, 255]
        print(h*i)

        return {
            "mean" :"",
            "variance" : "", 
            "skewness" : "",
            "kurtosis" : "",
            "entropy" : ""
        }

    def rgb_feature(self, img):
        return {
            "red" : img[:,:,2], 
            "green" : img[:,:,1],
            "blue" : img[:,:,0]
        }
    
    def get_rgb_mean(self, feature) :
        return {
            "red": round(mean(mean(feature["red"])), 2),
            "green": round(mean(mean(feature["green"])), 2),
            "blue": round(mean(mean(feature["blue"])), 2)
        }

test = Knn()
print(test.first_order_extraction("training_data/latih_01.jpg"))
