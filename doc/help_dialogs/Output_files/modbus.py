
import prettytable
import re
from PyQt5.QtWidgets import QApplication
def u(x):
    return str(x)
if True:  #here just to achieve the indent
    if True:
# ----- Cut below ---------------------------------------------

        # autogenerated help pasted below

        newline = "\n"  #@UnusedVariable
        helpstr = ""
        helpstr += "<head><style>"
        helpstr += "td, th {border: 1px solid #ddd;  padding: 6px;}"
        helpstr += "th {padding-top: 6px;padding-bottom: 6px;text-align: left;background-color: #0C6AA6; color: white;}"
        helpstr += "</style></head>"
        helpstr += "<body>"
        helpstr += "<b>" + u(QApplication.translate('HelpDlg','MODBUS',None)) + "</b>"
        tbl_Modbustop = prettytable.PrettyTable()
        tbl_Modbustop.header = False
        tbl_Modbustop.add_row([u(QApplication.translate('HelpDlg','The MODBUS device corresponds to input channels1 and 2.. The MODBUS_34 extra device adds input channels 3 and 4.',None))+newline+u(QApplication.translate('HelpDlg','',None))+newline+u(QApplication.translate('HelpDlg','Inputs with slave id set to 0 are turned off.',None))+newline+u(QApplication.translate('HelpDlg','',None))+newline+u(QApplication.translate('HelpDlg','Modbus function 3 "read holding register" is the standard. Modbus function 4 triggers the use of "read input register". Input registers (fct 4) usually are from 30000-39999.',None))+newline+u(QApplication.translate('HelpDlg','',None))+newline+u(QApplication.translate('HelpDlg','Most devices hold data in 2 byte integer registers. A temperature of 145.2C is often sent as 1452. In that case you have to set the divider to "x/10".',None))+newline+u(QApplication.translate('HelpDlg','',None))+newline+u(QApplication.translate('HelpDlg','Few devices hold data as 4 byte floats in two registers. Tick the Float flag in this case.',None))])
        helpstr += tbl_Modbustop.get_html_string(attributes={"width":"100%","border":"1","padding":"1","border-collapse":"collapse"})
        helpstr += "</body>"
        helpstr = re.sub(r"&amp;#160;", r"&#160;",helpstr)

        # autogenerated help pasted above

# ----- Cut above ---------------------------------------------
outfile = open('../output_files/modbus.html','w')
outfile.write(helpstr)
outfile.close()
outfile = open('../output_files/help.html','w')
outfile.write(helpstr)
outfile.close()