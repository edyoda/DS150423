# File Handling
# it is use to store data the permanently in the file

# Types of file 
# 1. Text file - ascii value
# 2. Binary file - images, video, audio

# Modes for text files :

# r ---> reads the data in the file
#   ---> throws an error if file doesn't exist
#   ---> it's a default mode

# w ---> writes the data in the file
#   ---> creates the file, if it doesn't exist
#   ---> if file exist, it overwrites it

# a ---> appends the data in the file
#   ---> creates the file, if it doesn't exist
#   ---> if file exist, it appends the data with previous record

# r+ ---> reads the data
#    ---> writes the data
#    ---> throws error if file doesn't exist

# w+ ---> writes the data
#    ---> reads the data
#    ---> creates the file
#    ---> if file exist, it overwrites the data

# a+ ---> appends the data
#    ---> reads the data
#    ---> creates the file
#    ---> if file exist, it appends the data

# Modes for binary files 
# rb
# wb
# ab
# rb+
# wb+
# ab+