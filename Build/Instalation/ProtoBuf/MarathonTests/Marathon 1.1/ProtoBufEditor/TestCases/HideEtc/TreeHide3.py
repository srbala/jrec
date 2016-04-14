useFixture(default)

def test():
	from Modules import commonBits
	java_recorded_version = '1.6.0_17'

	if window(commonBits.applicationName()):
		select('FileNameTxtFld', commonBits.sampleDir() +  'protoStoreSales3.bin')
		click('Edit1')
##		select('JTreeTable', '')
		rightclick('JTreeTable', 'Tree,0')
		select_menu('Fully Expand Tree')
##		select('JTreeTable', '')
		rightclick('JTreeTable', 'Tree,9')
		select_menu('Edit Record')
		assert_p('BaseLineAsColumn$LineAsColTbl', 'Content', '[[keycode, 1, , 69684558, 69684558], [saleDate, 2, , 40118, 40118], [quantity, 3, , -1, -1], [price, 4, , -19000, -19000]]')
##		select('BaseLineAsColumn$LineAsColTbl', '')
		rightclick('BaseLineAsColumn$LineAsColTbl', 'Data,3')
		select_menu('Hide Column')
		assert_p('BaseLineAsColumn$LineAsColTbl', 'Content', '[[keycode, 1, , 69684558, 69684558], [saleDate, 2, , 40118, 40118], [quantity, 3, , -1, -1]]')
##		select('Table', '')
		rightclick('BaseLineAsColumn$LineAsColTbl', 'Data,2')
		select_menu('Hide Column')
		assert_p('BaseLineAsColumn$LineAsColTbl', 'Content', '[[keycode, 1, , 69684558, 69684558], [saleDate, 2, , 40118, 40118]]')
##		select('Table', '')
		rightclick('BaseLineAsColumn$LineAsColTbl', 'Data,1')
		select_menu('Hide Column')
		assert_p('BaseLineAsColumn$LineAsColTbl', 'Content', '[[keycode, 1, , 69684558, 69684558]]')
##		select('Table', '')
		rightclick('BaseLineAsColumn$LineAsColTbl', 'Data,0')
		select_menu('Show Product Fields>>saleDate')
		assert_p('BaseLineAsColumn$LineAsColTbl', 'Content', '[[keycode, 1, , 69684558, 69684558], [saleDate, 2, , 40118, 40118]]')
##		select('Table', '')
		rightclick('BaseLineAsColumn$LineAsColTbl', 'Data,1')
		select_menu('Show Product Fields>>quantity')
		assert_p('BaseLineAsColumn$LineAsColTbl', 'Content', '[[keycode, 1, , 69684558, 69684558], [saleDate, 2, , 40118, 40118], [quantity, 3, , -1, -1]]')
##		select('Table', '')
		rightclick('BaseLineAsColumn$LineAsColTbl', 'Data,2')
		select_menu('Show Product Fields>>price')
		assert_p('BaseLineAsColumn$LineAsColTbl', 'Content', '[[keycode, 1, , 69684558, 69684558], [saleDate, 2, , 40118, 40118], [quantity, 3, , -1, -1], [price, 4, , -19000, -19000]]')
##		select('Table', '')
		rightclick('BaseLineAsColumn$LineAsColTbl', 'Data,0')
		select_menu('Hide Column')
		assert_p('BaseLineAsColumn$LineAsColTbl', 'Content', '[[saleDate, 2, , 40118, 40118], [quantity, 3, , -1, -1], [price, 4, , -19000, -19000]]')
##		select('Table', '')
		rightclick('BaseLineAsColumn$LineAsColTbl', 'Data,0')
		select_menu('Hide Column')
		assert_p('BaseLineAsColumn$LineAsColTbl', 'Content', '[[quantity, 3, , -1, -1], [price, 4, , -19000, -19000]]')
##		select('Table', '')
		rightclick('BaseLineAsColumn$LineAsColTbl', 'Data,0')
		select_menu('Hide Column')
		assert_p('BaseLineAsColumn$LineAsColTbl', 'Content', '[[price, 4, , -19000, -19000]]')
##		select('Table', '')
		
		rightclick('BaseLineAsColumn$LineAsColTbl', 'Data,0')
		
		select_menu('Show Product Fields>>keycode')

		assert_p('BaseLineAsColumn$LineAsColTbl', 'Content', '[[keycode, 1, , 69684558, 69684558], [price, 4, , -19000, -19000]]')
##		select('Table', '')
		rightclick('BaseLineAsColumn$LineAsColTbl', 'Data,1')
		select_menu('Show Product Fields>>saleDate')
		assert_p('BaseLineAsColumn$LineAsColTbl', 'Content', '[[keycode, 1, , 69684558, 69684558], [saleDate, 2, , 40118, 40118], [price, 4, , -19000, -19000]]')
##		select('Table', '')
		rightclick('BaseLineAsColumn$LineAsColTbl', 'Data,1')
		select_menu('Show Product Fields>>quantity')
		assert_p('BaseLineAsColumn$LineAsColTbl', 'Content', '[[keycode, 1, , 69684558, 69684558], [saleDate, 2, , 40118, 40118], [quantity, 3, , -1, -1], [price, 4, , -19000, -19000]]')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
	close()
