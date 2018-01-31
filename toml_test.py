import toml

f = open(".git_cache", "w")
to_write = "['pr 2']\npr='2'\nbranch='test2'\nuser='theodoreear'\n\n "
toml_string = toml.loads(to_write)
toml.dump(toml_string, f)

# f=open("test.toml", "r")
# pr_dict = toml.load(f)
# print(pr_dict['pr 2']['branch'])

f = open(".git_cache", "r")
pr_dict = toml.load(f)
to_write = "['pr 3']\npr='3'\nbranch='test3'\nuser='serayang'\n\n "
to_write = {'pr 3': {"pr" : "3", "branch" : "test3", "user" : "serayang"}}
print(to_write)
print(pr_dict)
pr_dict['pr 3'] = to_write['pr 3']
print(pr_dict)
f = open("test.toml", "w")
toml.dump(pr_dict, f)

# print(to_write)
# toml_string = toml.loads(to_write)
# toml.dump(toml_string, f)