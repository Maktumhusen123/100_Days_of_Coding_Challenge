# # FileNotFound Error
# with open("file.txt", "r") as f:
#     f.read()
#
# # Key Error
# a_dict = {"key": "value"}
# a = a_dict["non_exist_key"]
#
# # IndexError
# a_list = ["mango", "apple"]
# element = a_list[3]
#
# # Type Error
# text = "abc"
# print(text + 5)

try:
    file = open("file.txt")
    a_dict = {"key": "value"}
    print(a_dict["saksa"])
except FileNotFoundError:
    file = open("file.txt", "w")
    file.write("Something....")
    print("file was not present, so we created file now")
    # do not use bare exception as it will ignore if many errors are present in try block.
    # Use specific error exception
except KeyError as e:
    print(f"the key {e} does not exist")
else:
    print(file.read())
    # this block gets executed when try block is succssful
finally:
    print("File can be closed here")
    # this block executes whether the error occurs or not
