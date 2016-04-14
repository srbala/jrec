useFixture(default)

def test():
	from Modules import commonBits
	java_recorded_version = '1.6.0_17'

	if window(commonBits.applicationName()):
		select('FileNameTxtFld', commonBits.sampleDir() + 'protoStoreSales3SDim.bin')
		click('Edit1')
##		select('JTreeTable', '')
		rightclick('JTreeTable', 'Tree,3')
		select_menu('Edit Record')
		click('Find1')
##		click('MetalInternalFrameTitlePane', 237, 12)
		select('TextField', '66')
		select('LayoutCombo', 'Product')
		select('ComboBox', 'keycode')
		select('ComboBox2', 'Backward')
		click('Find1')
		select_menu('Window>>protoStoreSales3SDim.bin>>Record: ')
		select('BaseLineAsColumn$LineAsColTbl', 'cell:Data,1(40118)')
		assert_p('BaseLineAsColumn$LineAsColTbl', 'Content', '[[keycode, 1, , 66624829, 66624829], [saleDate, 2, , 40118, 40118], [quantity, 3, , 1, 1], [price, 4, , 1990, 1990]]')
		click('Find1')
		select('ComboBox', 'keycode')
		click('Find1')
		select_menu('Window>>protoStoreSales3SDim.bin>>Record: ')
		select('BaseLineAsColumn$LineAsColTbl', 'cell:Data,2(1)')
		assert_p('BaseLineAsColumn$LineAsColTbl', 'Content', '[[keycode, 1, , 66624253, 66624253], [saleDate, 2, , 40118, 40118], [quantity, 3, , 1, 1], [price, 4, , 3490, 3490]]')
		click('Find1')
		select('ComboBox', 'keycode')
		click('Find1')
		select_menu('Window>>protoStoreSales3SDim.bin>>Record: ')
		select('BaseLineAsColumn$LineAsColTbl', 'cell:Data,1(40118)')
		assert_p('BaseLineAsColumn$LineAsColTbl', 'Content', '[[keycode, 1, , 66624253, 66624253], [saleDate, 2, , 40118, 40118], [quantity, 3, , 1, 1], [price, 4, , 3490, 3490]]')
		click('Find1')
		select('ComboBox', 'keycode')
		click('Find1')
		select_menu('Window>>protoStoreSales3SDim.bin>>Record: ')
		select('BaseLineAsColumn$LineAsColTbl', 'cell:Data,1(40118)')
		assert_p('BaseLineAsColumn$LineAsColTbl', 'Content', '[[keycode, 1, , 62664909, 62664909], [saleDate, 2, , 40118, 40118], [quantity, 3, , 1, 1], [price, 4, , 3290, 3290]]')
		click('Find1')
##		click('MetalInternalFrameTitlePane', 127, 12)
		select('ComboBox', 'keycode')
		click('Find1')
		select_menu('Window>>protoStoreSales3SDim.bin>>Record: ')
		select('BaseLineAsColumn$LineAsColTbl', 'cell:Data,0(67664966)')
		assert_p('BaseLineAsColumn$LineAsColTbl', 'Content', '[[keycode, 1, , 67664966, 67664966], [saleDate, 2, , 40118, 40118], [quantity, 3, , 1, 1], [price, 4, , 890, 890]]')
		click('Find1')
##		click('BaseHelpPanel', 11, 15)
		select('ComboBox', 'keycode')
		click('Find1')
		select_menu('Window>>protoStoreSales3SDim.bin>>Record: ')
		select('BaseLineAsColumn$LineAsColTbl', 'cell:Data,0(67664966)')
		assert_p('BaseLineAsColumn$LineAsColTbl', 'Content', '[[keycode, 1, , 67664966, 67664966], [saleDate, 2, , 40118, 40118], [quantity, 3, , 1, 1], [price, 4, , 890, 890]]')

	close()