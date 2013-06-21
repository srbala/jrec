useFixture(reCsvEditor)

def test():
	from Modules import commonBits
	java_recorded_version = '1.6.0_22'

	if window('reCsv Editor'):
		select('FilePane$3', 'DTAR020.csv')
		doubleclick('FilePane$3', '3')
		click(commonBits.fl('Edit') + '1')
		select('LineList.FileDisplay_JTbl', 'rows:[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18],columns:[1|keycode-no,2|Store-No]')
		select_menu(commonBits.fl('View') + '>>' + commonBits.fl('Table View #{Selected Records#}'))
##		select('TabbedPane', 'Table:')
		select('LineList.FileDisplay_JTbl1', 'cell:3|Date,10(40118)')
		assert_p('LineList.FileDisplay_JTbl1', 'Content', '[[69694158, 20, 40118, 280, 1, 19.00], [69694158, 20, 40118, 280, -1, -19.00], [69694158, 20, 40118, 280, 1, 5.01], [63604808, 20, 40118, 170, 1, 4.87], [62684671, 20, 40118, 685, 1, 69.99], [62684671, 20, 40118, 685, -1, -69.99], [64634429, 20, 40118, 957, 1, 3.99], [66624458, 20, 40118, 957, 1, 0.89], [63674861, 20, 40118, 957, 10, 2.70], [65674532, 20, 40118, 929, 1, 3.59], [64614401, 59, 40118, 957, 1, 1.99], [64614401, 59, 40118, 957, 1, 1.99], [61664713, 59, 40118, 335, 1, 17.99], [61664713, 59, 40118, 335, -1, -17.99], [68634752, 59, 40118, 410, 1, 8.99], [60614487, 59, 40118, 878, 1, 5.95]]')
		select('LineList.FileDisplay_JTbl1', 'cell:3|Date,10(40118)')
		select_menu(commonBits.fl('Edit') + '>>' + commonBits.fl('Update Csv Columns'))
		select('LineList.FileDisplay_JTbl1', 'cell:3|Date,10(40118)')
		select('FieldChange_JTbl', commonBits.fl('Number'), commonBits.fl('Type') + ',4')
		select('FieldChange_JTbl', commonBits.fl('Number (Fixed Decimal)'), commonBits.fl('Type') + ',5')
		select('FieldChange_JTbl', 'cell:' + commonBits.fl('Decimal Places') + ',4(null)')
		assert_p('FieldChange_JTbl', 'Content', '[[keycode-no, true, ' + commonBits.fl('Text') + ', , , ], [Store-No, true, ' + commonBits.fl('Text') + ', , , ], [Date, true, ' + commonBits.fl('Text') + ', , , ], [Dept-No, true, ' + commonBits.fl('Text') + ', , , ], [Qty-Sold, true, ' + commonBits.fl('Number') + ', , , ], [Sale-Price, true, ' + commonBits.fl('Number (Fixed Decimal)') + ', 0, , ]]')
		select('FieldChange_JTbl', '3', commonBits.fl('Decimal Places') + ',5')
		select('FieldChange_JTbl', 'cell:' + commonBits.fl('Decimal Places') + ',4(null)')
		assert_p('FieldChange_JTbl', 'Content', '[[keycode-no, true, ' + commonBits.fl('Text') + ', , , ], [Store-No, true, ' + commonBits.fl('Text') + ', , , ], [Date, true, ' + commonBits.fl('Text') + ', , , ], [Dept-No, true, ' + commonBits.fl('Text') + ', , , ], [Qty-Sold, true, ' + commonBits.fl('Number') + ', , , ], [Sale-Price, true, ' + commonBits.fl('Number (Fixed Decimal)') + ', 3, , ]]')
		select('FieldChange_JTbl', 'cell:' + commonBits.fl('Decimal Places') + ',4(null)')
		click(commonBits.fl('Apply'))
		select_menu(commonBits.fl('Edit') + '>>' + commonBits.fl('Save File Description as Xml'))
		select('File Name', 'DTAR020xyy.Xml')
		click(commonBits.fl('Save'))
		select_menu(commonBits.fl('Window') + '>>DTAR020.csv>>' + commonBits.fl('Table:'))
		click('BasicInternalFrameTitlePane$NoFocusButton2')

		if window(commonBits.fl('Save Changes to file: ' + commonBits.reCsvEditParamDir() + 'DTAR020.csv')):
			click('No')
		close()

		click(commonBits.fl('Edit') + '1')
		select('LineList.FileDisplay_JTbl', 'rows:[4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],columns:[1|keycode-no]')
		select_menu(commonBits.fl('View') + '>>' + commonBits.fl('Table View #{Selected Records#}'))
##		select('TabbedPane', 'Table:')
		select('LineList.FileDisplay_JTbl1', 'cell:1|keycode-no,5(64634429)')
		assert_p('LineList.FileDisplay_JTbl1', 'Content', '[[69694158, 20, 40118, 280, -1, -19.00], [69694158, 20, 40118, 280, 1, 5.01], [63604808, 20, 40118, 170, 1, 4.87], [62684671, 20, 40118, 685, 1, 69.99], [62684671, 20, 40118, 685, -1, -69.99], [64634429, 20, 40118, 957, 1, 3.99], [66624458, 20, 40118, 957, 1, 0.89], [63674861, 20, 40118, 957, 10, 2.70], [65674532, 20, 40118, 929, 1, 3.59], [64614401, 59, 40118, 957, 1, 1.99], [64614401, 59, 40118, 957, 1, 1.99], [61664713, 59, 40118, 335, 1, 17.99], [61664713, 59, 40118, 335, -1, -17.99], [68634752, 59, 40118, 410, 1, 8.99], [60614487, 59, 40118, 878, 1, 5.95], [63644339, 59, 40118, 878, 1, 12.65], [60694698, 59, 40118, 620, 1, 3.99]]')
		select('LineList.FileDisplay_JTbl1', 'cell:1|keycode-no,5(64634429)')
		select_menu(commonBits.fl('Edit') + '>>' + commonBits.fl('Load File Description from Xml'))
		select('LineList.FileDisplay_JTbl1', 'cell:1|keycode-no,5(64634429)')
		select('File Name', 'DTAR020xyy.Xml')
		click(commonBits.fl('Load'))
		select('LineList.FileDisplay_JTbl1', 'cell:4|Dept-No,9(957)')
		select_menu(commonBits.fl('Window') + '>>DTAR020.csv>>' + commonBits.fl('Table:'))
		select('LineList.FileDisplay_JTbl1', 'cell:3|Date,6(40118)')
		assert_p('LineList.FileDisplay_JTbl1', 'Content', '[[69694158, 20, 40118, 280, -1, -19.00], [69694158, 20, 40118, 280, 1, 5.01], [63604808, 20, 40118, 170, 1, 4.87], [62684671, 20, 40118, 685, 1, 69.99], [62684671, 20, 40118, 685, -1, -69.99], [64634429, 20, 40118, 957, 1, 3.99], [66624458, 20, 40118, 957, 1, 0.89], [63674861, 20, 40118, 957, 10, 2.70], [65674532, 20, 40118, 929, 1, 3.59], [64614401, 59, 40118, 957, 1, 1.99], [64614401, 59, 40118, 957, 1, 1.99], [61664713, 59, 40118, 335, 1, 17.99], [61664713, 59, 40118, 335, -1, -17.99], [68634752, 59, 40118, 410, 1, 8.99], [60614487, 59, 40118, 878, 1, 5.95], [63644339, 59, 40118, 878, 1, 12.65], [60694698, 59, 40118, 620, 1, 3.99]]')
		select('LineList.FileDisplay_JTbl1', 'cell:3|Date,6(40118)')
		select_menu(commonBits.fl('Edit') + '>>' + commonBits.fl('Update Csv Columns'))
		select('LineList.FileDisplay_JTbl1', 'cell:3|Date,6(40118)')
		assert_p('FieldChange_JTbl', 'Content', '[[keycode-no, true, ' + commonBits.fl('Text') + ', , , ], [Store-No, true, ' + commonBits.fl('Text') + ', , , ], [Date, true, ' + commonBits.fl('Text') + ', , , ], [Dept-No, true, ' + commonBits.fl('Text') + ', , , ], [Qty-Sold, true, ' + commonBits.fl('Number') + ', , , ], [Sale-Price, true, ' + commonBits.fl('Number (Fixed Decimal)') + ', 3, , ]]')
		select_menu(commonBits.fl('Window') + '>>DTAR020.csv>>' + commonBits.fl('Update Screen Columns'))
		click('BasicInternalFrameTitlePane$NoFocusButton2')
		click(commonBits.fl('Table:') + '1')
		select('LineList.FileDisplay_JTbl1', 'cell:3|Date,6(40118)')
		select('LineList.FileDisplay_JTbl1', '2.710', '6|Sale-Price,7')
		select('LineList.FileDisplay_JTbl1', 'cell:1|keycode-no,8(65674532)')
		assert_p('LineList.FileDisplay_JTbl1', 'Content', '[[69694158, 20, 40118, 280, -1, -19.00], [69694158, 20, 40118, 280, 1, 5.01], [63604808, 20, 40118, 170, 1, 4.87], [62684671, 20, 40118, 685, 1, 69.99], [62684671, 20, 40118, 685, -1, -69.99], [64634429, 20, 40118, 957, 1, 3.99], [66624458, 20, 40118, 957, 1, 0.89], [63674861, 20, 40118, 957, 10, 2.710], [65674532, 20, 40118, 929, 1, 3.59], [64614401, 59, 40118, 957, 1, 1.99], [64614401, 59, 40118, 957, 1, 1.99], [61664713, 59, 40118, 335, 1, 17.99], [61664713, 59, 40118, 335, -1, -17.99], [68634752, 59, 40118, 410, 1, 8.99], [60614487, 59, 40118, 878, 1, 5.95], [63644339, 59, 40118, 878, 1, 12.65], [60694698, 59, 40118, 620, 1, 3.99]]')
		select('LineList.FileDisplay_JTbl1', 'cell:1|keycode-no,8(65674532)')
		click('Sort')
		select('fields_JTbl', 'Sale-Price', commonBits.fl('Field') + ',0')
		select('fields_JTbl', 'cell:' + commonBits.fl('Field') + ',0(Sale-Price)')
		click(commonBits.fl('Sort'))
		assert_p('LineList.FileDisplay_JTbl1', 'Content', '[[62684671, 20, 40118, 685, -1, -69.99], [69694158, 20, 40118, 280, -1, -19.00], [61664713, 59, 40118, 335, -1, -17.99], [66624458, 20, 40118, 957, 1, 0.89], [64614401, 59, 40118, 957, 1, 1.99], [64614401, 59, 40118, 957, 1, 1.99], [63674861, 20, 40118, 957, 10, 2.710], [65674532, 20, 40118, 929, 1, 3.59], [64634429, 20, 40118, 957, 1, 3.99], [60694698, 59, 40118, 620, 1, 3.99], [63604808, 20, 40118, 170, 1, 4.87], [69694158, 20, 40118, 280, 1, 5.01], [60614487, 59, 40118, 878, 1, 5.95], [68634752, 59, 40118, 410, 1, 8.99], [63644339, 59, 40118, 878, 1, 12.65], [61664713, 59, 40118, 335, 1, 17.99], [62684671, 20, 40118, 685, 1, 69.99]]')

##		if window(rcommonBits.fl('Save Changes to file: C:\Users\BruceTst2\.RecordEditor\reCsvEd\SampleFiles\DTAR020.csv')):
##			click('No')
##		close()
	close()
