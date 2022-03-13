# -*- coding: utf-8 -*-
import logging
import os
from pathlib import Path
from dotenv import find_dotenv, load_dotenv

import click
import pandas as pd


@click.command()
@click.argument('output_filepath', type=click.Path())
def main(output_filepath: str = os.path.join('data', 'processed')):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')
    data = pd.read_csv((
        'https://raw.githubusercontent.com/rfordatascience/tidytuesday/'
        'master/data/2019/2019-01-29/milkcow_facts.csv'
    ))
    data.to_csv(os.path.join(output_filepath,
                'milkcow_facts.csv'), index=False)
    logger.info('exported final data set')


if __name__ == '__main__':
    LOG_FMT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=LOG_FMT)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
