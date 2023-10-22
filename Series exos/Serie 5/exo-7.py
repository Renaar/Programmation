block_num_tel = ""
num_tel = ""
base_num = 0
blocked = []


def get_num_tel():
    global block_num_tel
    global num_tel
    if block_num_tel == "":
        block_num_tel = input("Entrez un numéro à bloquer : ")
        check_length_num(block_num_tel)
    else:
        num_tel = input("Entrez un nouveau numéro de téléphone : ")
        check_length_num(num_tel)


def check_length_num(x):
    global block_num_tel
    global num_tel
    global blocked
    if len(x) != 10:
        print("Numéro incorrect")
        if blocked:
            block_num_tel = "1"
            num_tel = ""
            get_num_tel()
        else:
            block_num_tel = ""
            get_num_tel()
    elif base_num == 0:
        get_base_num(x)
    else:
        is_it_spam(x)


def get_base_num(y):
    global base_num
    base_num = y[:-2]
    create_blocked_list(base_num)


def create_blocked_list(z):
    global base_num
    global blocked
    for i in range(0, 10):
        for j in range(0, 10):
            number = str(z) + str(i) + str(j)
            blocked.append(number)
    get_num_tel()


def is_it_spam(o):
    if o in blocked:
        print("SPAM !")
        get_num_tel()
    else:
        print("OK !")
        get_num_tel()


get_num_tel()
