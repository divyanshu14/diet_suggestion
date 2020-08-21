from bing_image_downloader import downloader

with open('download-dataset-query-strings.txt') as f:
    for query_string in f:
        query_string = query_string.strip()
        print('Downloading images for:', query_string)
        print()
        downloader.download(query_string, limit=500,  output_dir='indian-food-dataset-divyanshu', adult_filter_off=True, force_replace=False, timeout=60)
        print()
        print()
