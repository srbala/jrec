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

    if window('Protocol Buffer Editor'):
        select_menu('View>>Sorted Field Tree')

        if frame('Create Sorted Tree - DTAR020_tst1.bin:0'):
            select('JTable_10', 'Store_No', '{0, Field}')
            select('JTable_10', 'Dept_No', '{1, Field}')
            select('JTable_10', 'rows:[1],columns:[Field]')
            click('Build Tree')
        close()

        if frame('Tree View - DTAR020_tst1.bin:0'):
            select('net.sf.RecordEditor.utils.swing.treeTable.JTreeTable_10', 'rows:[13],columns:[Dept_No]')
            assert_content('net.sf.RecordEditor.utils.swing.treeTable.JTreeTable_10', [ ['', '', '', '', '', '', '', ''],
['', '', '', '', '', '', '', ''],
['', '', '63604808', '20', '40118', '170', '1', '4870'],
['', '', '', '', '', '', '', ''],
['', '', '69684558', '20', '40118', '280', '1', '19000'],
['', '', '69684558', '20', '40118', '280', '-1', '-19000'],
['', '', '69694158', '20', '40118', '280', '1', '5010'],
['', '', '', '', '', '', '', ''],
['', '', '62684671', '20', '40118', '685', '1', '69990'],
['', '', '62684671', '20', '40118', '685', '-1', '-69990'],
['', '', '', '', '', '', '', ''],
['', '', '', '', '', '', '', ''],
['', '', '61664713', '59', '40118', '335', '1', '17990'],
['', '', '61664713', '59', '40118', '335', '-1', '-17990'],
['', '', '61684613', '59', '40118', '335', '1', '12990'],
['', '', '', '', '', '', '', ''],
['', '', '68634752', '59', '40118', '410', '1', '8990'],
['', '', '', '', '', '', '', ''],
['', '', '60694698', '59', '40118', '620', '1', '3990'],
['', '', '60664659', '59', '40118', '620', '1', '3990'],
['', '', '', '', '', '', '', ''],
['', '', '60614487', '59', '40118', '878', '1', '5950'],
['', '', '', '', '', '', '', ''],
['', '', '', '', '', '', '', ''],
['', '', '68654655', '166', '40118', '60', '1', '5080'
],
['', '', '', '', '', '', '', ''],
['', '', '69624033', '166', '40118', '80', '1', '18190'],
['', '', '60604100', '166', '40118', '80', '1', '13300'],
['', '', '', '', '', '', '', ''],
['', '', '68674560', '166', '40118', '170', '1', '5990']
])
            select('net.sf.RecordEditor.utils.swing.treeTable.JTreeTable_10', 'rows:[13],columns:[Dept_No]')
        close()

        click('Export in another format')

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
['', '', '', '', '63604808', '20', '40118', '170', '1', '4870', 'True', ''],
['', '', '', '', '280', '', '', '', '', '', '', ''],
['', '', '', '', '69684558', '20', '40118', '280', '1', '19000', 'True', ''],
['', '', '', '', '69684558', '20', '40118', '280', '-1', '-19000', 'True', ''],
['', '', '', '', '69694158', '20', '40118', '280', '1', '5010', 'True', ''],
['', '', '', '', '685', '', '', '', '', '', '', ''],
['', '', '', '', '62684671', '20', '40118', '685', '1', '69990', 'True', ''],
['', '', '', '', '62684671', '20', '40118', '685', '-1', '-69990', 'True', ''],
['', '', '', '', '59', '', '', '', '', '', '', ''],
['', '', '', '', '335', '', '', '', '', '', '', ''],
['', '', '', '', '61664713', '59', '40118', '335', '1', '17990', 'True', ''],
['', '', '', '', '61664713', '59', '40118', '335', '-1', '-17990', 'True', ''],
['', '', '', '', '61684613', '59', '40118', '335', '1', '12990', 'True', ''],
['', '', '', '', '410', '', '', '', '', '', '', ''],
['', '', '', '', '68634752', '59', '40118', '410', '1', '8990', 'True', ''],
['', '', '', '', '620', '', '', '', '', '', '', ''],
['', '', '', '', '60694698', '59', '40118', '620', '1', '3990', 'True', ''],
['', '', '', '', '60664659', '59', '40118', '620', '1', '3990', 'True', ''],
['', '', '', '', '878', '', '', '', '', '', '', ''],
['', '', '', '', '60614487', '59', '40118', '878', '1', '5950', 'True', ''],
['', '', '', '', '166', '', '', '', '', '', '', ''],
['', '', '', '', '60', '', '', '', '', '', '', ''],
['', '', '', '', '68654655', '166', '40118', '60', '1', '5080'
, 'True', ''],
['', '', '', '', '80', '', '', '', '', '', '', ''],
['', '', '', '', '69624033', '166', '40118', '80', '1', '18190', 'True', ''],
['', '', '', '', '60604100', '166', '40118', '80', '1', '13300', 'True', ''],
['', '', '', '', '170', '', '', '', '', '', '', ''],
['', '', '', '', '68674560', '166', '40118', '170', '1', '5990', 'True', '']
])
            select('net.sf.RecordEditor.utils.swing.treeTable.JTreeTable_10', 'rows:[14],columns:[Xml~Namespace]')
            click('Close')
##            select('net.sf.RecordEditor.utils.swing.treeTable.JTreeTable_10', 'rows:[14],columns:[Xml~Namespace]')
        close()

##        if frame('Tree View - DTAR020_tst1.bin:0'):
##            select('net.sf.RecordEditor.utils.swing.treeTable.JTreeTable_10', 'rows:[13],columns:[Dept_No]')
##        close()

##        window_closed('Record Editor')
    close()

    pass
