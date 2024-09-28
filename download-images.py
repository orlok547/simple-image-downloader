import os
import requests

# List of image URLs
image_urls = [
	'https://example.com/image1.jpg',
	'https://example.com/image2.jpg',
	'https://example.com/image3.jpg'
]

# Directory to save images
save_directory = 'downloaded_images'

# Create the directory if it doesn't exist
if not os.path.exists(save_directory):
	os.makedirs(save_directory)

# Function to download and save images
def download_image(url, folder):
	try:
		response = requests.get(url, stream=True)
		response.raise_for_status()  # Check for request errors
		file_name = os.path.join(folder, url.split("/")[-1])  # Save as the last part of the URL
		with open(file_name, 'wb') as file:
			for chunk in response.iter_content(1024):
				file.write(chunk)
		print(f"Downloaded: {file_name}")
	except requests.exceptions.RequestException as e:
		print(f"Error downloading {url}: {e}")

# Download all images
for url in image_urls:
	download_image(url, save_directory)

print("All images downloaded.")