useFixture(default)

def test():
	from Modules import commonBits
	java_recorded_version = '1.6.0_17'

	if window('Record Editor'):
		select('FileChooser', commonBits.sampleDir() + 'Ams_PODownload_20050101.txt')
		commonBits.selectOldFilemenu(select_menu, 'Utilities', 'File Copy Menu')
		click('*4')
		select('FileChooser', commonBits.sampleDir() + 'Ams_PODownload_20050101.txt')
		select('FileChooser1', commonBits.sampleDir() + 'CpyXml_Ams_PODownload_20050101.xml')
		###select('ComboBox1', 'Ams')
		select('ComboBox2', 'ams PO Download')
		click('Right')
		select('TabbedPane', '')
		assert_p('Table1', 'Content', '[[Record Type, true], [Pack Qty, true], [Pack Cost, true], [APN, true], [Filler, true], [Product, true], [pmg dtl tech key, true], [Case Pack id, true], [Product Name, true]]')
		assert_p('Table', 'Content', '[[ams PO Download: Detail, true], [ams PO Download: Header, true], [ams PO Download: Allocation, true]]')
		select('Table1', 'cell:Include,4(true)')
		select('Table', 'cell:Record,1(ams PO Download: Header)')
		select('Table1', 'cell:Include,5(true)')
		select('Table', 'cell:Record,1(ams PO Download: Header)')
		click('Right')
		select('TabbedPane', '')
		select('Table', 'cell:Parent Record,0(-1)')


		select('Table', 'ams PO Download: Header', 'Parent Record,0')
		select('Table', 'ams PO Download: Detail', 'Parent Record,2')

##		select('Table', '1', 'Parent Record,0')
##		select('Table', '0', 'Parent Record,2')

		select('Table', 'cell:Parent Record,2(0)')
		assert_p('Table', 'Content', '[[ams PO Download: Detail, 1], [ams PO Download: Header, -1], [ams PO Download: Allocation, 0]]')
		select('Table', 'cell:Parent Record,2(0)')
		click('Right')
		select('TabbedPane', '')
		click('Copy2')
		assert_p('TextField1', 'Text', 'Copy Done !!! ')

		commonBits.selectOldFilemenu(select_menu, 'Utilities', 'Compare Menu')
		click('*2')
		select('FileChooser', commonBits.sampleDir() + 'Ams_PODownload_20050101.txt')
		select('ComboBox2', 'ams PO Download')
		click('Right')
		select('TabbedPane', '')
		select('FileChooser', commonBits.sampleDir() + 'CpyXml_Ams_PODownload_20050101.xml')
		click('Right')
		select('TabbedPane', '')
		select('Table', 'cell:Equivalent Record,0(-1)')
		select('Table', 'cell:Equivalent Record,0(-1)')
		keystroke('Table', 'Ctrl+V', 'Equivalent Record,0')
#		select('Table', '-1', 'Equivalent Record,0')
#		select('Table', '-1', 'Equivalent Record,1')
		select('Table', ' ', 'Equivalent Record,0')


		select('Table', ' ', 'Equivalent Record,1')
		select('Table', 'cell:Equivalent Record,0(-1)')
		keystroke('Table', 'Ctrl+V', 'Equivalent Record,0')
		select('Table', 'ams_PO_Download__Detail', 'Equivalent Record,0')
		select('Table', 'cell:Equivalent Record,0(3)')
		select('Table', 'cell:Equivalent Record,0(3)')
		select('Table', 'cell:Equivalent Record,1(0)')
		select('Table', 'ams_PO_Download__Header', 'Equivalent Record,1')
##		select('Table', 'cell:Equivalent Record,1(0)')

		select('Table', 'ams_PO_Download__Allocation', 'Equivalent Record,2')
		
##		select('Table', 'cell:Equivalent Record,2(4)')
		select('Table', 'ams_PO_Download__Allocation', 'Equivalent Record,2')
##		select('Table', 'cell:Equivalent Record,2(4)')
		click('Right')
		select('TabbedPane', '')
		click('Compare')
		assert_p('TextPane', 'Text', 'Files are Identical !!!')
	close()
