import pandas as pd
import re

# Import data using pandas with read_csv 
posts_csv = pd.read_csv('files/posts-100.csv')
print(type(posts_csv), "\n")
print(posts_csv, "\n")
print(posts_csv.head(), "\n")
print(posts_csv.head(3), "\n")

# You can get the numpy array from the DataFrame
print(type(posts_csv.values), "\n")
print(posts_csv.values, "\n")

# You can read a small number of lines too
posts_small = pd.read_csv('files/posts-100.csv', nrows=3)
print(posts_small, "\n")

posts_small = pd.read_csv('files/posts-100.csv', nrows=3, skiprows=3)
print(posts_small, "\n")

# Use a lambda to specify which rows to skip
posts_odd = pd.read_csv('files/posts-100.csv', skiprows=lambda x: x % 2 != 0)
print(posts_odd.head(), "\n")

# You can also specify that you want to load only certain columns
posts_columns = pd.read_csv('files/posts-100.csv', usecols=[0,8])
print(posts_columns.head(5), "\n")

# The DataFrame gives a name to columns, but this does not look right
print(posts_columns.columns, "\n")

# So we specify that the file does not have a header, and now labels are added automatically
posts_no_header = pd.read_csv('files/posts-100.csv', header=None)
print(posts_no_header, "\n")
print(posts_no_header.columns, "\n")

# And you can add a prefix for column names when no header info exists
posts_prefix = pd.read_csv('files/posts-100.csv', header=None, prefix='Col')
print(posts_prefix.columns, "\n")

# And you can add column names
header_fields = ['New_Id', 'New_PostTypeId', 'New_CreationDate', 'New_Score', 'New_ViewCount', 'New_LastActivityDate', 'New_Title', 'New_Tags', 'New_AnswerCount', 'New_CommentCount', 'New_FavoriteCount', 'New_ClosedDate']
posts_add_header = pd.read_csv('files/posts-100.csv', names=header_fields)
print(posts_add_header, "\n")

# Even easier if headers are included in the file
posts_header = pd.read_csv('files/posts-100-header.csv') 
print(posts_header.columns, "\n")

# Headers are important because you can use them to refer to columns
print(posts_header['AnswerCount'].head(), "\n")
print(posts_header[['Id','PostTypeId']].head(), "\n")

# Although you might want to actually remove the headers
print(pd.read_csv('files/posts-100-header.csv', skiprows=1).head(), "\n")

# Specify types
print(pd.read_csv('files/posts-100-header.csv', usecols=[0, 1, 2, 7]).head(), "\n")
print(pd.read_csv('files/posts-100-header.csv', usecols=[0, 1, 2, 7]).columns, "\n")
print(pd.read_csv('files/posts-100-header.csv', usecols=[0, 1, 2, 7]).dtypes, "\n")
print(pd.read_csv('files/posts-100-header.csv', usecols=[0, 1, 2, 7], dtype={'PostTypeId': str}).dtypes, "\n")
print(pd.read_csv('files/posts-100-header.csv', usecols=[0, 1, 2, 7], dtype={'PostTypeId': float}).dtypes, "\n")

# Apply a function with a regular expression
posts_tags = pd.read_csv('files/posts-100-header.csv', usecols=[0, 1, 2, 7], converters={'Tags': lambda x: re.findall('<[A-Za-z0-9_-]*>',x)})
print(posts_tags.head(5), "\n")

# Work with dates too
print(type(pd.read_csv('files/posts-100-header.csv', usecols=[0, 1, 2, 7])['CreationDate'][0]), "\n")
posts_date = pd.read_csv('files/posts-100-header.csv', usecols=[0, 1, 2, 7], parse_dates=['CreationDate'])
print(type(posts_date['CreationDate'][0]), "\n")

# Let's see some missing values
posts_missing = pd.read_csv('files/posts-100-header.csv', usecols=[0, 3, 4, 8, 9, 10])
print(posts_missing, "\n")

# Work with missing values
# na_filter argument looks for values and identifies any that may be NaN, such as blank cells or various iterations of “NA” (“N/A”, “NA”, “NaN”,...). For the value, it places a NaN value (if set to True)
print(pd.read_csv('files/posts-100-header.csv', usecols=[0, 3, 4, 8, 9, 10], na_filter=False).head(), "\n")
print(pd.read_csv('files/posts-100-header.csv', usecols=[0, 3, 4, 8, 9, 10], na_filter=True).head(), "\n")

# Now with a tsv file, there is an error 
try:
    posts_tsv = pd.read_csv('files/posts-100.tsv')
except Exception as e:
    print(e, "\n")

# Unless you set sep or delimiter
posts_tsv = pd.read_csv('files/posts-100.tsv', sep='\t')
print(posts_tsv.head())

# Can use read_table instead
posts_tsv =  pd.read_table('files/posts-100.tsv')
print(posts_tsv.head())

# Import text files with special encoding, such as UTF-8
posts_utf8 = pd.read_csv('files/posts-100-header.csv', encoding='utf-8')
print(posts_utf8, "\n")

# Import from a URL
remote_file = 'https://raw.githubusercontent.com/xmorera/sample-data/main/posts-100.csv'
posts_url = pd.read_csv(remote_file, header=None)
print(posts_url.head(), "\n")