useFixture(default)

def test():
	from Modules import commonBits
	import os
	java_recorded_version = '1.6.0_17'

	if window(commonBits.applicationName()):
		select('FileNameTxtFld', commonBits.sampleDir() + 'zXzCreateSales3.bin')
		select('FileNameTxtFld1', commonBits.stdCopybookDir() + 'StoreSales3.proto')
		select('ComboBox1', 'Proto Definition')
		click('Edit1')
		assert_p('BaseLineAsColumn$LineAsColTbl', 'Content', '[[store, 1, , 0, 0], [name, 2, , , ]]')
		select('BaseLineAsColumn$LineAsColTbl', '11', 'Data,0')
		select('BaseLineAsColumn$LineAsColTbl', 'name 11', 'Data,1')
		select('BaseLineAsColumn$LineAsColTbl', 'cell:Data,0(11)')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
		select_menu('Window>>zXzCreateSales3.bin>>Tree View')
		select('LayoutCombo', 'Store')
		assert_p('JTreeTable', 'Content', '[[, , 11, name 11]]')
		select('JTreeTable', 'cell:Tree,0(null)')
		click('New')

		if window('Record Selection'):
			click('OK')
		close()

		select('BaseLineAsColumn$LineAsColTbl', '121', 'Data,0')
		select('BaseLineAsColumn$LineAsColTbl', 'name 121', 'Data,1')
		select('BaseLineAsColumn$LineAsColTbl', 'cell:Data,0(121)')
		assert_p('BaseLineAsColumn$LineAsColTbl', 'Content', '[[department, 1, , 121, 121], [name, 2, , name 121, name 121]]')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
		select_menu('Window>>zXzCreateSales3.bin>>Tree View')
		select('LayoutCombo', 'Prefered')
##		select('JTreeTable', '')
		rightclick('JTreeTable', 'Tree,0')
		select_menu('Expand Tree')
##		select('JTreeTable', '')
		rightclick('JTreeTable', 'Tree,1')
		select_menu('Expand Tree')
		assert_p('JTreeTable', 'Content', '[[, , 11, name 11, , ], [, , , , , ], [, , 121, name 121, , ]]')
		click('Save1')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
		click('Edit1')
##		select('JTreeTable', '')
		rightclick('JTreeTable', 'Tree,1')
		select_menu('Expand Tree')
		assert_p('JTreeTable', 'Content', '[[, , 11, name 11], [, , , ], [, , , ]]')
		select('LayoutCombo', 'Prefered')
		assert_p('JTreeTable', 'Content', '[[, , 11, name 11, , ], [, , , , , ], [, , 121, name 121, , ]]')
		select('JTreeTable', 'cell:Tree,0(null)')
		click('Delete2')
		click('BasicInternalFrameTitlePane$NoFocusButton2')

		if window('Save Changes to file: ' + commonBits.sampleDir() + 'zXzCreateSales3.bin'):
			click('Yes')
		close()

		click('Edit1')
		assert_p('BaseLineAsColumn$LineAsColTbl', 'Content', '[[store, 1, , 0, 0], [name, 2, , , ]]')
		click('Delete2')
		click('BasicInternalFrameTitlePane$NoFocusButton2')

		if window('Save Changes to file: ' + commonBits.sampleDir() + 'zXzCreateSales3.bin'):
			click('No')
		close()

		click('Edit1')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
		select('LayoutCombo', 'Store')
		assert_p('JTreeTable', 'Content', '[[, , 0, ]]')
		select('JTreeTable', 'cell:Tree,0(null)')
		click('Delete2')
		click('Save1')
		click('Save1')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
		os.remove(commonBits.sampleDir() + 'zXzCreateSales3.bin')
	close()
