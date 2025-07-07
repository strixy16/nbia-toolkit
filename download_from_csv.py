
from nbiatoolkit import NBIAClient
from pathlib import Path
import click

@click.command()
@click.option('--series_list', help='Path to the CSV file containing series IDs', required=True)
@click.option('--download_dir', help='Directory to download the images to', required=True)
def download_series(series_list, download_dir):
    """
    Download series from TCIA using a list of SeriesInstanceUIDs.
    
    :param series_list: Path to the CSV file containing SeriesInstanceUIDs.
    :param download_dir: Directory to download the images to.
    """
    with open(series_list, 'r') as f:
        series_ids_list = [line.strip() for line in f]
    
    series_ids_list = list(set(series_ids_list))  # Remove duplicates

    file_pattern = '%Modality/%PatientID/%StudyInstanceUID/%SeriesInstanceUID/%InstanceNumber.dcm'
    n_parallel = 8

    with NBIAClient(return_type="dataframe") as client:
        client.downloadSeries(
            SeriesInstanceUID=series_ids_list,
            downloadDir=download_dir,
            filePattern=file_pattern,
            nParallel=n_parallel,
            Progressbar=True
        )

if __name__ == "__main__":
    download_series()


