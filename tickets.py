# coding: gbk

"""Train tickets query via command-line.

Usage:
	ticktes [-gdtkz] <from> <to> <date>

Options:
	-h,--help		��ʾ�����˵�
	-g				����
	-d				����
	-t				�ؿ�
	-k				����
	-z				ֱ��

Examples:
	tickets �Ͼ� ���� 2016-9-23
	tickets -dg �Ͼ� ���� 2016-9-23

"""
import requests
import sys
from stations import stations
from docopt import docopt
from prettytable import PrettyTable
from colorama import Fore, init, AnsiToWin32

def cli():
    """command-line interface"""
    arguments = docopt(__doc__)
    from_station = stations.get(arguments['<from>'])
    to_station = stations.get(arguments['<to>'])
    date = arguments['<date>']
    
    #����url
    #��chrome�����߹���Network�ҵ���Name���Ҽ�copy link address
    #��queryDate��from_station��to_station����{}ռλ��
    url = 'https://kyfw.12306.cn/otn/lcxxcx/query?purpose_codes=ADULT&queryDate={}&from_station={}&to_station={}'.format(date, from_station, to_station)

    #���verify=False����������֤֤��
    r = requests.get(url, verify = False)
    rows = r.json()['data']['datas']
    
    #��ʽ����ʾ����
    headers = '���� ��վ ʱ�� ��ʱ ���� һ�� ���� ���� Ӳ�� ���� Ӳ�� ����'.split()
    pt = PrettyTable()
    pt._set_field_names(headers)
    for row in rows:
        #��row�и���headers������Ϣ��Ȼ�����pt.add_row()��ӵ�����
        pt.add_row([row["station_train_code"],row["start_station_name"],row["start_time"],row["lishi"],row["swz_num"],row["zy_num"],row["ze_num"],row["rw_num"],row["yw_num"],row["rz_num"],row["yz_num"],row["wz_num"]])
        pt.add_row(["",row["end_station_name"],row["arrive_time"],"","","","","","","","",""])
    print(pt)
    
if __name__ == '__main__':
    cli()





