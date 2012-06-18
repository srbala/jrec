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


        select_menu('File>>Export as CSV file')

        if frame('Export - DTAR020_tst1.bin:0'):
            select('Only export Nodes with Data', 'false')
            select('Edit Output File', 'true')
            select('Keep screen open', 'true')
            select('names on first line', 'true')
            select('Delimiter', ';')
            click('save file')
        close()

        if frame('Table:  - DTAR020_tst1.bin.csv:0'):
            assert_content('JTable_22', [ ['File', '', '', '', '', '', '', '', '', ''],
['File', '60', '', '', '', '', '', '', '', ''],
['File', '60', '166', '', '', '', '', '', '', ''],
['File', '60', '166', '', '68654655', '166', '40118', '60', '1', '5080'
],
['File', '80', '', '', '', '', '', '', '', ''],
['File', '80', '166', '', '', '', '', '', '', ''],
['File', '80', '166', '', '69624033', '166', '40118', '80', '1', '18190'],
['File', '80', '166', '', '60604100', '166', '40118', '80', '1', '13300'],
['File', '170', '', '', '', '', '', '', '', ''],
['File', '170', '20', '', '', '', '', '', '', ''],
['File', '170', '20', '', '63604808', '20', '40118', '170', '1', '4870'],
['File', '170', '166', '', '', '', '', '', '', ''],
['File', '170', '166', '', '68674560', '166', '40118', '170', '1', '5990'],
['File', '280', '', '', '', '', '', '', '', ''],
['File', '280', '20', '', '', '', '', '', '', ''],
['File', '280', '20', '', '69684558', '20', '40118', '280', '1', '19000'],
['File', '280', '20', '', '69684558', '20', '40118', '280', '-1', '-19000'],
['File', '280', '20', '', '69694158', '20', '40118', '280', '1', '5010'],
['File', '335', '', '', '', '', '', '', '', ''],
['File', '335', '59', '', '', '', '', '', '', ''],
['File', '335', '59', '', '61664713', '59', '40118', '335', '1', '17990'],
['File', '335', '59', '', '61664713', '59', '40118', '335', '-1', '-17990'],
['File', '335', '59', '', '61684613', '59', '40118', '335', '1', '12990'],
['File', '410', '', '', '', '', '', '', '', ''],
['File', '410', '59', '', '', '', '', '', '', ''],
['File', '410', '59', '', '68634752', '59', '40118', '410', '1', '8990'],
['File', '620', '', '', '', '', '', '', '', ''],
['File', '620', '59', '', '', '', '', '', '', ''],
['File', '620', '59', '', '60694698', '59', '40118', '620', '1', '3990'],
['File', '620', '59', '', '60664659', '59', '40118', '620', '1', '3990'],
['File', '685', '', '', '', '', '', '', '', ''],
['File', '685', '20', '', '', '', '', '', '', ''],
['File', '685', '20', '', '62684671', '20', '40118', '685', '1', '69990'],
['File', '685', '20', '', '62684671', '20', '40118', '685', '-1', '-69990'],
['File', '878', '', '', '', '', '', '', '', ''],
['File', '878', '59', '', '', '', '', '', '', ''],
['File', '878', '59', '', '60614487', '59', '40118', '878', '1', '5950']
])
            select('JTable_22', 'rows:[0],columns:[2|Level_2]')
            assert_p('net.sf.RecordEditor.edit.display.BaseDisplay$HeaderToolTips_27', 'Text', '10|Sale_Price', '10|Sale_Price')
            assert_p('net.sf.RecordEditor.edit.display.BaseDisplay$HeaderToolTips_27', 'Text', '8|Dept_No', '8|Dept_No')
            assert_p('net.sf.RecordEditor.edit.display.BaseDisplay$HeaderToolTips_27', 'Text', '5|Keycode_no', '5|Keycode_no')
            assert_p('net.sf.RecordEditor.edit.display.BaseDisplay$HeaderToolTips_27', 'Text', '3|Level_3', '3|Level_3')
            select('Layouts', 'Full Line')
            assert_content('JTable_22', [ ['File;;;;;;;;;'],
['File;60;;;;;;;;'],
['File;60;166;;;;;;;'],
['File;60;166;;68654655;166;40118;60;1;5080'
],
['File;80;;;;;;;;'],
['File;80;166;;;;;;;'],
['File;80;166;;69624033;166;40118;80;1;18190'],
['File;80;166;;60604100;166;40118;80;1;13300'],
['File;170;;;;;;;;'],
['File;170;20;;;;;;;'],
['File;170;20;;63604808;20;40118;170;1;4870'],
['File;170;166;;;;;;;'],
['File;170;166;;68674560;166;40118;170;1;5990'],
['File;280;;;;;;;;'],
['File;280;20;;;;;;;'],
['File;280;20;;69684558;20;40118;280;1;19000'],
['File;280;20;;69684558;20;40118;280;-1;-19000'],
['File;280;20;;69694158;20;40118;280;1;5010'],
['File;335;;;;;;;;'],
['File;335;59;;;;;;;'],
['File;335;59;;61664713;59;40118;335;1;17990'],
['File;335;59;;61664713;59;40118;335;-1;-17990'],
['File;335;59;;61684613;59;40118;335;1;12990'],
['File;410;;;;;;;;'],
['File;410;59;;;;;;;'],
['File;410;59;;68634752;59;40118;410;1;8990'],
['File;620;;;;;;;;'],
['File;620;59;;;;;;;'],
['File;620;59;;60694698;59;40118;620;1;3990'],
['File;620;59;;60664659;59;40118;620;1;3990'],
['File;685;;;;;;;;'],
['File;685;20;;;;;;;'],
['File;685;20;;62684671;20;40118;685;1;69990'],
['File;685;20;;62684671;20;40118;685;-1;-69990'],
['File;878;;;;;;;;'],
['File;878;59;;;;;;;'],
['File;878;59;;60614487;59;40118;878;1;5950']
])
            click('Close')
        close()

        if frame('Export - DTAR020_tst1.bin:0'):
#            select('JTable_37', 'rows:[4],columns:[Include]')
#            select('JTable_37', 'false', '{2, Include}')
#            select('JTable_37', 'rows:[2],columns:[Include]')
#            select('JTable_37', 'false', '{4, Include}')
            select('JTable_34', 'rows:[4],columns:[Include]')
            select('JTable_34', 'false', '{2, Include}')
            select('JTable_34', 'rows:[2],columns:[Include]')
            select('JTable_34', 'false', '{4, Include}')
            click('save file')
        close()

        if frame('Table:  - DTAR020_tst1.bin.csv:0'):
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
            select('JTable_22', 'rows:[0],columns:[2|Level_2]')
            assert_p('net.sf.RecordEditor.edit.display.BaseDisplay$HeaderToolTips_27', 'Text', '7|Dept_No', '7|Dept_No')
            assert_p('net.sf.RecordEditor.edit.display.BaseDisplay$HeaderToolTips_27', 'Text', '6|Store_No', '6|Store_No')
            assert_p('net.sf.RecordEditor.edit.display.BaseDisplay$HeaderToolTips_27', 'Text', '5|Keycode_no', '5|Keycode_no')
            assert_p('net.sf.RecordEditor.edit.display.BaseDisplay$HeaderToolTips_27', 'Text', '3|Level_3', '3|Level_3')
            select('Layouts', 'Full Line')
            assert_content('JTable_22', [ ['File;;;;;;;'],
['File;60;;;;;;'],
['File;60;166;;;;;'],
['File;60;166;;68654655;166;60;5080'
],
['File;80;;;;;;'],
['File;80;166;;;;;'],
['File;80;166;;69624033;166;80;18190'],
['File;80;166;;60604100;166;80;13300'],
['File;170;;;;;;'],
['File;170;20;;;;;'],
['File;170;20;;63604808;20;170;4870'],
['File;170;166;;;;;'],
['File;170;166;;68674560;166;170;5990'],
['File;280;;;;;;'],
['File;280;20;;;;;'],
['File;280;20;;69684558;20;280;19000'],
['File;280;20;;69684558;20;280;-19000'],
['File;280;20;;69694158;20;280;5010'],
['File;335;;;;;;'],
['File;335;59;;;;;'],
['File;335;59;;61664713;59;335;17990'],
['File;335;59;;61664713;59;335;-17990'],
['File;335;59;;61684613;59;335;12990'],
['File;410;;;;;;'],
['File;410;59;;;;;'],
['File;410;59;;68634752;59;410;8990'],
['File;620;;;;;;'],
['File;620;59;;;;;'],
['File;620;59;;60694698;59;620;3990'],
['File;620;59;;60664659;59;620;3990'],
['File;685;;;;;;'],
['File;685;20;;;;;'],
['File;685;20;;62684671;20;685;69990'],
['File;685;20;;62684671;20;685;-69990'],
['File;878;;;;;;'],
['File;878;59;;;;;'],
['File;878;59;;60614487;59;878;5950']
])
            click('Close')
        close()

        if frame('Export - DTAR020_tst1.bin:0'):
            select('Delimiter', ',')
            click('save file')
        close()

        if frame('Table:  - DTAR020_tst1.bin.csv:0'):
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
            select('JTable_22', 'rows:[0],columns:[2|Level_2]')
            assert_p('net.sf.RecordEditor.edit.display.BaseDisplay$HeaderToolTips_27', 'Text', '8|Sale_Price', '8|Sale_Price')
            assert_p('net.sf.RecordEditor.edit.display.BaseDisplay$HeaderToolTips_27', 'Text', '8|Sale_Price', '8|Sale_Price')
            assert_p('net.sf.RecordEditor.edit.display.BaseDisplay$HeaderToolTips_27', 'Text', '7|Dept_No', '7|Dept_No')
            assert_p('net.sf.RecordEditor.edit.display.BaseDisplay$HeaderToolTips_27', 'Text', '6|Store_No', '6|Store_No')
            assert_p('net.sf.RecordEditor.edit.display.BaseDisplay$HeaderToolTips_27', 'Text', '5|Keycode_no', '5|Keycode_no')
            assert_p('net.sf.RecordEditor.edit.display.BaseDisplay$HeaderToolTips_27', 'Text', '2|Level_2', '2|Level_2')
            select('Layouts', 'Full Line')
            assert_p('JTable_22', 'Text', 'File,170,20,,,,,', '{9, Full Line}')
            assert_content('JTable_22', [ ['File,,,,,,,'],
['File,60,,,,,,'],
['File,60,166,,,,,'],
['File,60,166,,68654655,166,60,5080'
],
['File,80,,,,,,'],
['File,80,166,,,,,'],
['File,80,166,,69624033,166,80,18190'],
['File,80,166,,60604100,166,80,13300'],
['File,170,,,,,,'],
['File,170,20,,,,,'],
['File,170,20,,63604808,20,170,4870'],
['File,170,166,,,,,'],
['File,170,166,,68674560,166,170,5990'],
['File,280,,,,,,'],
['File,280,20,,,,,'],
['File,280,20,,69684558,20,280,19000'],
['File,280,20,,69684558,20,280,-19000'],
['File,280,20,,69694158,20,280,5010'],
['File,335,,,,,,'],
['File,335,59,,,,,'],
['File,335,59,,61664713,59,335,17990'],
['File,335,59,,61664713,59,335,-17990'],
['File,335,59,,61684613,59,335,12990'],
['File,410,,,,,,'],
['File,410,59,,,,,'],
['File,410,59,,68634752,59,410,8990'],
['File,620,,,,,,'],
['File,620,59,,,,,'],
['File,620,59,,60694698,59,620,3990'],
['File,620,59,,60664659,59,620,3990'],
['File,685,,,,,,'],
['File,685,20,,,,,'],
['File,685,20,,62684671,20,685,69990'],
['File,685,20,,62684671,20,685,-69990'],
['File,878,,,,,,'],
['File,878,59,,,,,'],
['File,878,59,,60614487,59,878,5950']
])
            click('Close')
        close()

        if frame('Export - DTAR020_tst1.bin:0'):
            select('JTable_34', 'rows:[4],columns:[Include]')
            select('JTable_34', 'rows:[2],columns:[Include]')
            select('JTable_34', 'true', '{2, Include}')
            select('JTable_34', 'true', '{4, Include}')

            click('save file')
        close()

        if frame('Table:  - DTAR020_tst1.bin.csv:0'):
            assert_p('JTable_22', 'Text', '69684558', '{16, 5|Keycode_no}')
            select('JTable_22', 'rows:[0],columns:[2|Level_2]')
            assert_p('net.sf.RecordEditor.edit.display.BaseDisplay$HeaderToolTips_27', 'Text', '10|Sale_Price', '10|Sale_Price')
            assert_p('net.sf.RecordEditor.edit.display.BaseDisplay$HeaderToolTips_27', 'Text', '8|Dept_No', '8|Dept_No')
            assert_p('net.sf.RecordEditor.edit.display.BaseDisplay$HeaderToolTips_27', 'Text', '7|DATE', '7|DATE')
            assert_p('net.sf.RecordEditor.edit.display.BaseDisplay$HeaderToolTips_27', 'Text', '5|Keycode_no', '5|Keycode_no')
            assert_p('net.sf.RecordEditor.edit.display.BaseDisplay$HeaderToolTips_27', 'Text', '3|Level_3', '3|Level_3')
            select('Layouts', 'Full Line')
            assert_content('JTable_22', [ ['File,,,,,,,,,'],
['File,60,,,,,,,,'],
['File,60,166,,,,,,,'],
['File,60,166,,68654655,166,40118,60,1,5080'
],
['File,80,,,,,,,,'],
['File,80,166,,,,,,,'],
['File,80,166,,69624033,166,40118,80,1,18190'],
['File,80,166,,60604100,166,40118,80,1,13300'],
['File,170,,,,,,,,'],
['File,170,20,,,,,,,'],
['File,170,20,,63604808,20,40118,170,1,4870'],
['File,170,166,,,,,,,'],
['File,170,166,,68674560,166,40118,170,1,5990'],
['File,280,,,,,,,,'],
['File,280,20,,,,,,,'],
['File,280,20,,69684558,20,40118,280,1,19000'],
['File,280,20,,69684558,20,40118,280,-1,-19000'],
['File,280,20,,69694158,20,40118,280,1,5010'],
['File,335,,,,,,,,'],
['File,335,59,,,,,,,'],
['File,335,59,,61664713,59,40118,335,1,17990'],
['File,335,59,,61664713,59,40118,335,-1,-17990'],
['File,335,59,,61684613,59,40118,335,1,12990'],
['File,410,,,,,,,,'],
['File,410,59,,,,,,,'],
['File,410,59,,68634752,59,40118,410,1,8990'],
['File,620,,,,,,,,'],
['File,620,59,,,,,,,'],
['File,620,59,,60694698,59,40118,620,1,3990'],
['File,620,59,,60664659,59,40118,620,1,3990'],
['File,685,,,,,,,,'],
['File,685,20,,,,,,,'],
['File,685,20,,62684671,20,40118,685,1,69990'],
['File,685,20,,62684671,20,40118,685,-1,-69990'],
['File,878,,,,,,,,'],
['File,878,59,,,,,,,'],
['File,878,59,,60614487,59,40118,878,1,5950']
])
            click('Close')
        close()

##        window_closed('Record Editor')
    close()

    pass
