# Instagram-AutoPoster
This repository contains python code for automatic image posting of the quotes. The code masks the quote and author name on the plain image and also adds the same in caption with any 5 random hashtags.

## How to use this code
1. Enter the filename with the path of the Instagram hastags text file. From this file we will be randomly picking the instagram hastags to include in the post's caption. For knowing the format of the hastag file, kindly refer to ```sample_hastags_file.txt```.
2. Enter your Instagram username and password on which you want to autopost the quotes image.
3. The default background image is the cream background image. If you want to use any other background image then download some plain HD image and give the path in the input_image.
4. Enter the path and filename of the csv file in which we will include the quotes and respective author names. In order to get the format of the csv file, kindly refer to ```sample_quotes_author_file.csv```.
5. The method "get_five_hastags()" fetched 5 hastags randomly from the hastag file. If you want to include number of hastags more or less than 5 then kindly replace the number with 5.
6. Now in order to schedule the post periodically, appropritely do that using the crontab if you don't want to continuosly run the python program or else use the time.sleep() method specifying the interval time.
7. Execute ```instagram_auto_poster.py``` as Step 6.

## Dependencies

- Python3 any version
- Python package: time, pandas==1.0.3, Pillow==7.1.1, wrapt==1.11.2, math, instabot, random

```pip3 install time pandas==1.0.3 Pillow==7.1.1 wrapt==1.11.2 math instabot random```
