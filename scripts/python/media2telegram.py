#!/usr/bin/env python3

# DESCRIPTION
# script that sends images or videos to a telegram channel

import urllib.request as ur
import urllib.parse as up
import sys, os, requests

def sendPhoto(url, channel, api_token, caption = "New Post :)"):
	if os.path.isfile(url):
		print("Found local file: " + url)
		r = requests.post("https://api.telegram.org/bot"+api_token+"/sendPhoto?", data={"chat_id": channel_name, "caption": caption}, files = {"photo": open(url, "rb")})
	else:
		r = ur.urlopen("https://api.telegram.org/bot"+api_token+"/sendPhoto?", up.urlencode({"chat_id": channel, "photo": url, "caption": caption}).encode("utf-8")).read()
	print(r)
	return

def sendVideo(url, channel, api_token, caption = "New Post :)"):
	if os.path.isfile(url):
		print("Found local file: " + url)
		r = requests.post("https://api.telegram.org/bot"+api_token+"/sendVideo?", data={"chat_id": channel_name, "caption": caption}, files = {"video": open(url, "rb")})
	else:
		r = ur.urlopen("https://api.telegram.org/bot"+api_token+"/sendVideo?", up.urlencode({"chat_id": channel, "video": url, "caption": caption}).encode("utf-8")).read()
	print(r)
	return

if __name__ == '__main__':

	channel_name = "@"
	api_token_value = ""

	if len(sys.argv) == 1:
		t = input("What type of media do you want to post? Image (i) / Video (v)\n")
		c = input("Caption:\n")
		u = input("Media URL:\n")
		if t == "i":
			sendPhoto(url = u, caption = c, channel = channel_name, api_token = api_token_value)
		elif t == "v":
			sendVideo(url = u, caption = c, channel = channel_name, api_token = api_token_value)
		else:
			print("Unrecognized media type!")
	elif len(sys.argv) == 2:
		sendPhoto(url = sys.argv[1], channel = channel_name, api_token = api_token_value)
	elif len(sys.argv) == 3:
		if sys.argv[1] == "photo":
			sendPhoto(url = sys.argv[2], channel = channel_name, api_token = api_token_value)
		elif sys.argv[1] == "video":
			sendVideo(url = sys.argv[2], channel = channel_name, api_token = api_token_value)
		else:
			sendPhoto(url = sys.argv[1], caption = sys.argv[2], channel = channel_name, api_token = api_token_value)
	elif len(sys.argv) == 4:
		if sys.argv[1] == "photo":
			sendPhoto(url = sys.argv[3], caption = sys.argv[2], channel = channel_name, api_token = api_token_value)
		elif sys.argv[1] == "video":
			sendVideo(url = sys.argv[3], caption = sys.argv[2], channel = channel_name, api_token = api_token_value)
		else:
			print("Wrong order of args, has to be media-info, caption, url")
	else:
		print("Wrong Usage! See script!")
