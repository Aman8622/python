arn = "arn:aws:iam::123456789012:user/john"
username = arn.split("/")
user = username[1]
print(user)