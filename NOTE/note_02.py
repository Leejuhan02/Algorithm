url = "https://google.com"
my_str = url.replace("https://", "")
my_str = my_str[:my_str.index(".")] #[0:4]
a= str(len(my_str))
b= str(my_str.count("e"))
password = my_str[:3] + a + b + "!"
print(password)