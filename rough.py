# lst = [1, 2, 3]
# my_str = "mlosp playlist"
# my_int = 155

# # print(type(my_int))
# lst.clear
# print(lst)

from  oops_proj import chatbook

# function vs method below

# lst = [1, 2, 3]

# function
# a1 = len(lst)
# print(a1)

# Method
user1 = chatbook()
print(user1.id)

# Using static method directly from class rather than obj
chatbook.set_id(10)
user2 = chatbook()
print(user2.id)

user3 = chatbook()
print(user3.id)
# user2 = chatbook()
# print(user2.id)

# user3 = chatbook()
# print(user3.id)

# user1.sendmsg()


# print(user1._chatbook__name)


# # Getter and Setter
# print(user1.get_name())
# user1.set_name("Agent X")
# print(user1.get_name())