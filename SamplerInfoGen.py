from glob import glob
import keys
import random
import id_no_generator


class SampleInfoGenerator:
    def __init__(self):
        self.chn_chars = list(keys.pureChinese)

    def gen_chi_name(self):
        return ''.join(random.sample(self.chn_chars, random.choice([2,3,4])))

    def get_id_card_no(self):
        age = random.randint(0, 100)
        gender = random.randint(0, 2)
        area_code = random.choice(list(id_no_generator.area_dict))
        return id_no_generator.gen_id_card(int(area_code), age, gender)

    def get_info(self,id_card_no):
        return id_no_generator.is_id_card(id_card_no)

    def get_register_info(self):
        chi_name = self.gen_chi_name()
        id_card_no = self.get_id_card_no()
        is_valid,area,gender,dob = self.get_info(id_card_no)
        return chi_name, gender, dob, id_card_no, area, is_valid









