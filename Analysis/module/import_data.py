# coding:utf-8
import pandas as pd

class Import_data():
    def __init__(self,file_name):
        self.file_name = file_name

    def import_nirsdata(self):
        try:
            df = pd.read_csv(self.file_name + '.TXT', sep='\t', skiprows=35)
        except FileNotFoundError:
            print('ファイル形式がTXTではありません．CSVで読み込みます')
            df = pd.read_csv(self.file_name + '.csv', sep=',')
        else:
            df = pd.read_csv(self.file_name + '.TXT', sep='\t', skiprows=35)
        finally:
            print('import_nirs_data')
            if len(df.columns) == 70:#スムージング処理済みの場合
                print('NIRS68ch分をインポート')
                df.columns = ['index', 'time', 'ch1_oxy','ch2_oxy', 'ch3_oxy', 'ch4_oxy', 'ch5_oxy',
                              'ch6_oxy', 'ch7_oxy', 'ch8_oxy', 'ch9_oxy', 'ch10_oxy',
                              'ch11_oxy', 'ch12_oxy', 'ch13_oxy', 'ch14_oxy', 'ch15_oxy',
                              'ch16_oxy', 'ch17_oxy', 'ch18_oxy', 'ch19_oxy', 'ch20_oxy',
                              'ch21_oxy', 'ch22_oxy', 'ch23_oxy', 'ch24_oxy', 'ch25_oxy',
                              'ch26_oxy', 'ch27_oxy', 'ch28_oxy', 'ch29_oxy', 'ch30_oxy',
                              'ch31_oxy', 'ch32_oxy', 'ch33_oxy', 'ch34_oxy', 'ch35_oxy',
                              'ch36_oxy', 'ch37_oxy', 'ch38_oxy', 'ch39_oxy', 'ch40_oxy',
                              'ch41_oxy', 'ch42_oxy', 'ch43_oxy', 'ch44_oxy', 'ch45_oxy',
                              'ch46_oxy', 'ch47_oxy', 'ch48_oxy', 'ch49_oxy', 'ch50_oxy',
                              'ch51_oxy', 'ch52_oxy', 'ch53_oxy', 'ch54_oxy', 'ch55_oxy',
                              'ch56_oxy', 'ch57_oxy', 'ch58_oxy', 'ch59_oxy', 'ch60_oxy',
                              'ch61_oxy', 'ch62_oxy', 'ch63_oxy', 'ch64_oxy', 'ch65_oxy',
                              'ch66_oxy','ch67_oxy', 'ch68_oxy'
                                ]
                return df
            elif len(df.columns) == 73:#スムージング処理済みの場合+EMG
                print('NIRS68ch分をインポート')
                df.columns = ['index', 'time', 'ch1_oxy','ch2_oxy', 'ch3_oxy', 'ch4_oxy', 'ch5_oxy',
                              'ch6_oxy', 'ch7_oxy', 'ch8_oxy', 'ch9_oxy', 'ch10_oxy',
                              'ch11_oxy', 'ch12_oxy', 'ch13_oxy', 'ch14_oxy', 'ch15_oxy',
                              'ch16_oxy', 'ch17_oxy', 'ch18_oxy', 'ch19_oxy', 'ch20_oxy',
                              'ch21_oxy', 'ch22_oxy', 'ch23_oxy', 'ch24_oxy', 'ch25_oxy',
                              'ch26_oxy', 'ch27_oxy', 'ch28_oxy', 'ch29_oxy', 'ch30_oxy',
                              'ch31_oxy', 'ch32_oxy', 'ch33_oxy', 'ch34_oxy', 'ch35_oxy',
                              'ch36_oxy', 'ch37_oxy', 'ch38_oxy', 'ch39_oxy', 'ch40_oxy',
                              'ch41_oxy', 'ch42_oxy', 'ch43_oxy', 'ch44_oxy', 'ch45_oxy',
                              'ch46_oxy', 'ch47_oxy', 'ch48_oxy', 'ch49_oxy', 'ch50_oxy',
                              'ch51_oxy', 'ch52_oxy', 'ch53_oxy', 'ch54_oxy', 'ch55_oxy',
                              'ch56_oxy', 'ch57_oxy', 'ch58_oxy', 'ch59_oxy', 'ch60_oxy',
                              'ch61_oxy', 'ch62_oxy', 'ch63_oxy', 'ch64_oxy', 'ch65_oxy',
                              'ch66_oxy','ch67_oxy', 'ch68_oxy','EMG_ch1', 'EMG_ch2', 'EMG_ch3'
                                ]
                return df
            elif len(df.columns) == 208:#アナログ入力なしの場合
                print('NIRS68ch分をインポート')
                df.columns = ['time', 'task', 'mark', 'count', 'ch1_oxy', 'ch1_deoxy', 'ch1_total',
                                'ch2_oxy', 'ch2_deoxy', 'ch2_total', 'ch3_oxy', 'ch3_deoxy', 'ch3_total',
                                'ch4_oxy', 'ch4_deoxy', 'ch4_total', 'ch5_oxy', 'ch5_deoxy', 'ch5_total',
                                'ch6_oxy', 'ch6_deoxy', 'ch6_total', 'ch7_oxy', 'ch7_deoxy', 'ch7_total',
                                'ch8_oxy', 'ch8_deoxy', 'ch8_total', 'ch9_oxy', 'ch9_deoxy', 'ch9_total',
                                'ch10_oxy', 'ch10_deoxy', 'ch10_total', 'ch11_oxy', 'ch11_deoxy', 'ch11_total',
                                'ch12_oxy', 'ch12_deoxy', 'ch12_total', 'ch13_oxy', 'ch13_deoxy', 'ch13_total',
                                'ch14_oxy', 'ch14_deoxy', 'ch14_total', 'ch15_oxy', 'ch15_deoxy', 'ch15_total',
                                'ch16_oxy', 'ch16_deoxy', 'ch16_total', 'ch17_oxy', 'ch17_deoxy', 'ch17_total',
                                'ch18_oxy', 'ch18_deoxy', 'ch18_total', 'ch19_oxy', 'ch19_deoxy', 'ch19_total',
                                'ch20_oxy', 'ch20_deoxy', 'ch20_total', 'ch21_oxy', 'ch21_deoxy', 'ch21_total',
                                'ch22_oxy', 'ch22_deoxy', 'ch22_total', 'ch23_oxy', 'ch23_deoxy', 'ch23_total',
                                'ch24_oxy', 'ch24_deoxy', 'ch24_total', 'ch25_oxy', 'ch25_deoxy', 'ch25_total',
                                'ch26_oxy', 'ch26_deoxy', 'ch26_total', 'ch27_oxy', 'ch27_deoxy', 'ch27_total',
                                'ch28_oxy', 'ch28_deoxy', 'ch28_total', 'ch29_oxy', 'ch29_deoxy', 'ch29_total',
                                'ch30_oxy', 'ch30_deoxy', 'ch30_total', 'ch31_oxy', 'ch31_deoxy', 'ch31_total',
                                'ch32_oxy', 'ch32_deoxy', 'ch32_total', 'ch33_oxy', 'ch33_deoxy', 'ch33_total',
                                'ch34_oxy', 'ch34_deoxy', 'ch34_total', 'ch35_oxy', 'ch35_deoxy', 'ch35_total',
                                'ch36_oxy', 'ch36_deoxy', 'ch36_total', 'ch37_oxy', 'ch37_deoxy', 'ch37_total',
                                'ch38_oxy', 'ch38_deoxy', 'ch38_total', 'ch39_oxy', 'ch39_deoxy', 'ch39_total',
                                'ch40_oxy', 'ch40_deoxy', 'ch40_total', 'ch41_oxy', 'ch41_deoxy', 'ch41_total',
                                'ch42_oxy', 'ch42_deoxy', 'ch42_total', 'ch43_oxy', 'ch43_deoxy', 'ch43_total',
                                'ch44_oxy', 'ch44_deoxy', 'ch44_total', 'ch45_oxy', 'ch45_deoxy', 'ch45_total',
                                'ch46_oxy', 'ch46_deoxy', 'ch46_total', 'ch47_oxy', 'ch47_deoxy', 'ch47_total',
                                'ch48_oxy', 'ch48_deoxy', 'ch48_total', 'ch49_oxy', 'ch49_deoxy', 'ch49_total',
                                'ch50_oxy', 'ch50_deoxy', 'ch50_total', 'ch51_oxy', 'ch51_deoxy', 'ch51_total',
                                'ch52_oxy', 'ch52_deoxy', 'ch52_total', 'ch53_oxy', 'ch53_deoxy', 'ch53_total',
                                'ch54_oxy', 'ch54_deoxy', 'ch54_total', 'ch55_oxy', 'ch55_deoxy', 'ch55_total',
                                'ch56_oxy', 'ch56_deoxy', 'ch56_total', 'ch57_oxy', 'ch57_deoxy', 'ch57_total',
                                'ch58_oxy', 'ch58_deoxy', 'ch58_total', 'ch59_oxy', 'ch59_deoxy', 'ch59_total',
                                'ch60_oxy', 'ch60_deoxy', 'ch60_total', 'ch61_oxy', 'ch61_deoxy', 'ch61_total',
                                'ch62_oxy', 'ch62_deoxy', 'ch62_total', 'ch63_oxy', 'ch63_deoxy', 'ch63_total',
                                'ch64_oxy', 'ch64_deoxy', 'ch64_total', 'ch65_oxy', 'ch65_deoxy', 'ch65_total',
                                'ch66_oxy', 'ch66_deoxy', 'ch66_total', 'ch67_oxy', 'ch67_deoxy', 'ch67_total',
                                'ch68_oxy', 'ch68_deoxy', 'ch68_total'
                                ]
                return df
            elif len(df.columns) > 208: # アナログ入力ありの場合
                print('NIRS68ch分＋アナログデータをインポート')
                df.columns = ['time', 'task', 'mark', 'count', 'ch1_oxy', 'ch1_deoxy', 'ch1_total',
                              'ch2_oxy', 'ch2_deoxy', 'ch2_total', 'ch3_oxy', 'ch3_deoxy', 'ch3_total',
                              'ch4_oxy', 'ch4_deoxy', 'ch4_total', 'ch5_oxy', 'ch5_deoxy', 'ch5_total',
                              'ch6_oxy', 'ch6_deoxy', 'ch6_total', 'ch7_oxy', 'ch7_deoxy', 'ch7_total',
                              'ch8_oxy', 'ch8_deoxy', 'ch8_total', 'ch9_oxy', 'ch9_deoxy', 'ch9_total',
                              'ch10_oxy', 'ch10_deoxy', 'ch10_total', 'ch11_oxy', 'ch11_deoxy', 'ch11_total',
                              'ch12_oxy', 'ch12_deoxy', 'ch12_total', 'ch13_oxy', 'ch13_deoxy', 'ch13_total',
                              'ch14_oxy', 'ch14_deoxy', 'ch14_total', 'ch15_oxy', 'ch15_deoxy', 'ch15_total',
                              'ch16_oxy', 'ch16_deoxy', 'ch16_total', 'ch17_oxy', 'ch17_deoxy', 'ch17_total',
                              'ch18_oxy', 'ch18_deoxy', 'ch18_total', 'ch19_oxy', 'ch19_deoxy', 'ch19_total',
                              'ch20_oxy', 'ch20_deoxy', 'ch20_total', 'ch21_oxy', 'ch21_deoxy', 'ch21_total',
                              'ch22_oxy', 'ch22_deoxy', 'ch22_total', 'ch23_oxy', 'ch23_deoxy', 'ch23_total',
                              'ch24_oxy', 'ch24_deoxy', 'ch24_total', 'ch25_oxy', 'ch25_deoxy', 'ch25_total',
                              'ch26_oxy', 'ch26_deoxy', 'ch26_total', 'ch27_oxy', 'ch27_deoxy', 'ch27_total',
                              'ch28_oxy', 'ch28_deoxy', 'ch28_total', 'ch29_oxy', 'ch29_deoxy', 'ch29_total',
                              'ch30_oxy', 'ch30_deoxy', 'ch30_total', 'ch31_oxy', 'ch31_deoxy', 'ch31_total',
                              'ch32_oxy', 'ch32_deoxy', 'ch32_total', 'ch33_oxy', 'ch33_deoxy', 'ch33_total',
                              'ch34_oxy', 'ch34_deoxy', 'ch34_total', 'ch35_oxy', 'ch35_deoxy', 'ch35_total',
                              'ch36_oxy', 'ch36_deoxy', 'ch36_total', 'ch37_oxy', 'ch37_deoxy', 'ch37_total',
                              'ch38_oxy', 'ch38_deoxy', 'ch38_total', 'ch39_oxy', 'ch39_deoxy', 'ch39_total',
                              'ch40_oxy', 'ch40_deoxy', 'ch40_total', 'ch41_oxy', 'ch41_deoxy', 'ch41_total',
                              'ch42_oxy', 'ch42_deoxy', 'ch42_total', 'ch43_oxy', 'ch43_deoxy', 'ch43_total',
                              'ch44_oxy', 'ch44_deoxy', 'ch44_total', 'ch45_oxy', 'ch45_deoxy', 'ch45_total',
                              'ch46_oxy', 'ch46_deoxy', 'ch46_total', 'ch47_oxy', 'ch47_deoxy', 'ch47_total',
                              'ch48_oxy', 'ch48_deoxy', 'ch48_total', 'ch49_oxy', 'ch49_deoxy', 'ch49_total',
                              'ch50_oxy', 'ch50_deoxy', 'ch50_total', 'ch51_oxy', 'ch51_deoxy', 'ch51_total',
                              'ch52_oxy', 'ch52_deoxy', 'ch52_total', 'ch53_oxy', 'ch53_deoxy', 'ch53_total',
                              'ch54_oxy', 'ch54_deoxy', 'ch54_total', 'ch55_oxy', 'ch55_deoxy', 'ch55_total',
                              'ch56_oxy', 'ch56_deoxy', 'ch56_total', 'ch57_oxy', 'ch57_deoxy', 'ch57_total',
                              'ch58_oxy', 'ch58_deoxy', 'ch58_total', 'ch59_oxy', 'ch59_deoxy', 'ch59_total',
                              'ch60_oxy', 'ch60_deoxy', 'ch60_total', 'ch61_oxy', 'ch61_deoxy', 'ch61_total',
                              'ch62_oxy', 'ch62_deoxy', 'ch62_total', 'ch63_oxy', 'ch63_deoxy', 'ch63_total',
                              'ch64_oxy', 'ch64_deoxy', 'ch64_total', 'ch65_oxy', 'ch65_deoxy', 'ch65_total',
                              'ch66_oxy', 'ch66_deoxy', 'ch66_total', 'ch67_oxy', 'ch67_deoxy', 'ch67_total',
                              'ch68_oxy', 'ch68_deoxy', 'ch68_total',
                              'EMG_ch1', 'EMG_ch2', 'EMG_ch3',
                              'start_count', 'finish_count', 'AI-6', 'AI-7', 'AI-8'
                              ]
                return df
            else:
                print('ERROR')
