# calc module
import json


class Calculator:
    _data = []
    _category_count_dict = {}
    _res_json = []

    def load(self, filename):
        # TODO: validate input file format
        "[ { gender, weight, height } ... ]"
        with open(filename, 'r') as f:
            self._data = json.load(f)

    def get_data(self):
        return self._data

    @staticmethod
    def cal_bmi(weight, height):
        '''
        :param weight: in kg
        :param height: in meters
        :return: bmi rounded to one decimal
        '''
        return round(weight / (height * height), 1)

    @staticmethod
    def calc_category_risk(bmi):
        """
        :param bmi: bmi
        :return: category, risk
        """
        if bmi <= 18.4 :
            return 'Underweight', 'Malnutrition risk'

        if bmi <= 24.9 :
            return 'Normal weight', 'Low risk'

        if bmi <= 29.9 :
            return 'Overweight', 'Enhanced risk'

        if bmi <= 34.9 :
            return 'Moderately obese', 'Medium risk'

        if bmi <= 39.9 :
            return 'Severely obese', 'High risk'

        return 'Very severely obese', 'Very high risk'

    def process_data(self):
        """
        processes data and updates res, count dict
        """
        # clear res and count at begining
        self._res_json = []
        self._category_count_dict = {}

        # for each data
        for data in self._data:
            res = data.copy()

            # calculate bmi, category and risk
            bmi = self.cal_bmi(data["WeightKg"], data["HeightCm"]/100)
            category, risk = self.calc_category_risk(bmi)

            # update res, count
            res['category'] = category
            res['risk'] = risk
            self._res_json.append(res)
            self._category_count_dict[category] = self._category_count_dict.get(category, 0) + 1

    def get_res_json(self):
        return self._res_json

    def get_count(self, category):
        return self._category_count_dict.get(category)