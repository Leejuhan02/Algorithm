url = "https://google.com"
my_str = url.replace("https://", "")
my_str = my_str[:my_str.index(".")] #[0:4]
password1 = my_str[:3] + str(len(my_str))
print(password1)
