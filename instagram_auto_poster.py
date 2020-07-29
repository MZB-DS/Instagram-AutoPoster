from PIL import Image, ImageDraw, ImageFont
import textwrap
import math
from instabot import Bot
import time
import pandas as pd
import random

hashtags=[]

f=open("INSTAGRAM_HASHTAGS_FILENAME.txt") # Enter the filename with the path of the instagram hastags you want to choose among to include in the caption.

for tags in f:
    hashtags.append(str(tags))

bot = Bot()
  
bot.login(username = "USERNAME",  # Enter your instagram username
          password = "PASSWORD")  # Enter your instagram password

input_image= Image.open('cream_background.jpg') # This is the background on which we will be masking the quotes and author name.

quotes_author_df= pd.read_csv("QUOTES_WITH_AUTHORNAMES_FILENAME.csv") # Enter the path and filename of the csv file in which we will include the quotes and respective author names

quotes_author_df = quotes_author_df.reset_index()

quotes_author_df.fillna("Empty",inplace=True)

# Below method takes the quotes, authorname and any five randomly chosen hashtags from the hashtag file and convert it into an image.
# It will then automatically post the image on the provided instagram account.
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
    
    # Code logic to centerly align the quotes and author name and also limiting the words per line as per the length of the quote.
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

# Picks any random 5 hashtags from the given hashtag files.
def get_five_hastags(hashtags_list):
    Random_list_index=[]
    for i in range(0, 5):
        Random_list_index.append(random.randint(0, len(hashtags_list)-1))

    combined_hashtags=""

    for i in Random_list_index:
        combined_hashtags=combined_hashtags+" "+str(hashtags_list[i])

    return combined_hashtags

# Code starts from here and picks the quotes and respective author name from the given csv file and calls the mask_image method for image masking and
# Auto posting on the instagram page.
for i in tqdm(range(0,quotes_author_df.shape[0])):
    random_five_hastags=get_five_hastags(hashtags)
    mask_image(quotes_author_df['Quote'][i],quotes_author_df['By'][i],random_five_hastags)
