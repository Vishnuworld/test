# # for generating secret key using secrets library...
#
# import secrets
# import string
# print("".join(secrets.choice(string.digits+string.ascii_letters+string
#                              .punctuation)for i in range(50)))
#
#
#
# # pickel turns python objects into bytes...
# import pickle
# a=pickle.dumps({'foo':'bar'})
# print(a)
# b=pickle.loads(b'\x80\x03}q\x00X\x03\x00\x00\x00fooq\x01X\x03\x00\x00\x00barq\x02s.')
# print(b)
#
