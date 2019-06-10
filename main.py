#!/usr/bin/env python
import student;
import json
def main():
    s = student.Student()
    s.type = "student"
    s.append({"name":"appdemo","version":"v1.0"})
    s.append({"name":"appdemo2","version":"v1.1"})
    s.printInfo()
    for item in s.items :
        print(json.dumps(item))
if __name__ == '__main__':
    main()
    