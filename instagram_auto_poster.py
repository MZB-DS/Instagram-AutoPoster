from PIL import Image, ImageDraw, ImageFont
import textwrap
import math
from tqdm import tqdm
from instabot import Bot
import sys
import time
import pandas as pd
import random

hashtags=[]

f=open("INSTAGRAM_HASHTAGS_FILENAME.txt")

for tags in f:
    hashtags.append(str(tags))

bot = Bot()
  
bot.login(username = "USERNAME",  
          password = "PASSWORD")

input_image= Image.open('cream_background.jpg')

quotes_author_df= pd.read_csv("QUOTES_WITH_AUTHORNAMES_FILENAME.csv")

quotes_author_df = quotes_author_df.reset_index()

quotes_author_df.fillna("Empty",inplace=True)

def mask_image(quote,author,random_five_hastags):
    image = input_image.resize((1080,1080))
    draw = ImageDraw.Draw(image)
    text = quote
    font_size = 60

    font_style = ImageFont.truetype(
        'times-new-roman-grassetto.ttf', font_size)

    author_font_style = ImageFont.truetype(
        'times-new-roman-grassetto.ttf', 20)

    para = textwrap.wrap(text, width=23)

    pad=5

    current_h = ((image.size[0])/2)-((math.floor((len(para)/2))+1)*(font_size+pad))
    for line in para:
        w, h = draw.textsize(line, font=font_style)
        draw.text(((image.size[0] - w) / 2, current_h), line, "black",font=font_style)
        current_h += h + pad

    if author!='Empty':
        w, h = draw.textsize(line, font=author_font_style)
        draw.text(((image.size[0] - w) / 2, current_h), "- "+str(author), "black",font=author_font_style)

    filename="PATH_OF_THE_OUTPUT_FILE/Quotes_Image.jpg"

    image.save(filename)
    if author=='Empty':
        bot.upload_photo(filename,caption=quote+"\n.\n.\n.\n{}".format(random_five_hastags))
    else:
        bot.upload_photo(filename,caption=quote+"  - "+author+"\n.\n.\n.\n{}".format(random_five_hastags))

def get_five_hastags(hashtags_list):
    Random_list_index=[]
    for i in range(0, 5):
        Random_list_index.append(random.randint(0, len(hashtags_list)-1))

    combined_hashtags=""

    for i in Random_list_index:
        combined_hashtags=combined_hashtags+" "+str(hashtags_list[i])

    return combined_hashtags

for i in tqdm(range(0,quotes_author_df.shape[0])):
    random_five_hastags=get_five_hastags(hashtags)
    mask_image(quotes_author_df['Quote'][i],quotes_author_df['By'][i],random_five_hastags)
