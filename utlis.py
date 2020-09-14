import os
from datetime import date, datetime


def create_dir_if_not_exists(dir_name):
    dirs = os.listdir(os.getcwd())
    if dir_name in dirs:
        os.chdir(dir_name)
        return os.getcwd()
    else:
        os.mkdir(dir_name)        
        os.chdir(dir_name)
        return os.getcwd()


def create_excel_file():

    now = datetime.now()
    current_year = now.year
    current_month = now.month
    current_day = now.day
    current_hour = now.hour
    current_minute = now.minute
    current_second = now.second
    report_name = str('Report_{year}-{month}-{day}_{hour}:{minute}:{second}.xlsx'.format(year=str(current_year), month=str(current_month), day=str(current_day), hour=str(current_hour), minute=str(current_minute), second=str(current_second)))
    report_dir = create_dir_if_not_exists('generated_reports')
    # path = report_dir + '/' + report_name
    return report_dir


# (lambda path_report_exists: os.getcwd() + '/generated_reports/' + report_name if path_report_exists == True else os.mkdir('generated_reports') + '/' + report_name ) (is_generated_reports)