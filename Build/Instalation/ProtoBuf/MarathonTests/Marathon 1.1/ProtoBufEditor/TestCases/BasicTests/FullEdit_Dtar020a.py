useFixture(default)

def test():
	from Modules import commonBits
	java_recorded_version = '1.5.0_11'

	if window(commonBits.applicationName()):
		select('FileNameTxtFld', commonBits.sampleDir() + 'protoSales.bin')
		##select('FileNameTxtFld', '/C:/Program Files/RecordEdit/MSaccess/SampleFiles/DTAR020.bin')


		click('Edit1')


		select('LinesTbl', 'cell:2|store,1(20)')
		rightclick('LinesTbl', '2|store,1')
		select_menu('Sort')


		#select('List', 'sale')
		select('Table', 'keycode', 'Field,0')
		select('Table', 'cell:Field,0(KEYCODE)')
		click('Sort1')
		select('LinesTbl', 'cell:1|keycode,0(60604100)')
		assert_p('LinesTbl', 'Text', '60604100', '1|keycode,0')
		select_menu('Window>>protoSales.bin>>Table:')
		select('LinesTbl', 'cell:1|keycode,0(60604100)')
		rightclick('LinesTbl', '1|keycode,0')
		select_menu('Edit Record')
##		select('Table1', 'cell:1|keycode,0(60604100)')
		select('BaseLineAsColumn$LineAsColTbl', 'cell:Data,5(13.30)')
		select('BaseLineAsColumn$LineAsColTbl', 'cell:Data,5(13.30)')
		click('Right')
		select('BaseLineAsColumn$LineAsColTbl', 'cell:Data,5(9.00)')
		assert_p('BaseLineAsColumn$LineAsColTbl', 'Content', '[[keycode, 1, , 60604880, 60604880], [store, 2, , 184, 184], [department, 3, , 250, 250], [saleDate, 4, , 40118, 40118], [quantity, 5, , 1, 1], [price, 6, , 9000, 9000]]')

		select('BaseLineAsColumn$LineAsColTbl', 'cell:Data,2(40118)')
		assert_p('BaseLineAsColumn$LineAsColTbl', 'Text', '250', 'Data,2')
		select('BaseLineAsColumn$LineAsColTbl', 'cell:Data,2(40118)')
		click('Right')
		select('BaseLineAsColumn$LineAsColTbl', 'cell:Data,5(-14.25)')
		select('BaseLineAsColumn$LineAsColTbl', 'cell:Data,5(-14.25)')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
		select_menu('Window>>protoSales.bin>>Table:')
		select('LinesTbl', 'cell:1|keycode,0(60604100)')
	close()

#### component <Table> : expected {[[KEYCODE, 1, 8, 69664668, 69664668, f6f9f6f6f4f6f6f8], [STORE, 9, 2, 184, <, 184c], [DATE, 11, 4, 40118,   �, 0040118c], [DEPT-NO, 15, 2, 903, �, 903c], [QTY-SOLD, 17, 5, 1,     , 000000001c], [SALE-PRICE, 22, 6, 8.95,     i*, 00000000895c]]} but was {[[keycode, 1, , 69664668, 69664668], [store, 2, , 184, 184], [department, 3, , 903, 903], [saleDate, 4, , 40118, 40118], [quantity, 5, , 1, 1], [price, 6, , 8950, 8950]]}	C:\Users\bm\marathon\ProtoBuf\TestCases\BasicTests\FullEdit_Dtar020.py	line 45 in function test

