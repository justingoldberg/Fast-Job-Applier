"""
[insert Greg utilities explanation]
Remember to include this module with your script if 
sending it to a different machine.
$Rev: 21 $

"""

import re
import os
import sys
import time
import datetime
from math import log,floor

#Constants:
PythonLibraryDirectory=r'C:\Python23\Lib'
Python23Keywords=["and","del","for","is","raise","assert","elif","from","lambda","return","break","else","global","not","try","class","except","if","or","while","continue","exec","import","pass","yield","def","finally","in","print"]
posInfinity=1e309 #poor man's pos infinity!

#make some kind of samples ref

#Function Mappings:
ascii=ord #who would remember 'ord'!!!
backascii=chr

def getAppPrefix():
    """Return the location the app is running from
    """
    isFrozen = False
    try:
        isFrozen = sys.frozen
    except AttributeError:
        pass
    if isFrozen:
        appPrefix = os.path.split(sys.executable)[0]
    else:
        appPrefix = os.path.split(os.path.abspath(sys.argv[0]))[0]
    return appPrefix
    
def join_file_and_app_path(filename):
    return os.path.join(getAppPrefix(),filename)


#def replace_print_with_log(yourScriptPath):
#"""
#When I'm ready to finalize a program, instead of deleting all the debugging 
#print statements, why not have them print to a log file?
#Better than "sys.stdout = file('log.txt', 'w')" because you can log and add new
#print statements that actually print.
#"""
#   Add global log file to script: 
#   ---GLOBALS------:
#   LOGFILE=file('log.txt', 'w')
#   add logging function to script:
#   def log(*args):
#       printstr=[str(arg) for arg in args]
#       printstr=",".join(printstr)+'\n'
#       LOGFILE.write(printstr)
#   replace: \(^ *\)print \([^#]*\)
#    with: \1log(\2)
    
#def eject_cdrom():
#    """eject cd tray"""
#    import pygame
#    cd=pygame.cdrom.CD(0)
#    cd.init()
#    cd.eject()

#class Infinity(int): Implement later
#    def __init__(self):
#        int.__init__(self)
#        self.sign = 1
#    def __str__(self):
#        return "%sInfinity" % {-1: "-", 1: ""}[self.sign]
#    def __repr__(self):
#         return "<%s>" % self
#    def __cmp__(self):
#        return True #?

#classes

#class SuperList(list):
#    def find(self,item):pass
#    def freq(self):pass
#    def make_unique(self):pass
#    def cut(self,size):pass
#    def exact_sum(self):pass
#    def average(self):pass
#    def std_dev(self):pass
#    def index_me(self):
#        """Put values into internal dict so finds are faster"""
#        pass
#    def make_table(self,format):
#        """return html table or csv table"""
#        pass

#New Utility Functions

def enquote(string,quotechar='"'):
    return quotechar + string + quotechar

print enquote('greg')
print enquote('greg','u')

def baseconvert(number,fromdigits,todigits):
    """ converts a "number" between two bases of arbitrary digits

    The input number is assumed to be a string of digits from the
    fromdigits string (which is in order of smallest to largest
    digit). The return value is a string of elements from todigits
    (ordered in the same way). The input and output bases are
    determined from the lengths of the digit strings. Negative 
    signs are passed through.

    decimal to binary
    >>> baseconvert(555,10,2)
    '1000101011'

    binary to decimal
    >>> baseconvert('1000101011',2,10)
    '555'

    integer interpreted as binary and converted to decimal (!)
    >>> baseconvert(1000101011,2,10)
    '555'

    base10 to base4
    >>> baseconvert(99,10,4)
    '1203'

    base4 to base5 (with alphabetic digits)
    >>> baseconvert(1203,"0123","abcde")
    'dee'

    base5, alpha digits back to base 10
    >>> baseconvert('dee',"abcde",BASE10)
    '99'

    decimal to a base that uses A-Z0-9a-z for its digits
    >>> baseconvert(257938572394L,BASE10,BASE62)
    'E78Lxik'

    ..convert back
    >>> baseconvert('E78Lxik',BASE62,BASE10)
    '257938572394'

    binary to a base with words for digits (the function cannot convert this back)
    >>> baseconvert('1101',BASE2,('Zero','One'))
    'OneOneZeroOne'

    """
    #letter sets to use
    BASE2 = "01"
    BASE4 = "0123"
    BASE10 = "0123456789"
    BASE16 = "0123456789ABCDEF"
    BASE62 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz"
    if '62' in str(fromdigits):
        fromdigits=BASE62
    elif '16' in str(fromdigits):
        fromdigits=BASE16
    elif '10' in str(fromdigits):
        fromdigits=BASE10
    elif '4' in str(fromdigits):
        fromdigits=BASE4
    elif '2' in str(fromdigits):
        fromdigits=BASE2
    else:
        print 'valid bases are 2,4,10,16,and 62'
        return
    if '62' in str(todigits):
        todigits=BASE62
    elif '16' in str(todigits):
        todigits=BASE16
    elif '10' in str(todigits):
        todigits=BASE10
    elif '4' in str(todigits):
        todigits=BASE4
    elif '2' in str(todigits):
        todigits=BASE2
    else:
        print 'valid bases are 2,4,10,16,and 62'
        return
    
    if str(number)[0]=='-':
        number = str(number)[1:]
        neg=1
    else:
        neg=0

    # make an integer out of the number
    x=long(0)
    for digit in str(number):
       x = x*len(fromdigits) + fromdigits.index(digit)
    
    # create the result in base 'len(todigits)'
    res=""
    while x>0:
        digit = x % len(todigits)
        res = todigits[digit] + res
        x /= len(todigits)
    if neg:
        res = "-"+res

    return res
    
def bin(number):
    """dec number to binary"""
    #later add 8 bit padding.
    return baseconvert(number,10,2)
    
def dec(number):
    """binary number to decimal"""
    return baseconvert(number,2,10)

def unhex(number):
    """hex number to decimal"""
    return baseconvert(number,16,10)
    
#misc utility functions:
def time_24HRto12HR(sHH_MM,AMPM=True,removeleading0=True):
    """Converts miltary time to regular time, input string in format HH:MM"""
    temp=list(time.localtime())
    temp[3]=int(sHH_MM[0:2].replace(":",""))
    temp[4]=int(sHH_MM[3:5].replace(":",""))
    if AMPM:returnval= time.strftime('%I:%M%p',temp)
    else:returnval= time.strftime('%I:%M',temp)
    if not removeleading0:return returnval
    else:
        if returnval[0]=='0':return returnval[1:]
        else:return returnval

def getparentdirectory(fileinput):
    """returns the parent dir as a string given a windows file path or a file"""
    try:return os.path.dirname(fileinput)
    except TypeError:
        try:return os.path.dirname(fileinput.name)
        except:
            print "Unexpected error:", sys.exc_info()[0]
            raise
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise

def cleanhex(number,padtowidth=2):
    """converts base10 to hex and pads to padtowidth and
    removes nasty 0x junk.  Caution, accepts
    nonnumeric inputs and just passes them through."""
    #in future calc max value for padtowidth,
    #and return min(regvalue,maxval)
    if str(number).isdigit():
        number=int(number)
        value=hex(number)
        value=value.upper()
        value=value[2:]
        while len(value)<padtowidth:
            value='0' + value
    else:
        value=number
    return value

def findinlist(item,alist):
    """just like str.find() but for a list
    (someday this will be a method in my
    list subclass customized just for me)"""
    for i,var in enumerate(alist):
        if var==item:return i
    return -1

def pad(strItem,padtowidth,padchar=' ',padbeforeword=False):
    """enter a string like 'Greg', and a length like 8, and
    this fellow will return 'Greg    '.  Pretty simple really.
    """
    if len(strItem)<padtowidth:
        if padbeforeword==False:
            for i in range(len(strItem),padtowidth,len(padchar)):
                strItem+=padchar
        else:
            for i in range(len(strItem),padtowidth,len(padchar)):
                strItem=padchar + strItem
    return strItem

def freq(ListOfItems,desc=True):
    """calculates freq. of each item in a list, 
    returns a list of tuples (item,count) ordered by count
    asc. or desc. per parm: desc."""
    dctItemsCount={}
    for item in ListOfItems:
        if dctItemsCount.has_key(str(item)):dctItemsCount[str(item)]+=1
        else:dctItemsCount[str(item)]=1
    lstFreq=dctItemsCount.items()
    if desc:lstFreq.sort(lambda y,x: x[1]-y[1]) #descending order
    else: lstFreq.sort(lambda x,y: x[1]-y[1]) #ascending order   
    return lstFreq

def spitsearch(text,lstCharsToSpit):
    """Go through text and spit out chars"""
    for i in text:
        if i in lstCharsToSpit:
            print i

def CutList(ListToUse,MaxItems):
    """Cuts list to the given size, MaxItems, appends number of
    remaining list items (those left out) as last value in new list."""
    ListLen=len(ListToUse)
    if ListLen>MaxItems:
            ListToUse=ListToUse[0:MaxItems]
            ListToUse.append("+" + str(ListLen-MaxItems) + " more items")
    return ListToUse

def FindInAnyStringMember(StringToFind,ListToLookIn,ViceVersa=False):
    """
    Answers "is my word a substring of any member of this list?" When ViceVersa=False
    and "is any member of this part a substring of my word?" when ViceVersa=True
    """
    if ViceVersa:
        for member in ListToLookIn:
            if StringToFind.upper().strip().find(member.upper().strip())>-1:
                return True
        return False
    else:
        for member in ListToLookIn:
            if member.upper().strip().find(StringToFind.upper().strip())>-1:
                return True
        return False
def StrInList(StringToFind,ListToLookIn):
    """Is my string in any member of this list?"""
    return FindInAnyStringMember(StringToFind,ListToLookIn)

def partialstringindex(StringToFind,ListToLookIn):
    for pos,member in enumerate(ListToLookIn):
        if member.upper().strip().find(StringToFind.upper().strip())>-1:
            return pos
    return -1

def age(birthdate):
    """What a thing to have to write myself!
    >birthday can be a datetime.datetime, datetime.date or a string like at
    least yyyy-mm-dd but can be 2005-06-20 22:22:44
    """
    birthdate=str(birthdate)
    dtstart=datetime.datetime(int(birthdate[0:4]),int(birthdate[5:7]),
    int(birthdate[8:10]))
    dtnow=datetime.datetime.now()
    return (dtnow-dtstart).days/365

def FloatingPointBinary(base10number,double=False,verbose=False):
    """Return a binary representation of a IEEE Standard 754 floating point
    single.  verbose lists sign, exponent, and significand in binary
    and decimal."""
    """Reference:
    :                Sign     Exponent   Fraction   Bias
    Single Precision 1 [31]   8  [30-23] 23 [22-00] 127
    Double Precision 1 [63]   11 [62-52] 52 [51-00] 1023
    """
    if base10number==0:
        exponentbit='00000000'
        fractionbit='00000000000000000000000'
    #find sign bit:
    if base10number<0:signbit='1'
    else:signbit='0'
    exponentbit=pad(bin(floor(log(base10number,10))+127),8,' ',True)
    #detect overflow here
    
    return 0 #not yet implemented

def EnumerateList(ListOfItems):
    """write out every possible order of the items in the input list"""
    #try making a big n dimensional table?
    pass

def simplefilerename(folderpath,basename,baseExt):
    """Rename all files in a folder to the basename+count+.baseExt"""
    count=1
    for filename in os.listdir(folderpath):
        filepathold=os.path.join(folderpath,filename)
        newname=basename+str(count)+r'.'+baseExt
        filepathnew=os.path.join(folderpath,newname)
        os.rename(filepathold,filepathnew)
        count+=1

def simplefileappend(folderpath,foldername='aggregation.txt'):
    """Not yet operational
    allcontent=file(foldername)
    for filename in os.listdir(folderpath):
        content=file(filename).read()
        allcontent.write(content)
    """
    pass

def make_unique(alist):
    """Remove duplicates from a list"""
    tempdict={}
    newlist=[]
    for item in alist:
        if tempdict.has_key(str(item)):
            pass
        else:
            tempdict[str(item)]=1 #add word to track
            newlist.append(item)
    return newlist

def file_exists(filepath):
    """Does a file exist or not, returns true,false"""
    try:
        test=file(filepath)
        test.close()
        return True
    except:
        return None

def sanitize(string):
    """Returns a string safe to use as a filename, etc"""    
    sanitization_pattern=re.compile(r'[^\w]|:\*!/') #Chars to remove
    safechar='-' #url safe replacement char
    return sanitization_pattern.sub(safechar,string)
    
def msum(iterable,start=0,abs=abs):
    """"
    Binary or Decimal floating point summation accurate to full precision.
    
    Description:
    Completely eliminates rounding errors during summation by keeping a list of partial sums at various precisions.

    Details:    
    The rounded sum of x+y is stored in hi and the roundoff error is stored in lo. Together, hi+lo are an exact summation of x+y.
    The inner loop applies hi/lo summations to each entry so that the list of partial sums remains exact. Also, the list of partial summations is kept in increasing order of magnitude. Only the last entry in the list may be zero. The partial sums are non-overlapping (the lowest non-zero bit of the larger value is greater than the highest bit of the smaller value).
    The slice assignment after the inner loop is equivalent to del partials[i:] followed by partials.append(x). The slice assignment elegantly captures the logic for three cases where the list shrinks, grows, or stays the same size between iterations of the outer loop.
    In practice, the list of partial sums rarely has more than a few entries. This gives a miniml memory footprint and O(n) running time.
    The function is generic and works with Decimal instances as well as floats. To work accurately with complex numbers, the real and imaginary components should be summed separately.
    For proof of correctness, see Theorem 10 in Shewchuk's "Adaptive Precision Floating-Point Arithmetic and Fast Robust Geometric Predicates".
    There are other recipes that mitigate roundoff errors during floating point summation (see recipe #298339 for example). This one goes beyond mitigation and is provably exact. Other features include O(n) runtime, a tiny memory footprint, accepting any iterable input, and working with Decimal objects (or any custom object that can be added, subtracted, and has meaningful absolute value comparisons).
    Tim Peters provided a good test case that defeats some other attempts at accurate summation:
    >>> print msum([1, 1e100, 1, -1e100] * 10000)
    20000.0    
    """
    partials = []               # sorted, non-overlapping partial sums
    for x in iterable:
        i = 0                   # cursor for writing-out new partials
        for y in partials:
            if abs(x) < abs(y):
                x, y = y, x
            hi = x + y
            lo = y - (hi - x)
            if lo:
                partials[i] = lo
                i += 1
            x = hi
        partials[i:] = [x]
    return sum(partials, start)
    
