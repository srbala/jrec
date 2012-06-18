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
            select('JTable_10', 'Dept_No', '{0, Field}')
            select('JTable_10', 'Store_No', '{1, Field}')
            select('JTable_10', 'rows:[1],columns:[Field]')
            click('Build Tree')
        close()

        if frame('Tree View - DTAR020_tst1.bin:0'):
            select('net.sf.RecordEditor.utils.swing.treeTable.JTreeTable_10', 'rows:[9],columns:[DATE]')
            assert_content('net.sf.RecordEditor.utils.swing.treeTable.JTreeTable_10', [ ['', '', '', '', '', '', '', ''],
['', '', '', '', '', '', '', ''],
['', '', '68654655', '166', '40118', '60', '1', '5080'
],
['', '', '', '', '', '', '', ''],
['', '', '', '', '', '', '', ''],
['', '', '69624033', '166', '40118', '80', '1', '18190'],
['', '', '60604100', '166', '40118', '80', '1', '13300'],
['', '', '', '', '', '', '', ''],
['', '', '', '', '', '', '', ''],
['', '', '63604808', '20', '40118', '170', '1', '4870'],
['', '', '', '', '', '', '', ''],
['', '', '68674560', '166', '40118', '170', '1', '5990'],
['', '', '', '', '', '', '', ''],
['', '', '', '', '', '', '', ''],
['', '', '69684558', '20', '40118', '280', '1', '19000'],
['', '', '69684558', '20', '40118', '280', '-1', '-19000'],
['', '', '69694158', '20', '40118', '280', '1', '5010'],
['', '', '', '', '', '', '', ''],
['', '', '', '', '', '', '', ''],
['', '', '61664713', '59', '40118', '335', '1', '17990'],
['', '', '61664713', '59', '40118', '335', '-1', '-17990'],
['', '', '61684613', '59', '40118', '335', '1', '12990'],
['', '', '', '', '', '', '', ''],
['', '', '', '', '', '', '', ''],
['', '', '68634752', '59', '40118', '410', '1', '8990'],
['', '', '', '', '', '', '', ''],
['', '', '', '', '', '', '', ''],
['', '', '60694698', '59', '40118', '620', '1', '3990'],
['', '', '60664659', '59', '40118', '620', '1', '3990'],
['', '', '', '', '', '', '', ''],
['', '', '', '', '', '', '', ''],
['', '', '62684671', '20', '40118', '685', '1', '69990'],
['', '', '62684671', '20', '40118', '685', '-1', '-69990'],
['', '', '', '', '', '', '', ''],
['', '', '', '', '', '', '', ''],
['', '', '60614487', '59', '40118', '878', '1', '5950']
])
            select('net.sf.RecordEditor.utils.swing.treeTable.JTreeTable_10', 'rows:[9],columns:[DATE]')
        close()

##        click('SaveAs')

        select_menu('File>>Export')

        if frame('Export - DTAR020_tst1.bin:0'):
##            select('JTabbedPane_16', 'Fixed')
            select('File Name_2', 'Fixed')
            select('Only export Nodes with Data', 'true')
            select('Edit Output File', 'true')
            select('Keep screen open', 'true')
            select('names on first line', 'true')
##            select('JTable_31', 'rows:[2],columns:[Include]')
            select('names on first line', 'true')
#            select('JTable_31', 'rows:[4],columns:[Include]')
            select('names on first line', 'true')
            select('JTable_28', 'false', '{2, Include}')
            select('JTable_28', 'false', '{4, Include}')
            click('save file')
        close()

        if frame('Table:  - DTAR020_tst1.bin.txt:0'):
            assert_content('JTable_22', [ ['Level_1', 'Level_2', 'Level_3', 'Level_4', 'Keycode_no', 'Store_No', 'Dept_No', 'Sale_Price'],
['File', '60', '166', '', '68654655', '166', '60', '5080'
],
['File', '80', '166', '', '69624033', '166', '80', '18190'],
['File', '80', '166', '', '60604100', '166', '80', '13300'],
['File', '170', '20', '', '63604808', '20', '170', '4870'],
['File', '170', '166', '', '68674560', '166', '170', '5990'],
['File', '280', '20', '', '69684558', '20', '280', '19000'],
['File', '280', '20', '', '69684558', '20', '280', '-19000'],
['File', '280', '20', '', '69694158', '20', '280', '5010'],
['File', '335', '59', '', '61664713', '59', '335', '17990'],
['File', '335', '59', '', '61664713', '59', '335', '-17990'],
['File', '335', '59', '', '61684613', '59', '335', '12990'],
['File', '410', '59', '', '68634752', '59', '410', '8990'],
['File', '620', '59', '', '60694698', '59', '620', '3990'],
['File', '620', '59', '', '60664659', '59', '620', '3990'],
['File', '685', '20', '', '62684671', '20', '685', '69990'],
['File', '685', '20', '', '62684671', '20', '685', '-69990'],
['File', '878', '59', '', '60614487', '59', '878', '5950']
])
            select('JTable_22', 'rows:[0],columns:[8 - 7|Level_2]')
            assert_p('net.sf.RecordEditor.edit.display.BaseDisplay$HeaderToolTips_27', 'Text', '54 - 10|Sale_Price', '54 - 10|Sale_Price')
            assert_p('net.sf.RecordEditor.edit.display.BaseDisplay$HeaderToolTips_27', 'Text', '47 - 7|Dept_No', '47 - 7|Dept_No')
            assert_p('net.sf.RecordEditor.edit.display.BaseDisplay$HeaderToolTips_27', 'Text', '39 - 8|Store_No', '39 - 8|Store_No')
            assert_p('net.sf.RecordEditor.edit.display.BaseDisplay$HeaderToolTips_27', 'Text', '29 - 10|Keycode_no', '29 - 10|Keycode_no')
            assert_p('net.sf.RecordEditor.edit.display.BaseDisplay$HeaderToolTips_27', 'Text', '22 - 7|Level_4', '22 - 7|Level_4')
            assert_p('net.sf.RecordEditor.edit.display.BaseDisplay$HeaderToolTips_27', 'Text', '15 - 7|Level_3', '15 - 7|Level_3')
            assert_p('net.sf.RecordEditor.edit.display.BaseDisplay$HeaderToolTips_27', 'Text', '1 - 7|Level_1', '1 - 7|Level_1')
            select('Layouts', 'Full Line')
            assert_p('JTable_22', 'Text', 'File   280    20            69684558  20      280    19000', '{6, Full Line}')
            click('Close')
        close()

        if frame('Export - DTAR020_tst1.bin:0'):
            select('JTable_28', 'true', '{4, Include}')
            select('JTable_28', 'rows:[4],columns:[Include]')
            select('JTable_28', 'rows:[5],columns:[Include]')
            select('JTable_28', 'false', '{5, Include}')
            select('JTable_28', 'true', '{4, Include}')
            select('space between fields', 'true')
            click('save file')
        close()

        if frame('Table:  - DTAR020_tst1.bin.txt:0'):
            assert_content('JTable_22', [ ['Level_1', 'Level_2', 'Level_3', 'Level_4', 'Keycode_no', 'Store_No', 'Dept_No', 'Qty_Sold'],
['File', '60', '166', '', '68654655', '166', '60', '1'],
['File', '80', '166', '', '69624033', '166', '80', '1'],
['File', '80', '166', '', '60604100', '166', '80', '1'],
['File', '170', '20', '', '63604808', '20', '170', '1'],
['File', '170', '166', '', '68674560', '166', '170', '1'],
['File', '280', '20', '', '69684558', '20', '280', '1'],
['File', '280', '20', '', '69684558', '20', '280', '-1'],
['File', '280', '20', '', '69694158', '20', '280', '1'],
['File', '335', '59', '', '61664713', '59', '335', '1'],
['File', '335', '59', '', '61664713', '59', '335', '-1'],
['File', '335', '59', '', '61684613', '59', '335', '1'],
['File', '410', '59', '', '68634752', '59', '410', '1'],
['File', '620', '59', '', '60694698', '59', '620', '1'],
['File', '620', '59', '', '60664659', '59', '620', '1'],
['File', '685', '20', '', '62684671', '20', '685', '1'],
['File', '685', '20', '', '62684671', '20', '685', '-1'],
['File', '878', '59', '', '60614487', '59', '878', '1']
])
            select('JTable_22', 'rows:[0],columns:[9 - 7|Level_2]')
            assert_p('net.sf.RecordEditor.edit.display.BaseDisplay$HeaderToolTips_27', 'Text', '61 - 8|Qty_Sold', '61 - 8|Qty_Sold')
            assert_p('net.sf.RecordEditor.edit.display.BaseDisplay$HeaderToolTips_27', 'Text', '53 - 7|Dept_No', '53 - 7|Dept_No')
            select('Layouts', 'Full Line')
            assert_content('JTable_22', [ ['Level_1 Level_2 Level_3 Level_4 Keycode_no Store_No Dept_No Qty_Sold'],
['File    60      166             68654655   166      60      1       '],
['File    80      166             69624033   166      80      1       '],
['File    80      166             60604100   166      80      1       '],
['File    170     20              63604808   20       170     1       '],
['File    170     166             68674560   166      170     1       '],
['File    280     20              69684558   20       280     1       '],
['File    280     20              69684558   20       280     -1      '],
['File    280     20              69694158   20       280     1       '],
['File    335     59              61664713   59       335     1       '],
['File    335     59              61664713   59       335     -1      '],
['File    335     59              61684613   59       335     1       '],
['File    410     59              68634752   59       410     1       '],
['File    620     59              60694698   59       620     1       '],
['File    620     59              60664659   59       620     1       '],
['File    685     20              62684671   20       685     1       '],
['File    685     20              62684671   20       685     -1      '],
['File    878     59              60614487   59       878     1       ']
])
            click('Close')
        close()

        if frame('Export - DTAR020_tst1.bin:0'):
            select('names on first line', 'false')
            click('save file')
        close()

        if frame('Table:  - DTAR020_tst1.bin.txt:0'):
            assert_content('JTable_22', [ ['File', '60', '166', '', '68654655', '166', '60', '1'],
['File', '80', '166', '', '69624033', '166', '80', '1'],
['File', '80', '166', '', '60604100', '166', '80', '1'],
['File', '170', '20', '', '63604808', '20', '170', '1'],
['File', '170', '166', '', '68674560', '166', '170', '1'],
['File', '280', '20', '', '69684558', '20', '280', '1'],
['File', '280', '20', '', '69684558', '20', '280', '-1'],
['File', '280', '20', '', '69694158', '20', '280', '1'],
['File', '335', '59', '', '61664713', '59', '335', '1'],
['File', '335', '59', '', '61664713', '59', '335', '-1'],
['File', '335', '59', '', '61684613', '59', '335', '1'],
['File', '410', '59', '', '68634752', '59', '410', '1'],
['File', '620', '59', '', '60694698', '59', '620', '1'],
['File', '620', '59', '', '60664659', '59', '620', '1'],
['File', '685', '20', '', '62684671', '20', '685', '1'],
['File', '685', '20', '', '62684671', '20', '685', '-1'],
['File', '878', '59', '', '60614487', '59', '878', '1']
])
            select('JTable_22', 'rows:[0],columns:[6 - 3|Level_2]')
            select('JTable_22', 'rows:[0],columns:[6 - 3|Level_2]')
            select('Layouts', 'Full Line')
            assert_p('JTable_22', 'Text', 'File 280 20       69694158   20       280     1', '{7, Full Line}')
            assert_content('JTable_22', [ ['File 60  166      68654655   166      60      1       '],
['File 80  166      69624033   166      80      1       '],
['File 80  166      60604100   166      80      1       '],
['File 170 20       63604808   20       170     1       '],
['File 170 166      68674560   166      170     1       '],
['File 280 20       69684558   20       280     1       '],
['File 280 20       69684558   20       280     -1      '],
['File 280 20       69694158   20       280     1       '],
['File 335 59       61664713   59       335     1       '],
['File 335 59       61664713   59       335     -1      '],
['File 335 59       61684613   59       335     1       '],
['File 410 59       68634752   59       410     1       '],
['File 620 59       60694698   59       620     1       '],
['File 620 59       60664659   59       620     1       '],
['File 685 20       62684671   20       685     1       '],
['File 685 20       62684671   20       685     -1      '],
['File 878 59       60614487   59       878     1       ']
])
            click('Close')
        close()

        if frame('Export - DTAR020_tst1.bin:0'):
            select('Only export Nodes with Data', 'true')
            select('JTable_28', 'rows:[4],columns:[Include]')
            select('JTable_28', 'rows:[5],columns:[Include]')
            select('JTable_28', 'rows:[5],columns:[Field Name]')
            select('JTable_28', 'false', '{4, Include}')
            select('JTable_28', 'true', '{5, Include}')
            
            click('save file')
        close()

        if frame('Table:  - DTAR020_tst1.bin.txt:0'):
            assert_content('JTable_22', [ ['File', '60', '166', '', '68654655', '166', '60', '5080'
],
['File', '80', '166', '', '69624033', '166', '80', '18190'],
['File', '80', '166', '', '60604100', '166', '80', '13300'],
['File', '170', '20', '', '63604808', '20', '170', '4870'],
['File', '170', '166', '', '68674560', '166', '170', '5990'],
['File', '280', '20', '', '69684558', '20', '280', '19000'],
['File', '280', '20', '', '69684558', '20', '280', '-19000'],
['File', '280', '20', '', '69694158', '20', '280', '5010'],
['File', '335', '59', '', '61664713', '59', '335', '17990'],
['File', '335', '59', '', '61664713', '59', '335', '-17990'],
['File', '335', '59', '', '61684613', '59', '335', '12990'],
['File', '410', '59', '', '68634752', '59', '410', '8990'],
['File', '620', '59', '', '60694698', '59', '620', '3990'],
['File', '620', '59', '', '60664659', '59', '620', '3990'],
['File', '685', '20', '', '62684671', '20', '685', '69990'],
['File', '685', '20', '', '62684671', '20', '685', '-69990'],
['File', '878', '59', '', '60614487', '59', '878', '5950']
])
##            select('JTable_22', 'rows:[0],columns:[6 - 3|Level_2]')
            assert_p('net.sf.RecordEditor.edit.display.BaseDisplay$HeaderToolTips_27', 'Text', '47 - 10|Sale_Price', '47 - 10|Sale_Price')
            assert_p('net.sf.RecordEditor.edit.display.BaseDisplay$HeaderToolTips_27', 'Text', '39 - 7|Dept_No', '39 - 7|Dept_No')
            select('Layouts', 'Full Line')
            assert_content('JTable_22', [ ['File 60  166      68654655   166      60      5080      '],
['File 80  166      69624033   166      80      18190     '],
['File 80  166      60604100   166      80      13300     '],
['File 170 20       63604808   20       170     4870      '],
['File 170 166      68674560   166      170     5990      '],
['File 280 20       69684558   20       280     19000     '],
['File 280 20       69684558   20       280     -19000    '],
['File 280 20       69694158   20       280     5010      '],
['File 335 59       61664713   59       335     17990     '],
['File 335 59       61664713   59       335     -17990    '],
['File 335 59       61684613   59       335     12990     '],
['File 410 59       68634752   59       410     8990      '],
['File 620 59       60694698   59       620     3990      '],
['File 620 59       60664659   59       620     3990      '],
['File 685 20       62684671   20       685     69990     '],
['File 685 20       62684671   20       685     -69990    '],
['File 878 59       60614487   59       878     5950      ']
])
            click('Close')
        close()

        if frame('Export - DTAR020_tst1.bin:0'):
            select('Only export Nodes with Data', 'false')
            click('save file')
        close()

        if frame('Table:  - DTAR020_tst1.bin.txt:0'):
            assert_content('JTable_22', [ ['File', '', '', '', '', '', '', ''],
['File', '60', '', '', '', '', '', ''],
['File', '60', '166', '', '', '', '', ''],
['File', '60', '166', '', '68654655', '166', '60', '5080'
],
['File', '80', '', '', '', '', '', ''],
['File', '80', '166', '', '', '', '', ''],
['File', '80', '166', '', '69624033', '166', '80', '18190'],
['File', '80', '166', '', '60604100', '166', '80', '13300'],
['File', '170', '', '', '', '', '', ''],
['File', '170', '20', '', '', '', '', ''],
['File', '170', '20', '', '63604808', '20', '170', '4870'],
['File', '170', '166', '', '', '', '', ''],
['File', '170', '166', '', '68674560', '166', '170', '5990'],
['File', '280', '', '', '', '', '', ''],
['File', '280', '20', '', '', '', '', ''],
['File', '280', '20', '', '69684558', '20', '280', '19000'],
['File', '280', '20', '', '69684558', '20', '280', '-19000'],
['File', '280', '20', '', '69694158', '20', '280', '5010'],
['File', '335', '', '', '', '', '', ''],
['File', '335', '59', '', '', '', '', ''],
['File', '335', '59', '', '61664713', '59', '335', '17990'],
['File', '335', '59', '', '61664713', '59', '335', '-17990'],
['File', '335', '59', '', '61684613', '59', '335', '12990'],
['File', '410', '', '', '', '', '', ''],
['File', '410', '59', '', '', '', '', ''],
['File', '410', '59', '', '68634752', '59', '410', '8990'],
['File', '620', '', '', '', '', '', ''],
['File', '620', '59', '', '', '', '', ''],
['File', '620', '59', '', '60694698', '59', '620', '3990'],
['File', '620', '59', '', '60664659', '59', '620', '3990'],
['File', '685', '', '', '', '', '', ''],
['File', '685', '20', '', '', '', '', ''],
['File', '685', '20', '', '62684671', '20', '685', '69990'],
['File', '685', '20', '', '62684671', '20', '685', '-69990'],
['File', '878', '', '', '', '', '', ''],
['File', '878', '59', '', '', '', '', ''],
['File', '878', '59', '', '60614487', '59', '878', '5950']
])
            select('JTable_22', 'rows:[0],columns:[6 - 3|Level_2]')
            select('JTable_22', 'rows:[0],columns:[6 - 3|Level_2]')
            select('Layouts', 'Full Line')
            assert_content('JTable_22', [ ['File                                                    '],
['File 60                                                 '],
['File 60  166                                            '],
['File 60  166      68654655   166      60      5080      '],
['File 80                                                 '],
['File 80  166                                            '],
['File 80  166      69624033   166      80      18190     '],
['File 80  166      60604100   166      80      13300     '],
['File 170                                                '],
['File 170 20                                             '],
['File 170 20       63604808   20       170     4870      '],
['File 170 166                                            '],
['File 170 166      68674560   166      170     5990      '],
['File 280                                                '],
['File 280 20                                             '],
['File 280 20       69684558   20       280     19000     '],
['File 280 20       69684558   20       280     -19000    '],
['File 280 20       69694158   20       280     5010      '],
['File 335                                                '],
['File 335 59                                             '],
['File 335 59       61664713   59       335     17990     '],
['File 335 59       61664713   59       335     -17990    '],
['File 335 59       61684613   59       335     12990     '],
['File 410                                                '],
['File 410 59                                             '],
['File 410 59       68634752   59       410     8990      '],
['File 620                                                '],
['File 620 59                                             '],
['File 620 59       60694698   59       620     3990      '],
['File 620 59       60664659   59       620     3990      '],
['File 685                                                '],
['File 685 20                                             '],
['File 685 20       62684671   20       685     69990     '],
['File 685 20       62684671   20       685     -69990    '],
['File 878                                                '],
['File 878 59                                             '],
['File 878 59       60614487   59       878     5950      ']
])
            click('Close')
        close()

        if frame('Export - DTAR020_tst1.bin:0'):
            select('names on first line', 'true')
            click('save file')
        close()

        if frame('Table:  - DTAR020_tst1.bin.txt:0'):
            assert_content('JTable_22', [ ['Level_1', 'Level_2', 'Level_3', 'Level_4', 'Keycode_no', 'Store_No', 'Dept_No', 'Sale_Price'],
['File', '', '', '', '', '', '', ''],
['File', '60', '', '', '', '', '', ''],
['File', '60', '166', '', '', '', '', ''],
['File', '60', '166', '', '68654655', '166', '60', '5080'
],
['File', '80', '', '', '', '', '', ''],
['File', '80', '166', '', '', '', '', ''],
['File', '80', '166', '', '69624033', '166', '80', '18190'],
['File', '80', '166', '', '60604100', '166', '80', '13300'],
['File', '170', '', '', '', '', '', ''],
['File', '170', '20', '', '', '', '', ''],
['File', '170', '20', '', '63604808', '20', '170', '4870'],
['File', '170', '166', '', '', '', '', ''],
['File', '170', '166', '', '68674560', '166', '170', '5990'],
['File', '280', '', '', '', '', '', ''],
['File', '280', '20', '', '', '', '', ''],
['File', '280', '20', '', '69684558', '20', '280', '19000'],
['File', '280', '20', '', '69684558', '20', '280', '-19000'],
['File', '280', '20', '', '69694158', '20', '280', '5010'],
['File', '335', '', '', '', '', '', ''],
['File', '335', '59', '', '', '', '', ''],
['File', '335', '59', '', '61664713', '59', '335', '17990'],
['File', '335', '59', '', '61664713', '59', '335', '-17990'],
['File', '335', '59', '', '61684613', '59', '335', '12990'],
['File', '410', '', '', '', '', '', ''],
['File', '410', '59', '', '', '', '', ''],
['File', '410', '59', '', '68634752', '59', '410', '8990'],
['File', '620', '', '', '', '', '', ''],
['File', '620', '59', '', '', '', '', ''],
['File', '620', '59', '', '60694698', '59', '620', '3990'],
['File', '620', '59', '', '60664659', '59', '620', '3990'],
['File', '685', '', '', '', '', '', ''],
['File', '685', '20', '', '', '', '', ''],
['File', '685', '20', '', '62684671', '20', '685', '69990'],
['File', '685', '20', '', '62684671', '20', '685', '-69990'],
['File', '878', '', '', '', '', '', ''],
['File', '878', '59', '', '', '', '', ''],
['File', '878', '59', '', '60614487', '59', '878', '5950']
])
            select('JTable_22', 'rows:[0],columns:[9 - 7|Level_2]')
            select('JTable_22', 'rows:[0],columns:[9 - 7|Level_2]')
            select('Layouts', 'Full Line')
            assert_content('JTable_22', [ ['Level_1 Level_2 Level_3 Level_4 Keycode_no Store_No Dept_No Sale_Price'],
['File                                                                  '],
['File    60                                                            '],
['File    60      166                                                   '],
['File    60      166             68654655   166      60      5080      '],
['File    80                                                            '],
['File    80      166                                                   '],
['File    80      166             69624033   166      80      18190     '],
['File    80      166             60604100   166      80      13300     '],
['File    170                                                           '],
['File    170     20                                                    '],
['File    170     20              63604808   20       170     4870      '],
['File    170     166                                                   '],
['File    170     166             68674560   166      170     5990      '],
['File    280                                                           '],
['File    280     20                                                    '],
['File    280     20              69684558   20       280     19000     '],
['File    280     20              69684558   20       280     -19000    '],
['File    280     20              69694158   20       280     5010      '],
['File    335                                                           '],
['File    335     59                                                    '],
['File    335     59              61664713   59       335     17990     '],
['File    335     59              61664713   59       335     -17990    '],
['File    335     59              61684613   59       335     12990     '],
['File    410                                                           '],
['File    410     59                                                    '],
['File    410     59              68634752   59       410     8990      '],
['File    620                                                           '],
['File    620     59                                                    '],
['File    620     59              60694698   59       620     3990      '],
['File    620     59              60664659   59       620     3990      '],
['File    685                                                           '],
['File    685     20                                                    '],
['File    685     20              62684671   20       685     69990     '],
['File    685     20              62684671   20       685     -69990    '],
['File    878                                                           '],
['File    878     59                                                    '],
['File    878     59              60614487   59       878     5950      ']
])
            click('Close')
        close()

##        window_closed('Record Editor')
    close()

    pass
