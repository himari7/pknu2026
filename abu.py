import sys
args = sys.argv

name1 : args[1]
name2 : args[2]
with open('./test_note.txt'.'a') as f:
    f.write(name1 ," ", name2 )
print("입력되었습니다.")