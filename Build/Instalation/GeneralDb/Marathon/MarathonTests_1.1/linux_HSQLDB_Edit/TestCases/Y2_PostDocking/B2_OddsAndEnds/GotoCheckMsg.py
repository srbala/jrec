useFixture(default)

def test():
	from Modules import commonBits
	java_recorded_version = '1.6.0_22'

	if window('Record Editor'):
		select('File_Txt', commonBits.sampleDir() + 'DTAR020_tst1.bin')
		click('Edit1')
		select('LineList.FileDisplay_JTbl', 'cell:9 - 2|STORE-NO,0(20)')
		rightclick('LineList.FileDisplay_JTbl', '9 - 2|STORE-NO,4')
##		select('LineList.FileDisplay_JTbl', 'cell:9 - 2|STORE-NO,0(20)')
		select_menu('Goto Line')
		select('LineList.FileDisplay_JTbl', 'cell:9 - 2|STORE-NO,0(20)')

		click('Goto')
		assert_p('TextField', 'Text', 'You must enter a line number')
		select('Line Number_Txt', '-1')
		click('Goto')
		assert_p('TextField', 'Text', 'line number must be > 0')
		select('Line Number_Txt', '')
		click('Goto')
		assert_p('TextField', 'Text', 'You must enter a line number')


##		select('Line Number_Txt', '-1')
##		click('Goto')
##		assert_p('TextField', 'Text', 'line number must be > 0')
		select('Line Number_Txt', 'aa')
		click('Goto')
		assert_p('TextField', 'Text', 'Invalid line number')
		select('Line Number_Txt', '111')
		click('Goto')
		assert_p('TextField', 'Text', 'line number must be < 17')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
		select('LineList.FileDisplay_JTbl', 'cell:9 - 2|STORE-NO,0(20)')
		select('LineList.FileDisplay_JTbl', 'cell:9 - 2|STORE-NO,0(20)')
		rightclick('LineList.FileDisplay_JTbl', '1 - 8|KEYCODE-NO,1')
		select_menu('Edit Record')
		select('TabbedPane', 'Record:')
##		select('LineFrame.FileDisplay_JTbl', '')
		rightclick('LineFrame.FileDisplay_JTbl', 'Data,2')
		select_menu('Goto Line')
		select('Line Number_Txt', '111')
		click('Goto')
		assert_p('TextField', 'Text', 'line number must be < 17')
		select('Line Number_Txt', '11')
		click('Goto')
		assert_p('LineFrame.Record_Txt', 'Text', '11')
##		assert_p('LineFrame.FileDisplay_JTbl', 'Content', '''[[KEYCODE-NO, 1, 8, Char, 60694698, 60694698, f6f0f6f9f4f6f9f8], [STORE-NO, 9, 2, Mainframe Packed Decimal (comp-3), 59, �, 059c], [DATE, 11, 4, Mainframe Packed Decimal (comp-3), 40118,   �, 0040118c], [DEPT-NO, 15, 2, Mainframe Packed Decimal (comp-3), 620, �, 620c], [QTY-SOLD, 17, 5, Mainframe Packed Decimal (comp-3), 1,     , 000000001c], [SALE-PRICE, 22, 6, Mainframe Packed Decimal (comp-3), 3.99,     ?�, 00000000399c]]''')
##		assert_p('LineFrame.FileDisplay_JTbl', 'Content', '''[[KEYCODE-NO, 1, 8, Char, 60694698, 60694698, f6f0f6f9f4f6f9f8], [STORE-NO, 9, 2, Mainframe Packed Decimal (comp-3), 59, �, 059c], [DATE, 11, 4, Mainframe Packed Decimal (comp-3), 40118,   �, 0040118c], [DEPT-NO, 15, 2, Mainframe Packed Decimal (comp-3), 620, �, 620c], [QTY-SOLD, 17, 5, Mainframe Packed Decimal (comp-3), 1,     , 000000001c], [SALE-PRICE, 22, 6, Mainframe Packed Decimal (comp-3), 3.99,     ?�, 00000000399c]]''')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
	close()
