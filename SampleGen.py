import SamplerInfoGen
from glob import glob
import cv2
import random
from PIL import Image,ImageDraw,ImageFont
import numpy as np

class SampleGenerator:
    def __init__(self):
        self.save_path = './Samples/'
        self.font_list = glob('./Fonts/*.ttf')
        self.bold_font = './Fonts/hwzs.ttf'
        self.common_font = './Fonts/SimSun.ttf'
        self.tempt_path_list = glob('./Templates/*.jpeg')
        self.tempt_arr_list = [cv2.imread(tempt_path) for tempt_path in self.tempt_path_list]
        self.samplerInfoGen = SamplerInfoGen.SampleInfoGenerator()


    def get_all_info(self):
        return self.samplerInfoGen.get_register_info()

    def get_coord(self):
        name_x = random.randint(580,700) #590
        name_y = random.randint(198,210) #205
        gender_x = random.randint(1800,1900) #1820
        gender_y = random.randint(340,355) #348
        dob_x = random.randint(1770,1830) #1774
        dob_y = random.randint(610,625) #618
        id_no_x = random.randint(530,560) #550
        id_no_y = random.randint(880,895) #886
        return name_x,name_y,gender_x,gender_y,dob_x,dob_y,id_no_x,id_no_y

    def write_on_template(self):
        name_x, name_y, gender_x, gender_y, dob_x, dob_y, id_no_x, id_no_y = self.get_coord()
        name,gender,dob,id_no,_,_ = self.get_all_info()
        font_name = ImageFont.truetype(self.bold_font, random.randint(68,80))
        font_no = ImageFont.truetype(self.bold_font, random.randint(60, 68))
        font_others = ImageFont.truetype(self.common_font, random.randint(62, 70))
        img = Image.open(random.choice(self.tempt_path_list))
        # img = img.convert('RGBA')
        # img.show()
        draw = ImageDraw.Draw(img)
        rand_fill = random.randint(77, 100)
        fill = (rand_fill,rand_fill,rand_fill)
        draw.text((name_x, name_y), name, fill=fill, font=font_name)
        draw.text((gender_x, gender_y), gender, fill=fill, font=font_others)
        draw.text((dob_x, dob_y), dob, fill=fill, font=font_others)
        draw.text((id_no_x, id_no_y), id_no, fill=fill, font=font_no)
        return img

    def get_blurred(self, img):
        img_array = np.asarray(img)
        blur_kernel = random.randrange(5,9,2)
        blur_var = random.randrange(2,4)
        return cv2.GaussianBlur(img_array,(blur_kernel,blur_kernel),blur_var) #add gaussian blue to the image

    def adjust_gamma(self,image):
        gamma = random.randrange(6, 18, 2) / 10.0
        invGamma = 1.0 / gamma
        table = np.array([((i / 255.0) ** invGamma) * 255 for i in np.arange(0, 256)]).astype("uint8")
        return cv2.LUT(image, table)

    def get_sample(self, cnt):
        for i in range(cnt):
            img = self.write_on_template()
            blurred_img_arr = self.get_blurred(img)
            gamma_img_arr = self.adjust_gamma(blurred_img_arr)
            # cv2.imshow(str(i),gamma_img_arr)
            # cv2.waitKey(0)
            cv2.imwrite(self.save_path+str(i)+'.png',gamma_img_arr)

if __name__ == '__main__':
    sampleGen = SampleGenerator()
    sampleGen.get_sample(100)

