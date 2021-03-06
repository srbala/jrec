useFixture(default)

def test():
	from Modules import commonBits
	java_recorded_version = '1.5.0_11'

	if window('Record Editor'):
		select('FileChooser', commonBits.sampleDir() + 'utf8a_Ams_LocDownload_20041228.txt')
		commonBits.setRecordLayout(select, 'utf8_ams Store')
		click('Edit1')
		select('Table', 'cell:10 - 35|Loc Name,1(VIC West Ad Support)')
		rightclick('Table', '10 - 35|Loc Name,1')
		select_menu('Edit Record')
	##	select('Table1', 'cell:10 - 35|Loc Name,1(VIC West Ad Support)')
		select('Table', 'cell:Data,3(VIC West Ad Support)')
		assert_p('Table', 'Text', 'VIC West Ad Support', 'Data,3')
		select('Table', 'cell:Data,3(VIC West Ad Support)')
		assert_p('Table', 'Text', 'cell:Data,3(VIC West Ad Support)')
		select('Table', 'cell:Data,3(VIC West Ad Support)')

		if commonBits.isMissingCol():
			assert_p('Table', 'RowCount', '9')
		else:
			assert_p('Table', 'RowCount', '10')

		select('Table', 'cell:Data,3(VIC West Ad Support)')
		select('Table', 'cell:Data,4()')
		select('Table', 'cell:Data,4()')
		click('Right')
		click('Left')
		click('Left')
		select('Table', 'cell:Data,2(DC)')

		if commonBits.isMissingCol():
			assert_p('Table', 'RowCount', '9')
		else:
			assert_p('Table', 'RowCount', '10')

		select('Table', 'cell:Data,2(DC)')
		assert_p('Table', 'ColumnCount', '5')
		select('Table', 'cell:Data,2(DC)')
		click('RightM')
		select('Table', 'cell:Data,3(Kalgoorlie (not yet open))')
		assert_p('Table', 'Text', 'Kalgoorlie (not yet open)', 'Data,3')
		select('Table', 'cell:Data,3(Kalgoorlie (not yet open))')
		click('LeftM')
		select('Table', 'cell:Data,3(DC - Taras Ave)')
		assert_p('Table', 'Text', 'DC - Taras Ave', 'Data,3')
		select('Table', 'cell:Data,3(DC - Taras Ave)')
		assert_p('Table', 'Text', 'cell:Data,3(DC - Taras Ave)')
		select('Table', 'cell:Data,3(DC - Taras Ave)')
		commonBits.closeWindow(click)
		##click('BasicInternalFrameTitlePane$NoFocusButton2')
		commonBits.closeWindow(click)
		##click('BasicInternalFrameTitlePane$NoFocusButton2')
	close()
