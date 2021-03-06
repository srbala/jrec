useFixture(default)

def test():
	from Modules import commonBits
	java_recorded_version = '1.6.0_17'

	if window('Record Editor'):
		select('FileChooser', commonBits.sampleDir() +  'DTAR1000_Store_file_std.bin')
		select('ComboBox2', 'Unknown Mainframe VB')
##		click('ScrollPane$ScrollBar', 3, 29)
		commonBits.doEdit(click)

		select('Table', 'rows:[0,1,2,3],columns:[1 - 1|Data]')
		select_menu('View>>Table View #{Selected Records#}')
##		select('Table2', 'rows:[0,1,2,3],columns:[1 - 1|Data]')
##		assert_p('Table', 'Content', '[[  ?V Geelong                                         NYNNNN], [  ?Q Coffs Harbour                                   NYNNNN], [  ?Q Mackay                                          NYNNNN], [ ? ?V Ballarat                                        NYNNNN]]')
##		assert_p('Table', 'Content', '[[  ?V Geelong                                         NYNNNN], [  ?Q Coffs Harbour                                   NYNNNN], [  ?Q Mackay                                          NYNNNN], [ ? ?V Ballarat                                        NYNNNN]]'}
		commonBits.closeWindow(click)
		##click('BasicInternalFrameTitlePane$NoFocusButton2')
		select('Table', 'rows:[0,1,2,3],columns:[1 - 1|Data]')
		select('Table', 'rows:[0,1,2,3],columns:[1 - 1|Data]')
		assert_p('Table', 'RowCount', '147')
		select('Table', 'rows:[0,1,2,3],columns:[1 - 1|Data]')
		assert_p('Table', 'ColumnCount', '1')
		select('Table', 'rows:[0,1,2,3],columns:[1 - 1|Data]')
		commonBits.closeWindow(click)
		##click('BasicInternalFrameTitlePane$NoFocusButton2')
		click('Open')
		select('ComboBox2', 'DTAR1000 VB')
		click('Edit1')
		assert_p('Table', 'ColumnCount', '9')

	close()
