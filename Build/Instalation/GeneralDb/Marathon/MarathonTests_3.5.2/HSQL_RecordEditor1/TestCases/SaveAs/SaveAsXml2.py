#{{{ Marathon
from default import *
#}}} Marathon

from Modules import commonBits

def test():

    set_java_recorded_version("1.6.0_22")
    if frame(' - Open File:0'):
        select('File', commonBits.sampleDir() + 'DTAR020_tst1.bin')
        click('Edit')
    close()

    if window('Record Editor'):
        select_menu('View>>Sorted Field Tree')

        if frame('Create Sorted Tree - DTAR020_tst1.bin:0'):
            select('JTable_10', 'STORE-NO', '{0, Field}')
            select('JTable_10', 'DEPT-NO', '{1, Field}')
            select('JTable_10', 'rows:[1],columns:[Field]')
            click('Build Tree')
        close()

        if frame('Tree View - DTAR020_tst1.bin:0'):
            select('net.sf.RecordEditor.utils.swing.treeTable.JTreeTable_10', 'rows:[13],columns:[DEPT-NO]')
            assert_content('net.sf.RecordEditor.utils.swing.treeTable.JTreeTable_10', [ ['', '', '', '', '', '', '', ''],
['', '', '', '', '', '', '', ''],
['', '', '63604808', '20', '40118', '170', '1', '4.87'],
['', '', '', '', '', '', '', ''],
['', '', '69684558', '20', '40118', '280', '1', '19.00'],
['', '', '69684558', '20', '40118', '280', '-1', '-19.00'],
['', '', '69694158', '20', '40118', '280', '1', '5.01'],
['', '', '', '', '', '', '', ''],
['', '', '62684671', '20', '40118', '685', '1', '69.99'],
['', '', '62684671', '20', '40118', '685', '-1', '-69.99'],
['', '', '', '', '', '', '', ''],
['', '', '', '', '', '', '', ''],
['', '', '61664713', '59', '40118', '335', '1', '17.99'],
['', '', '61664713', '59', '40118', '335', '-1', '-17.99'],
['', '', '61684613', '59', '40118', '335', '1', '12.99'],
['', '', '', '', '', '', '', ''],
['', '', '68634752', '59', '40118', '410', '1', '8.99'],
['', '', '', '', '', '', '', ''],
['', '', '60694698', '59', '40118', '620', '1', '3.99'],
['', '', '60664659', '59', '40118', '620', '1', '3.99'],
['', '', '', '', '', '', '', ''],
['', '', '60614487', '59', '40118', '878', '1', '5.95'],
['', '', '', '', '', '', '', ''],
['', '', '', '', '', '', '', ''],
['', '', '68654655', '166', '40118', '60', '1', '5.08'],
['', '', '', '', '', '', '', ''],
['', '', '69624033', '166', '40118', '80', '1', '18.19'],
['', '', '60604100', '166', '40118', '80', '1', '13.30'],
['', '', '', '', '', '', '', ''],
['', '', '68674560', '166', '40118', '170', '1', '5.99']
])
            select('net.sf.RecordEditor.utils.swing.treeTable.JTreeTable_10', 'rows:[13],columns:[DEPT-NO]')
        close()

        click('Export')

        if frame('Export - DTAR020_tst1.bin:0'):
##            select('JTabbedPane_16', 'Xml')
            select('File Name_2', 'Xml')
            select('Edit Output File', 'true')
            click('save file')
        close()

        if frame('Tree View - DTAR020_tst1.bin.xml:0'):
            select('net.sf.RecordEditor.utils.swing.treeTable.JTreeTable_10', 'rows:[14],columns:[Xml~Namespace]')
            assert_content('net.sf.RecordEditor.utils.swing.treeTable.JTreeTable_10', [ ['', '', 'UTF-8', '1.0', 'false', '', '', '', '', '', '', ''],
['', '', '', '', 'File', '', '', '', '', '', '', ''],
['', '', '', '', '20', '', '', '', '', '', '', ''],
['', '', '', '', '170', '', '', '', '', '', '', ''],
['', '', '', '', '63604808', '20', '40118', '170', '1', '4.87', 'True', ''],
['', '', '', '', '280', '', '', '', '', '', '', ''],
['', '', '', '', '69684558', '20', '40118', '280', '1', '19.00', 'True', ''],
['', '', '', '', '69684558', '20', '40118', '280', '-1', '-19.00', 'True', ''],
['', '', '', '', '69694158', '20', '40118', '280', '1', '5.01', 'True', ''],
['', '', '', '', '685', '', '', '', '', '', '', ''],
['', '', '', '', '62684671', '20', '40118', '685', '1', '69.99', 'True', ''],
['', '', '', '', '62684671', '20', '40118', '685', '-1', '-69.99', 'True', ''],
['', '', '', '', '59', '', '', '', '', '', '', ''],
['', '', '', '', '335', '', '', '', '', '', '', ''],
['', '', '', '', '61664713', '59', '40118', '335', '1', '17.99', 'True', ''],
['', '', '', '', '61664713', '59', '40118', '335', '-1', '-17.99', 'True', ''],
['', '', '', '', '61684613', '59', '40118', '335', '1', '12.99', 'True', ''],
['', '', '', '', '410', '', '', '', '', '', '', ''],
['', '', '', '', '68634752', '59', '40118', '410', '1', '8.99', 'True', ''],
['', '', '', '', '620', '', '', '', '', '', '', ''],
['', '', '', '', '60694698', '59', '40118', '620', '1', '3.99', 'True', ''],
['', '', '', '', '60664659', '59', '40118', '620', '1', '3.99', 'True', ''],
['', '', '', '', '878', '', '', '', '', '', '', ''],
['', '', '', '', '60614487', '59', '40118', '878', '1', '5.95', 'True', ''],
['', '', '', '', '166', '', '', '', '', '', '', ''],
['', '', '', '', '60', '', '', '', '', '', '', ''],
['', '', '', '', '68654655', '166', '40118', '60', '1', '5.08', 'True', ''],
['', '', '', '', '80', '', '', '', '', '', '', ''],
['', '', '', '', '69624033', '166', '40118', '80', '1', '18.19', 'True', ''],
['', '', '', '', '60604100', '166', '40118', '80', '1', '13.30', 'True', ''],
['', '', '', '', '170', '', '', '', '', '', '', ''],
['', '', '', '', '68674560', '166', '40118', '170', '1', '5.99', 'True', '']
])
            select('net.sf.RecordEditor.utils.swing.treeTable.JTreeTable_10', 'rows:[14],columns:[Xml~Namespace]')
            click('Close')
##            select('net.sf.RecordEditor.utils.swing.treeTable.JTreeTable_10', 'rows:[14],columns:[Xml~Namespace]')
        close()

##        if frame('Tree View - DTAR020_tst1.bin:0'):
##            select('net.sf.RecordEditor.utils.swing.treeTable.JTreeTable_10', 'rows:[13],columns:[DEPT-NO]')
##        close()

##        window_closed('Record Editor')
    close()

    pass
