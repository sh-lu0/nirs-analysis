import pandas as pd

class Delete_data():
    def __init__(self,df):
        self.df = df

    def delete_nirsdata(self):
        """
        :return: oxy-Hb以外のデータ
        """
        if len(self.df.columns) < 208:
            print('ERROR：カルム数が足りません（68ch分のデータが入力がない）')
            return self.df
        elif len(self.df.columns) == 208:
            print('不要なカルム削除(68ch分)')
            drop_col = ['task','mark','count','ch1_deoxy','ch1_total','ch2_deoxy','ch2_total',
                        'ch3_deoxy','ch3_total','ch4_deoxy', 'ch4_total','ch5_deoxy','ch5_total',
                        'ch6_deoxy', 'ch6_total', 'ch7_deoxy', 'ch7_total','ch8_deoxy', 'ch8_total',
                        'ch9_deoxy', 'ch9_total','ch10_deoxy', 'ch10_total', 'ch11_deoxy', 'ch11_total',
                        'ch12_deoxy', 'ch12_total', 'ch13_deoxy', 'ch13_total','ch14_deoxy', 'ch14_total',
                        'ch15_deoxy', 'ch15_total','ch16_deoxy', 'ch16_total', 'ch17_deoxy', 'ch17_total',
                        'ch18_deoxy', 'ch18_total', 'ch19_deoxy', 'ch19_total','ch20_deoxy','ch20_total',
                        'ch21_deoxy','ch21_total','ch22_deoxy','ch22_total','ch23_deoxy','ch23_total',
                        'ch24_deoxy', 'ch24_total','ch25_deoxy','ch25_total','ch26_deoxy', 'ch26_total',
                        'ch27_deoxy', 'ch27_total','ch28_deoxy', 'ch28_total', 'ch29_deoxy', 'ch29_total',
                        'ch30_deoxy','ch30_total','ch31_deoxy','ch31_total','ch32_deoxy','ch32_total',
                        'ch33_deoxy','ch33_total','ch34_deoxy', 'ch34_total','ch35_deoxy','ch35_total',
                        'ch36_deoxy', 'ch36_total', 'ch37_deoxy', 'ch37_total','ch38_deoxy', 'ch38_total',
                        'ch39_deoxy', 'ch39_total','ch40_deoxy','ch40_total','ch41_deoxy','ch41_total',
                        'ch42_deoxy','ch42_total','ch43_deoxy','ch43_total','ch44_deoxy', 'ch44_total',
                        'ch45_deoxy','ch45_total','ch46_deoxy', 'ch46_total', 'ch47_deoxy', 'ch47_total',
                        'ch48_deoxy', 'ch48_total', 'ch49_deoxy', 'ch49_total','ch50_deoxy','ch50_total',
                        'ch51_deoxy','ch51_total','ch52_deoxy','ch52_total','ch53_deoxy','ch53_total',
                        'ch54_deoxy', 'ch54_total','ch55_deoxy','ch55_total','ch56_deoxy', 'ch56_total',
                        'ch57_deoxy', 'ch57_total','ch58_deoxy', 'ch58_total', 'ch59_deoxy', 'ch59_total',
                        'ch60_deoxy','ch60_total','ch61_deoxy','ch61_total','ch62_deoxy','ch62_total',
                        'ch63_deoxy','ch63_total','ch64_deoxy', 'ch64_total','ch65_deoxy','ch65_total',
                        'ch66_deoxy', 'ch66_total', 'ch67_deoxy', 'ch67_total','ch68_deoxy', 'ch68_total'
                        ]
            df = self.df.drop(drop_col, axis=1)
            return df
        elif len(self.df.columns) > 208:
            print('不要なカルム削除(68ch分+アナログデータ)')
            drop_col = ['task','mark','count','ch1_deoxy','ch1_total','ch2_deoxy','ch2_total',
                        'ch3_deoxy','ch3_total','ch4_deoxy', 'ch4_total','ch5_deoxy','ch5_total',
                        'ch6_deoxy', 'ch6_total', 'ch7_deoxy', 'ch7_total','ch8_deoxy', 'ch8_total',
                        'ch9_deoxy', 'ch9_total','ch10_deoxy', 'ch10_total', 'ch11_deoxy', 'ch11_total',
                        'ch12_deoxy', 'ch12_total', 'ch13_deoxy', 'ch13_total','ch14_deoxy', 'ch14_total',
                        'ch15_deoxy', 'ch15_total','ch16_deoxy', 'ch16_total', 'ch17_deoxy', 'ch17_total',
                        'ch18_deoxy', 'ch18_total', 'ch19_deoxy', 'ch19_total','ch20_deoxy','ch20_total',
                        'ch21_deoxy','ch21_total','ch22_deoxy','ch22_total','ch23_deoxy','ch23_total',
                        'ch24_deoxy', 'ch24_total','ch25_deoxy','ch25_total','ch26_deoxy', 'ch26_total',
                        'ch27_deoxy', 'ch27_total','ch28_deoxy', 'ch28_total', 'ch29_deoxy', 'ch29_total',
                        'ch30_deoxy','ch30_total','ch31_deoxy','ch31_total','ch32_deoxy','ch32_total',
                        'ch33_deoxy','ch33_total','ch34_deoxy', 'ch34_total','ch35_deoxy','ch35_total',
                        'ch36_deoxy', 'ch36_total', 'ch37_deoxy', 'ch37_total','ch38_deoxy', 'ch38_total',
                        'ch39_deoxy', 'ch39_total','ch40_deoxy','ch40_total','ch41_deoxy','ch41_total',
                        'ch42_deoxy','ch42_total','ch43_deoxy','ch43_total','ch44_deoxy', 'ch44_total',
                        'ch45_deoxy','ch45_total','ch46_deoxy', 'ch46_total', 'ch47_deoxy', 'ch47_total',
                        'ch48_deoxy', 'ch48_total', 'ch49_deoxy', 'ch49_total','ch50_deoxy','ch50_total',
                        'ch51_deoxy','ch51_total','ch52_deoxy','ch52_total','ch53_deoxy','ch53_total',
                        'ch54_deoxy', 'ch54_total','ch55_deoxy','ch55_total','ch56_deoxy', 'ch56_total',
                        'ch57_deoxy', 'ch57_total','ch58_deoxy', 'ch58_total', 'ch59_deoxy', 'ch59_total',
                        'ch60_deoxy','ch60_total','ch61_deoxy','ch61_total','ch62_deoxy','ch62_total',
                        'ch63_deoxy','ch63_total','ch64_deoxy', 'ch64_total','ch65_deoxy','ch65_total',
                        'ch66_deoxy', 'ch66_total', 'ch67_deoxy', 'ch67_total','ch68_deoxy', 'ch68_total',
                        'start_count', 'finish_count', 'AI-6', 'AI-7', 'AI-8'
                        ]
            df = self.df.drop(drop_col, axis=1)
            return df