import random
data = 'qwertyuiopasdfghjklzxcvbnm'
data_password = 'qwertyuiopasdfghjklzxcvbnm123456789!-_'
def get_random_name(n=5):
    return ''.join(random.choices(data, k=n)).capitalize()

def get_random_email():
    return get_random_name(8).lower() + '@' + get_random_name(4).lower() + '.com'

def get_random_password():
    return ''.join(random.choices(data_password, k=8))




if __name__ =='__main__':
    print(get_random_name())
    print(get_random_name(8))
    print(get_random_email())
    print(get_random_email())
    print(get_random_password())
    print(get_random_password())
