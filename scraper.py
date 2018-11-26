import os
import re

start_url = "https://www.lds.org/media-library/video/categories/bible-videos-chronologically?lang=eng"

def download_html(url):
	global num
	command = f"curl {url} > temp.html"
	os.system(command)

def get_urls():
	command = """sed -n 's/.*href="\\([^"]*\\).*/\\1/p' temp.html"""
	urls = os.popen(command).readlines()
	valids = set()
	for url in urls:
		if "video" in url and "https" not in url and len(url) > 25:
			valids.add(url.strip())
	return list(valids)

def download_video(url):
	if "2014" in url:
		media_url = "http://media2.ldscdn.org/assets/scripture-and-lesson-support/the-life-of-jesus-christ-bible-videos-2014/"
	elif "2016" in url:
		media_url = "http://media2.ldscdn.org/assets/scripture-and-lesson-support/the-life-of-jesus-christ-bible-videos-2016/"
	else:
		media_url = "http://media2.ldscdn.org/assets/scripture-and-lesson-support/the-life-of-jesus-christ-bible-videos/"
	end_url = "-1080p-eng.mp4?download=true"
	title = re.search('(?<=o\/)(.*?)(?=\?)', url).group(0).strip()
	title_only = re.search('[a-z].*', title).group(0).strip()
	command = f"curl {media_url}{title}{end_url} > {title_only}.mp4"
	os.system(command)

def clean():
	os.system("rm temp.html")

def main():
	download_html(start_url)
	video_urls = get_urls()
	for url in video_urls:
		download_video(f"{url}?")
	clean()

if __name__ == "__main__":
	main()
