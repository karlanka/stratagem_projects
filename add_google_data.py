import mysql.connector
import pandas as pd
import os
from sqlalchemy import create_engine


pw = 'anton'
host_name = '127.0.0.1'

cnx = mysql.connector.connect(user='root', password=pw, host=host_name, database='stratagem')
cursor = cnx.cursor(buffered=True)
engine = create_engine('mysql+mysqlconnector://root:anton@localhost/stratagem')


# add the csv-files to their respective tables
def make_df(f_name):

    df = pd.read_csv(f_name)

    df.drop(df.columns[[0]], axis=1, inplace=True)

    if 'minsplayed' in f_name:
        df.to_sql('minsplayed', engine, if_exists='append', chunksize=1000)

    elif 'matchinfo' in f_name:
        df.to_sql('matchinfo', engine, if_exists='append', chunksize=1000)

    elif 'chances' in f_name:
        df.to_sql('chances', engine, if_exists='append', chunksize=1000)

    elif 'keyentries' in f_name:
        df.to_sql('keyentries', engine, if_exists='append', chunksize=1000)


# clear tables
def truncate_tables():

    tables = ['minsplayed', 'chances', 'keyentries', 'matchinfo']

    for table in tables:
        sql = 'TRUNCATE TABLE {};'.format(table)
        cursor.execute(sql)
        cnx.commit()


# read all files in a directory
def read_files(competition_path):

    # list all files in the directory
    files = [f for f in os.listdir(competition_path) if f.endswith('.csv')]

    # send all files to make_df
    for f in files:
        f_name = competition_path + '/' + f
        make_df(f_name)


def main():

    # empty all tables with truncate_table method
    truncate_tables()

    # list of all dirs and subdirs
    competition_paths = [x[0] for x in os.walk("/Users/antonkarling/Google Drive/")]

    # send all paths to read_files method
    for competition_path in competition_paths:
        read_files(competition_path)

if __name__ == '__main__':
    main()
