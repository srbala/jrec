useFixture(default)

def test():
	from Modules import commonBits
	java_recorded_version = '1.6.0_17'

	if window(commonBits.applicationName()):
		select('FileNameTxtFld', commonBits.sampleDir() + 'protoStoreSales3a.bin')
		click('Edit1')
##		select('JTreeTable', '')
		rightclick('JTreeTable', 'Tree,1')
		select_menu('Fully Expand Tree')
		select('LayoutCombo', 'Product')
		select('JTreeTable', 'cell:saleDate,5(40118)')
		assert_p('JTreeTable', 'Content', '[[, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , 61664713, 40118, 1, 17990], [, , 61664713, 40118, -1, -17990], [, , 61684613, 40118, 1, 12990], [, , , , , ], [, , , , , ], [, , , , , ], [, , 68634752, 40118, 1, 8990], [, , , , , ], [, , , , , ], [, , , , , ], [, , 60664659, 40118, 1, 3990], [, , 60694698, 40118, 1, 3990], [, , , , , ], [, , , , , ], [, , , , , ], [, , 60614487, 40118, 1, 5950], [, , 63644339, 40118, 1, 12650], [, , , , , ], [, , , , , ], [, , , , , ], [, , 67674686, 40118, 1, 3990], [, , , , , ], [, , , , , ], [, , , , , ], [, , 62684217, 40118, 1, 9990], [, , 64614401, 40118, 1, 1990], [, , 64614401, 40118, 1, 1990], [, , 64624770, 40118, 1, 2590], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ]]')
		select('JTreeTable', 'rows:[31,32],columns:[saleDate]')
		select_menu('Edit>>Copy Record#{s#}')
		select('JTreeTable', 'cell:saleDate,6(40118)')
		select_menu('Edit>>Paste Record#{s#}')
		select('JTreeTable', 'cell:keycode,5(61664713)')
		assert_p('JTreeTable', 'Content', '[[, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , 61664713, 40118, 1, 17990], [, , 61664713, 40118, -1, -17990], [, , 64614401, 40118, 1, 1990], [, , 64624770, 40118, 1, 2590], [, , 61684613, 40118, 1, 12990], [, , , , , ], [, , , , , ], [, , , , , ], [, , 68634752, 40118, 1, 8990], [, , , , , ], [, , , , , ], [, , , , , ], [, , 60664659, 40118, 1, 3990], [, , 60694698, 40118, 1, 3990], [, , , , , ], [, , , , , ], [, , , , , ], [, , 60614487, 40118, 1, 5950], [, , 63644339, 40118, 1, 12650], [, , , , , ], [, , , , , ], [, , , , , ], [, , 67674686, 40118, 1, 3990], [, , , , , ], [, , , , , ], [, , , , , ], [, , 62684217, 40118, 1, 9990], [, , 64614401, 40118, 1, 1990], [, , 64614401, 40118, 1, 1990], [, , 64624770, 40118, 1, 2590], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ]]')
		select_menu('Utilities>>Compare with Disk')
		select('Table', 'cell:saleDate,1(40118)')
		assert_p('Table', 'Content', '[[, , , , , , ], [, Inserted, 37, 64614401, 40118, 1, 1990], [, , , , , , ], [, Inserted, 38, 64624770, 40118, 1, 2590]]')
		select('Table', 'cell:saleDate,1(40118)')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
		click('Save')
		select_menu('Utilities>>Compare with Disk')
		assert_p('TextPane', 'Text', 'Files are Identical !!!')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
		select_menu('Window>>protoStoreSales3a.bin>>Tree View')
		select('JTreeTable', 'rows:[7,8],columns:[saleDate]')
		rightclick('JTreeTable', 'saleDate,7')
		select_menu('Delete Record#{s#}')
		select('JTreeTable', 'cell:keycode,6(61664713)')
		assert_p('JTreeTable', 'Content', '[[, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , 61664713, 40118, 1, 17990], [, , 61664713, 40118, -1, -17990], [, , 61684613, 40118, 1, 12990], [, , , , , ], [, , , , , ], [, , , , , ], [, , 68634752, 40118, 1, 8990], [, , , , , ], [, , , , , ], [, , , , , ], [, , 60664659, 40118, 1, 3990], [, , 60694698, 40118, 1, 3990], [, , , , , ], [, , , , , ], [, , , , , ], [, , 60614487, 40118, 1, 5950], [, , 63644339, 40118, 1, 12650], [, , , , , ], [, , , , , ], [, , , , , ], [, , 67674686, 40118, 1, 3990], [, , , , , ], [, , , , , ], [, , , , , ], [, , 62684217, 40118, 1, 9990], [, , 64614401, 40118, 1, 1990], [, , 64614401, 40118, 1, 1990], [, , 64624770, 40118, 1, 2590], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ], [, , , , , ]]')
		select_menu('Utilities>>Compare with Disk')
		select('Table', 'cell:saleDate,2(40118)')
		assert_p('Table', 'Content', '[[, Deleted, 37, 64614401, 40118, 1, 1990], [, , , , , , ], [, Deleted, 38, 64624770, 40118, 1, 2590], [, , , , , , ]]')
		select('Table', 'cell:saleDate,2(40118)')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
		select_menu('Window>>protoStoreSales3a.bin>>Tree View')
		click('Save')
		select_menu('Utilities>>Compare with Disk')
		assert_p('TextPane', 'Text', 'Files are Identical !!!')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
	close()
