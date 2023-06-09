import gdown
import argparse

file_destinations = {'GAN-Colorization':'Victorian400.zip'}

file_id_dic = {'GAN-Colorization':'1_NX9egQeck5gmmTQD9SmJULWSpSIfcZV'}

def download_file_from_google_drive(id_, destination):
    url = f'https://drive.google.com/uc?id={id_}'
    output = destination
    gdown.download(url, output, quiet=False)
    print(f'{output} download complete!')
    
parser = argparse.ArgumentParser(description = 'Data loader for the DHSI workshop: Deep Learning for Humanists')

parser.add_argument('--data', type = str, help = 'key for selecting data')

args = parser.parse_args()

download_file_from_google_drive(id_=file_id_dic[args.data], destination=file_destinations[args.data])