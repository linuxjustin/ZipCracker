###@@@###Zip Cracker ###@@###
justin = '''
+=======================================+
|..........Zip Cracker............................................|
+--------------------------------------------------------------+
|#Author: JUSTIN |
|#Contact: https://github.com/linuxjustin/ZipCracker|
|#Date: 11/08/2017 |
|#this tools just for test |
|#i dont' need the opportunity to hack |
+=======================================+
|..........Zip Cracker...........................................|
+-------------------------------------------------------------+
'''
print " Usage: " + "-f <zip file> -d <dict> "
print justin
import zipfile
import optparse
from threading import Thread
def a(z,password):
    try:
        z.extractall(pwd=password)
        print "!!PASSWORD= " + password + '\n'
    except:
        pass
    def main():
        parse = optparse.OptionParser("Usage: " + "-f <zip file> -d <dict>")
        parse.add_option("-f",dest="jus",type="string",help="zip file")
        parse.add_option("-d",dest="tin",type="string",help="password file")
        (options,args) = parse.parse_args()
        if (options.jus == None) | (options.tin == None):
            print parse.usage
            exit(0)
        else:
            jus = options.jus
            tin = options.tin
            z=zipfile.ZipFile(jus)
            pq=open(tin)
            for x in pq.readlines():
                password = x.strip('\n')
                t = Thread(target=a,args=(z,password))
                t.start()
                if __name__ == '__main__':
                    main()
