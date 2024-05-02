import os
import requests

# Function to download a file from a URL and save it to a specified path
def download_file(url, file_path, headers):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded {url} to {file_path}")
    else:
        print(f"Failed to download {url}. Status code: {response.status_code}")

# Example URLs
urls = [
    'https://libgen.is/covers/263000/27cf13026e2d72124cc38edc58661516-d.jpg',
    'https://libgen.is/covers/269000/72390a5afc6793e02ff36eaf61ff4532-d.jpg',
    'https://libgen.is/covers/324000/a46c787b38183e0784ae1b0221c5dcb1-d.jpg',
    'https://libgen.is/covers/386000/410d6144e8e009357d3394af44585a0c-d.jpg',
    'https://libgen.is/covers/393000/4cdd5a83d7b596f2da2464182aa2c37b-d.jpg',
    'https://libgen.is/covers/396000/4603e0261e4f5b999d30bd6a385dbff7-g.jpg',
    'https://libgen.is/covers/398000/52f4cf6060fd8a46c10ad97b6c579dd2-d.jpg',
    'https://libgen.is/covers/401000/50740153c2bf4a5db99f8b807b4a4b60-d.jpg',
    'https://libgen.is/covers/406000/7f2b6638ab9ec6bfeb5924bf8e7f17e1-d.jpg',
    'https://libgen.is/covers/406000/7f0f681b7f000521bcc5e70270f8a155-d.jpg',
    'https://libgen.is/covers/409000/7b25a790e51f5e50d508b6c7896731f8-d.jpg',
    'https://libgen.is/covers/410000/7a68fb77bb1e7ad0ec8ed6d189b71fc9-d.jpg',
    'https://libgen.is/covers/414000/7592ff85f4b7fbdaf45dc276ed1fa08f-d.jpg',
    'https://libgen.is/covers/418000/71b8772b9758fdd0ca1da810398111a4-d.jpg',
    'https://libgen.is/covers/425000/6812d5774c143ffae8cddcb7ee0e28e8-d.jpg',
    'https://libgen.is/covers/430000/62747a60236630ee9a6fcce25fc1affb-d.jpg',
    'https://libgen.is/covers/431000/61a7fd7b0f4f411d2d5f38d9e3a77059-d.jpg',
    'https://libgen.is/covers/434000/5e9d654c50d1ca91ab35b564e5e8e97a-d.jpg',
    'https://libgen.is/covers/438000/58e1ea13c4e92764df36a118dc508d6e-d.jpg',
    'https://libgen.is/covers/438000/58f595b5401af1c4f07ca5baedc27741-d.jpg',
    'https://libgen.is/covers/438000/588b5085f49c776acd7b54ed9846b504-d.jpg',
    'https://libgen.is/covers/438000/586f09be44daeb0564807e18199e64be-d.jpg',
    'https://libgen.is/covers/449000/f4f0a5531b51d032e75197b7a6123015-d.jpg',
    'https://libgen.is/covers/449000/f332b5ebb7f6dc195bded563f2ca9e65-d.jpg',
    'https://libgen.is/covers/452000/f06e9d74b7d671c3ff1393c83abf42d2-d.jpg',
    'https://libgen.is/covers/452000/f0a0beca050610397b9a1c2604c1a472-d.jpg',
    'https://libgen.is/covers/456000/ebab27fa9ba01edd805e18fdd00c6232-g.jpg',
]

# Directory to save the files
save_directory = '.'

# Create the directory if it doesn't exist
# if not os.path.exists(save_directory):
#     os.makedirs(save_directory)

# Define headers
headers = {
    'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Cookie': 'lg_topic=libgen',
    'DNT': '1',
    'Pragma': 'no-cache',
    'Referer': 'https://libgen.is/',
    'Sec-Fetch-Dest': 'image',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

# Download each file
for url in urls:
    file_name = url.split('/')[-1]
    os.makedirs(os.path.join(save_directory, url.split('/')[-2]), exist_ok=True)
    file_path = os.path.join(save_directory, url.split('/')[-2], file_name)
    download_file(url, file_path, headers)

