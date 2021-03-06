useFixture(default)

def test():
	from Modules import commonBits
	java_recorded_version = '1.6.0_17'

	if window(commonBits.applicationName()):
		select('FileNameTxtFld', commonBits.sampleDir() + 'protoStoreSales3.bin')
		click('Edit1')
##		select('JTreeTable', '')
		rightclick('JTreeTable', 'Tree,0')
		select_menu('Edit Record')
		select('BaseLineAsColumn$LineAsColTbl', 'cell:Data,0(20)')
		assert_p('BaseLineAsColumn$LineAsColTbl', 'Content', '[[store, 1, , 20, 20], [name, 2, , Store: 20, Store: 20]]')
		click('Find1')
		click('MetalInternalFrameTitlePane', 219, 13)
		select('TextField', '66')
		select('ComboBox', 'All Fields')
		click('Find1')
		select_menu('Window>>protoStoreSales3.bin>>Record: ')
		select('BaseLineAsColumn$LineAsColTbl', 'cell:Data,0(66624458)')
		assert_p('BaseLineAsColumn$LineAsColTbl', 'Content', '[[keycode, 1, , 66624458, 66624458], [saleDate, 2, , 40118, 40118], [quantity, 3, , 1, 1], [price, 4, , 890, 890]]')
		select_menu('Window>>protoStoreSales3.bin>>Find')
##		click('Find1')

		##click('Find1')
		select('ComboBox', 'All Fields')
		click('Find1')


		select_menu('Window>>protoStoreSales3.bin>>Record: ')
		select('BaseLineAsColumn$LineAsColTbl', 'cell:Data,0(66624458)')
		assert_p('BaseLineAsColumn$LineAsColTbl', 'Content', '[[keycode, 1, , 66624458, 66624458], [quantity, 2, , 1, 1]]')
		select_menu('Window>>protoStoreSales3.bin>>Find')
		click('Find1')

		click('Find1')
		select('ComboBox', 'All Fields')
		click('Find1')


		select_menu('Window>>protoStoreSales3.bin>>Record: ')
		select('BaseLineAsColumn$LineAsColTbl', 'cell:Data,1(40118)')
		assert_p('BaseLineAsColumn$LineAsColTbl', 'Content', '[[keycode, 1, , 61664713, 61664713], [saleDate, 2, , 40118, 40118], [quantity, 3, , -1, -1], [price, 4, , -17990, -17990]]')
#		click('Find1')
#		click('Find1')

		click('Find1')
		select('ComboBox', 'All Fields')
		click('Find1')


		select_menu('Window>>protoStoreSales3.bin>>Record: ')
		select('BaseLineAsColumn$LineAsColTbl', 'cell:Data,0(60664659)')
		assert_p('BaseLineAsColumn$LineAsColTbl', 'Content', '[[keycode, 1, , 60664659, 60664659], [quantity, 2, , 1, 1]]')
##		click('Find1')
##		click('Find1')


		click('Find1')
		select('ComboBox', 'All Fields')
		click('Find1')



		select_menu('Window>>protoStoreSales3.bin>>Record: ')
		select('BaseLineAsColumn$LineAsColTbl', 'cell:Data,0(166)')
		assert_p('BaseLineAsColumn$LineAsColTbl', 'Content', '[[store, 1, , 166, 166], [name, 2, , Store: 166, Store: 166]]')

	close()
