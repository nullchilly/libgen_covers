import os
import pymysql
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

# Connect to MySQL
mysql_conn = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='books',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

# Function to download cover image
def download_cover(url, filename):
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
    print(filename)
    if os.path.exists(filename):
        print(f"{filename} already exists. Skipping download.")
        return True
    response = requests.get(url, headers=headers, stream=True)
    if response.status_code == 200:
        # Get the ID from the filename
        folder_name = os.path.dirname(filename)
        os.makedirs(folder_name, exist_ok=True)  # Create the folder if it doesn't exist
        with open(filename, 'wb') as f:
            for chunk in tqdm(response.iter_content(chunk_size=8192), desc='Downloading', unit='KB'):
                if chunk:
                    f.write(chunk)
                    f.flush()
        return True
    else:
        print(f"Failed to download {filename}. Status code: {response.status_code}")
        return False

# Main function to download covers
def download_covers(data):
    with ThreadPoolExecutor(max_workers=20) as executor:  # Adjust max_workers as needed
        # print(os.path.dirname(row['Coverurl']))
        futures = [executor.submit(download_cover, "https://libgen.is/covers/" + row['Coverurl'], f"{os.path.dirname(row['Coverurl'])}/{os.path.basename(row['Coverurl'])}") for row in data]
        for future in as_completed(futures):
            result = future.result()

with mysql_conn.cursor() as cursor:
    cursor.execute("SELECT COUNT(*) as total_rows FROM updated")
    total_rows = cursor.fetchone()['total_rows']

# Insert data from MySQL to MongoDB in chunks
chunk_size = 1000  # Adjust the chunk size as needed
offset = 0

# Query data from MySQL in chunks of 1000 IDs
with mysql_conn.cursor() as cursor:
    cursor.execute("SELECT ID, Coverurl FROM updated LIMIT %s OFFSET %s", (chunk_size, offset))
    for offset in range(0, total_rows, chunk_size):
        cursor.execute("SELECT ID, Coverurl FROM updated LIMIT %s OFFSET %s", (chunk_size, offset))
        data = cursor.fetchall()
        # Modify cover_url in the data
        for row in data:
            pass
            # row['Coverurl'] = "https://libgen.is/covers/" + row['Coverurl']
        # Download covers
        download_covers(data)
        print(f"Downloaded {min(offset + chunk_size, total_rows)} out of {total_rows} rows")

# Close MySQL connection
mysql_conn.close()
