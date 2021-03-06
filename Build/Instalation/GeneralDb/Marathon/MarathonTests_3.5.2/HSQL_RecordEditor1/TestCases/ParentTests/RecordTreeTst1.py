#{{{ Marathon
from default import *
#}}} Marathon

from Modules import commonBits

def test():

    set_java_recorded_version("1.6.0_22")
    if frame(' - Open File:0'):
        select('File', commonBits.sampleDir() + 'Ams_PODownload_20041231_Compare1.txt')
        click('Edit')
    close()

    if frame('Table:  - Ams_PODownload_20041231_Compare1.txt:0'):
        select('JTable_22', 'rows:[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32],columns:[7 - 8|Pack Quantity 1]')
    close()

    if window('Record Editor'):
        select_menu('View>>Record Layout Tree (Selected Records)')

#        if frame('Table:  - Ams_PODownload_20041231_Compare1.txt:1'):
#            select('JTable_22', 'rows:[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32],columns:[7 - 8|Pack Quantity 1]')
#        close()

        if frame('Tree View - Ams_PODownload_20041231_Compare1.txt:0'):
            assert_content('net.sf.RecordEditor.utils.swing.treeTable.JTreeTable_10', [ ['', '', 'H1', '4534', '90000006', '602', '86225', '', '200', '50', '10205010', '7596', '5', 'LAD', 'IES KNIC', 'FT', '', '', '', '', ''],
['', '', 'D1', '1', '70000000', '0', '10222', '4331', '45310000', '5', '45400000', '7', '207', '5359', '', '4561', '4531', 'D', 'ONKEY 24', '-6', '607 SHWL'],
['', '', 'S1', '5043', '10', '9045', '2', '5076', '1', '5079', '1', '5151', '1', '5072', '1', '', '0', '', '0', '', '0'],
['', '', 'D1', '1', '40000000', '1', '48320000', '0561', '49440000', '5', '45400000', '4', '207', '5360', '', '5614', '944', 'M', 'ILK 24-0', '660', '7 SHWL W'],
['', '', 'S1', '5045', '11', '5076', '1', '3331', '49440001', '', '0', '', '0', '', '0', '', '0', '', '0', '', '0'],
['', '', 'D1', '0', '80000000', '0', '48320000', '5561', '50710000', '5', '45400000', '48', '207', '5361', '', '5561', '5071', 'M', '.ROSE 24', '-6', '607 SHWL'],
['', '', 'S1', '5036', '6', '5043', '51', '3331', '50710003', '5065', '4', '5069', '4', '5076', '4', '5079', '2', '5094', '4', '5128', '3'],
['', '', 'S1', '5151', '4', '5180', '3', '5173', '2', '', '0', '', '0', '', '0', '', '0', '', '0', '', '0'],
['', '', 'D1', '0', '40000000', '1', '48320000', '5561', '51560000', '5', '45400000', '4', '207', '5362', '', '5561', '5156', 'A', 'QUA 24-0', '660', '7 SHWL W'],
['', '', 'S1', '5043', '1', '5045', '1', '3331', '51560001', '', '0', '', '0', '', '0', '', '0', '', '0', '', '0'],
['', '', 'H1', '4535', '6', '2280', '222', '', '200', '50', '10205010', '7596', '6', 'LAD', 'IES KNIC', 'FT', '', '', '', '', ''],
['', '', 'D1', '1', '60000006', '2281', '48320000', '0222', '45310000', '5', '45400000', '16', '207', '5348', '', '5614', '531', 'D', 'ONKEY 24', '-6', '607 SHWL'],
['', '', 'S1', '5019', '1', '5037', '1', '5078', '1', '5085', '1', '5091', '1', '5093', '1', '5095', '1', '51 D', 'ONKEY 24', '-6', '607 SHWL'],
['', '', 'S1', '5171', '1', '5177', '1', '5136', '1', '5145', '1', '5096', '1', '', '0', '', '0', '', '0', '', '0'],
['', '', 'D1', '0', '80000000', '1', '48320000', '6222', '49440000', '5', '45400000', '8', '207', '5349', '', '6561', '4944', 'M', 'ILK 24-0', '660', '7 SHWL W'],
['', '', 'S1', '5019', '1', '5037', '1', '5091', '1', '5093', '1', '5129', '1', '5177', '1', '5145', '1', '', '0', '', '0'],
['', '', 'D1', '10', '80000000', '1', '48320000', '6222', '50710000', '5', '45400001', '8', '207', '5350', '', '6561', '5071', 'M', '.ROSE 24', '-6', '607 SHWL'],
['', '', 'S1', '5015', '2', '5019', '5', '5035', '2', '5037', '4', '5052', '2', '5055', '2', '5060', '2', '5070', '2', '5074', '4'],
['', '', 'S1', '5078', '5', '5081', '2', '5090', '2', '5091', '4', '5093', '4', '5095', '4', '5129', '4', '5144', '4', '5165', '2'],
['', '', 'S1', '5303', '2', '5169', '2', '5171', '3', '5177', '4', '5016', '2', '5089', '4', '5136', '3', '5011', '2', '5046', '2'],
['', '', 'S1', '5145', '4', '5096', '3', '5162', '2', '5163', '2', '5164', '2', '5192', '2', '5150', '2', '5175', '2', '', '0'],
['', '', 'D1', '0', '80000000', '1', '48320000', '5222', '51560000', '5', '45400000', '8', '207', '5351', '', '5561', '5156', 'M', '.ROSE 24', '-6', '607 SHWL'],
['', '', 'S1', '5019', '1', '5037', '1', '5091', '1', '5093', '1', '5129', '1', '5177', '1', '5145', '1', '', '0', '', '0'],
['', '', 'H1', '4535', '10000006', '2280', '222', '', '200', '50', '10205010', '7596', '8', 'LAD', 'IES KNIC', 'FT', '', '', '', '', ''],
['', '', 'D1', '0', '60000000', '1', '48320000', '4561', '45310000', '5', '45400000', '6', '207', '5352', '', '4561', '4531', 'D', 'ONKEY 24', '-6', '607 SHWL'],
['', '', 'S1', '5009', '1', '5021', '1', '5025', '1', '5026', '1', '5127', '1', '', '0', '', '0', '', '0', '', '0'],
['', '', 'D1', '0', '30000000', '1', '48320000', '4561', '49440000', '5', '45400000', '3', '207', '5353', '', '4561', '4944', 'M', 'ILK 24-0', '660', '7 SHWL W'],
['', '', 'S1', '5009', '1', '5021', '1', '', '0', '', '0', '', '0', '', '0', '', '0', '', '0', '', '0'],
['', '', 'D1', '4', '40000000', '1', '48320000', '4561', '50710000', '5', '45400000', '44', '207', '5354', '', '4561', '5071', 'M', '.ROSE 24', '-6', '607 SHWL'],
['', '', 'S1', '5009', '5', '5021', '5', '5025', '4', '5026', '4', '5047', '3', '5077', '2', '5127', '5', '5134', '4', '5142', '2'],
['', '', 'S1', '5044', '2', '5071', '2', '', '0', '', '0', '', '0', '', '0', '', '0', '', '0', '', '0'],
['', '', 'D1', '0', '30000000', '1', '48320000', '4561', '51560000', '5', '45400000', '3', '207', '5355', '', '3561', '5156', 'A', 'QUA 24-0', '660', '7 SHWL W'],
['', '', 'S1', '5009', '1', '5021', '1', '', '0', '', '0', '', '0', '', '0', '', '0', '', '0', '', '0']
])
            click('Close')
        close()
    close()

    pass
