import argparse,string
import secrets as secs

def GeneratePassword(length_password):
    alphabet = string.ascii_letters+string.digits
    return ''.join(secs.choice(alphabet) for i in range(int(length_password)))





parser=argparse.ArgumentParser(description='Generate a  password')
parser.add_argument('-l',help='A length of a password',required=True)

args=parser.parse_args()

argsl=args.l
print(argsl)

if (argsl.isdigit()):
    print(GeneratePassword(argsl))
else:
    print ('The argument is incorrect\n')

#print (GeneratePassword(args.l))
