from configuration_settings import configuration_settings
import datetime
import pandas as pd_pricing
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists

config_settings = configuration_settings()


def get_date():

    today = datetime.datetime.now()
    data_date = today.strftime('%m/%d/%Y')
    uri_date = today.strftime('%Y%m%d')

    return data_date, uri_date


def get_db_connection():
    db_conn = ''
    db_url = config_settings['database_information']['alchemy_engine']
    if database_exists(db_url):
        db_conn = create_engine(db_url, connect_args={'options': '-csearch_path=energydata_miso'})
        print('Database exists')
    else:
        print('Connection Failed')

    return db_conn


def da_exante_data(trade_date, uri_date):

    data_table = config_settings['database_information']['database_table']
    lmp_data = pd_pricing.read_csv(f'https://docs.misoenergy.org/marketreports/{uri_date}_da_exante_lmp.csv', skiprows=4)
    lmp_data.insert(3, 'Date', trade_date)
    data = lmp_data
    engine = get_db_connection()
    try:
        data.to_sql(data_table, engine, if_exists='append', index=False)
        print('CSV data imported')
    except Exception as db_err:
        print(db_err)


if __name__ == '__main__':

    trade_date, uri_date = get_date()
    da_exante_data(trade_date, uri_date)