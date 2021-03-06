useFixture(default)

def test():
	from Modules import commonBits
	java_recorded_version = '1.6.0_17'

	if window('Record Editor'):
		select('FileChooser', commonBits.sampleDir() + 'DTAR1000_Store_file_std.bin')
		select('ComboBox2', 'Unknown Format')
		select('ComboBox2', 'Unknown Mainframe VB')
		click('Edit1')
		select('Table', 'rows:[0,1,2,3,4],columns:[1 - 1|Data]')
		select_menu('View>>Table View #{Selected Records#}')
		select('LayoutCombo', 'Prefered')
		select_menu('Window>>DTAR1000_Store_file_std.bin>>Table:')
		select_menu('View>>Table View #{Selected Records#}')
		select('LayoutCombo', 'Full Line')
##		click('MetalInternalFrameTitlePane', 480, 12)
		select_menu('Window>>DTAR1000_Store_file_std.bin>>Table:')
		select_menu('View>>Table View #{Selected Records#}')
		select('LayoutCombo', 'Hex 1 Line')
##		assert_p('Table', 'Content', '[[[B@247b2e], [[B@1ef5e7d], [[B@13c5cc8], [[B@13cc73c], [[B@e5707f]]')
		assert_p('Table', 'Text', '00010014e540c78585939695874040404040404040404040404040404040404040404040404040404040404040404040404040404040d5e8d5d5d5d5', '         +         1|Hex (1 Line),0')
		assert_p('Table', 'Text', '')
		select_menu('Window>>DTAR1000_Store_file_std.bin>>Table:')
		select_menu('View>>Table View #{Selected Records#}')
		select('LayoutCombo', 'Hex 2 Lines (Mainframe Style)')
		assert_p('Table', 'Text', '')
		select_menu('Window>>DTAR1000_Store_file_std.bin>>Table:')
		select_menu('View>>Table View #{Selected Records#}')
		select('LayoutCombo', 'Hex 3 Lines (ISPF Edit Hex)')
##		assert_p('Table', 'Text', '''##0002d4d8898a444444444444444444444444444444444444444444dedddd
##030880413218000000000000000000000000000000000000000000585555''', '    +    1|Hex (SPF Edit Style),2')
		select_menu('Edit>>Change Layout')
###		select('ComboBox1', 'Mainframe')
		select('ComboBox2', 'DTAR1000 VB')
		click('Go')
		select_menu('Window>>DTAR1000_Store_file_std.bin>>Table:')
		assert_p('Table', 'Text', '')
		assert_p('Table', 'ColumnCount', '9')
		select('Table', 'cell:3 - 2|REGION-NO,4(20)')
		rightclick('Table', '3 - 2|REGION-NO,4')
		select_menu('Edit Record')
##		select('Table1', 'cell:3 - 2|REGION-NO,4(20)')
##		assert_p('Table', 'Content', '[[STORE-NO, 1, 2, 5, 		commonBits.closeWindow(click)
		##click('BasicInternalFrameTitlePane$NoFocusButton2')
##		select('Table', 'cell:3 - 2|REGION-NO,4(20)')
##		select('Table', 'cell:3 - 2|REGION-NO,4(20)')
		select_menu('Window>>DTAR1000_Store_file_std.bin>>Table:1')
##		select('Table2', 'cell:3 - 2|REGION-NO,4(20)')
		assert_p('Table', 'Content', '[[1, 20, V Geelong, N, Y, N, N, N, N], [2, 40, Q Coffs Harbour, N, Y, N, N, N, N], [3, 40, Q Mackay, N, Y, N, N, N, N], [4, 20, V Ballarat, N, Y, N, N, N, N], [5, 20, V Albury, N, Y, N, N, N, N]]')
		select_menu('Window>>DTAR1000_Store_file_std.bin>>Table:2')
		assert_p('Table', 'Content', '[[1, 20, V Geelong, N, Y, N, N, N, N], [2, 40, Q Coffs Harbour, N, Y, N, N, N, N], [3, 40, Q Mackay, N, Y, N, N, N, N], [4, 20, V Ballarat, N, Y, N, N, N, N], [5, 20, V Albury, N, Y, N, N, N, N]]')
		select_menu('Window>>DTAR1000_Store_file_std.bin>>Table:3')
		assert_p('Table', 'Content', '[[1, 20, V Geelong, N, Y, N, N, N, N], [2, 40, Q Coffs Harbour, N, Y, N, N, N, N], [3, 40, Q Mackay, N, Y, N, N, N, N], [4, 20, V Ballarat, N, Y, N, N, N, N], [5, 20, V Albury, N, Y, N, N, N, N]]')
		select_menu('Window>>DTAR1000_Store_file_std.bin>>Table:4')
		assert_p('Table', 'Content', '[[1, 20, V Geelong, N, Y, N, N, N, N], [2, 40, Q Coffs Harbour, N, Y, N, N, N, N], [3, 40, Q Mackay, N, Y, N, N, N, N], [4, 20, V Ballarat, N, Y, N, N, N, N], [5, 20, V Albury, N, Y, N, N, N, N]]')
		select_menu('Window>>DTAR1000_Store_file_std.bin>>Table:5')
		assert_p('Table', 'Content', '[[1, 20, V Geelong, N, Y, N, N, N, N], [2, 40, Q Coffs Harbour, N, Y, N, N, N, N], [3, 40, Q Mackay, N, Y, N, N, N, N], [4, 20, V Ballarat, N, Y, N, N, N, N], [5, 20, V Albury, N, Y, N, N, N, N]]')
		click('Open')
		select_menu('Window>>Open File')
##		select('ComboBox1', 'Mainframe')
		select('ComboBox2', 'DTAR1000 VB')
		click('Edit1')
		select('Table', 'cell:3 - 2|REGION-NO,2(40)')
		rightclick('Table', '3 - 2|REGION-NO,2')
		select_menu('Edit Record')
##		select('Table1', 'cell:3 - 2|REGION-NO,2(40)')
		select('Table', 'cell:Data,2(Q Mackay)')
		assert_p('Table', 'Text', 'N', 'Data,3')
		select('Table', 'cell:Data,1(40)')
		assert_p('Table', 'Text', 'cell:Data,1(40)')
		select('Table', 'cell:Data,0(3)')
		assert_p('Table', 'Text', '3', 'Data,0')
		select('Table', 'cell:Data,8(N)')
		assert_p('Table', 'Text', 'N', 'Data,8')
		select('Table', 'cell:Data,7(N)')
		assert_p('Table', 'Text', 'N', 'Data,7')
		select('Table', 'cell:Data,6(N)')
		assert_p('Table', 'Text', 'N', 'Data,6')
		select('Table', 'cell:Data,5(N)')
		assert_p('Table', 'Text', 'cell:Data,5(N)')
		select('Table', 'cell:Data,4(Y)')
		assert_p('Table', 'Text', 'Y', 'Data,4')
	close()


## component <Table> : expected {]
##[[STORE-NO, 1, 2, 5, ##[[STORE-NO, 1, 2, 5, 
##}	C:\Users\bm\marathon\HSQL_Edit\Untitled	line 45 in function test
