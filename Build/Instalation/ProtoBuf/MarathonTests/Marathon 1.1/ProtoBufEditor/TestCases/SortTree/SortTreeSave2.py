useFixture(default)

def test():
	from Modules import commonBits
	java_recorded_version = '1.6.0_03'

	if window(commonBits.applicationName()):
		select('FileNameTxtFld', commonBits.sampleDir() + 'protoSales.bin')

		click('Edit1')
		select_menu('View>>Sorted Field Tree')
		#select('List', 'sale')
		#select('List', 'sale')
		select('Table', 'cell:Field,0( )')
		#select('List', 'sale')
		select('Table', 'department', 'Field,0')
		select('Table', 'saleDate', 'Field,1')
		select('Table', 'cell:Field,1(date)')
		select('Table1', 'cell:Function,2()')
		select('Table', 'cell:Field,1(date)')
		select('Table1', 'Maximum', 'Function,2')
		select('Table1', 'Maximum', 'Function,3')
		select('Table1', 'Sum', 'Function,4')
		select('Table1', 'Sum', 'Function,5')
		select('Table1', 'cell:Function,5(Sum)')
		click('Save1')
		##select('FileNameTxtFld', commonBits.userDir() +  'SortTree'  + commonBits.fileSep() + 'xx2')
		commonBits.selectFileName(select, commonBits.userDir() +  'SortTree'  + commonBits.fileSep() + 'xx2')


		click('Save1')
		select_menu('Window>>protoSales.bin>>Create Sorted Tree')
		click('Build Tree')
		select('JTreeTable', 'cell:saleDate,0(40118)')
		assert_p('JTreeTable', 'Text', '40118', 'saleDate,0')
		select('JTreeTable', 'cell:department,0(60)')
		assert_p('JTreeTable', 'Text', '5', 'quantity,2')
		select('JTreeTable', 'cell:price,0(8740)')
		assert_p('JTreeTable', 'Text', '166940', 'price,1')
		select('JTreeTable', 'cell:price,1(166940)')
		assert_p('JTreeTable', 'Text', '166940', 'price,1')
		select('JTreeTable', 'cell:Tree,1(null)')
		rightclick('JTreeTable', 'Tree,1')
		select_menu('Expand Tree')
		select('JTreeTable', 'cell:quantity,2(8)')
		assert_p('JTreeTable', 'Text', '5', 'quantity,3')
		select('JTreeTable', 'cell:Tree,2(null)')
		rightclick('JTreeTable', 'Tree,2')
		select_menu('Expand Tree')
		select('JTreeTable', 'cell:price,3(12990)')
		assert_p('JTreeTable', 'Text', '12990', 'price,4')
		select('JTreeTable', 'cell:Tree,14(null)')
		rightclick('JTreeTable', 'Tree,14')
		select_menu('Edit Record')
		select('JTreeTable', 'cell:Tree,14(null)')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
		select_menu('Window>>protoSales.bin>>Table:')
		select_menu('View>>Execute Sort Tree')
		##select('FileNameTxtFld', commonBits.userDir() +  'SortTree'  + commonBits.fileSep() + 'xx2')
		commonBits.selectFileName(select, commonBits.userDir() +  'SortTree'  + commonBits.fileSep() + 'xx2')

		click('Run')
		select('JTreeTable', 'cell:price,1(166940)')
		assert_p('JTreeTable', 'Text', '166940', 'price,1')
		select('JTreeTable', 'cell:price,2(87460)')
		assert_p('JTreeTable', 'Text', '87460', 'price,2')
		select('JTreeTable', 'cell:price,3(-15850)')
		assert_p('JTreeTable', 'Text', '-15850', 'price,3')
		select('JTreeTable', 'cell:price,9(-4000)')
		select('JTreeTable', 'cell:price,7(14090)')
		assert_p('JTreeTable', 'Text', '17730', 'price,8')
	close()

