useFixture(default)

def test():
	from Modules import commonBits
	java_recorded_version = '1.6.0_10'

	if window('Record Editor'):
		select('FileChooser', commonBits.sampleDir() + 'Ams_PODownload_20041231.txt')
		click('Edit1')
		select_menu('View>>Record Based Tree')
		select('Table', '1', 'Parent Record,0')
		select('Table', '0', 'Parent Record,2')
		select('Table', 'cell:Parent Record,2(0)')
		click('Build')
		select_menu('File>>Save Tree as XML')

		if window('Open'):
			select('File Name', 'xmlTreeSaveAms_PODownload_20041231.xml')
			click('Open')
		close()

		select_menu('File>>Compare Menu')
		click('*2')
		select('FileChooser', commonBits.sampleDir() + 'xmlTreeSaveAms_PODownload_20041231.xml')
		click('Right')
		select('TabbedPane', '')
		select('FileChooser', commonBits.sampleDir() + 'Ams_PODownload_20041231.txt')
		click('Right')
		select('TabbedPane', '')
		select('Table', 'cell:Equivalent Record,2(-1)')
##		select('Table', '1', 'Equivalent Record,2')
##		select('Table', '0', 'Equivalent Record,3')
##		select('Table', '2', 'Equivalent Record,4')
		select('Table', 'ams PO Download: Detail', 'Equivalent Record,2')
		select('Table', 'ams PO Download: Header', 'Equivalent Record,3')
		select('Table', 'ams PO Download: Allocation', 'Equivalent Record,4')
		click('FieldChoice', 727, 517)
		click('ReFrame', 790, 602)
		click('Right')
		select('TabbedPane', '')
		click('Compare')
		assert_p('TextPane', 'Text', 'Files are Identical !!!')

		select_menu('Window>>Menu>>Compare Menu')
		click('*2')
		select('FileChooser', commonBits.sampleDir() +  'Ams_PODownload_20041231.txt')
		click('Right')
		select('TabbedPane', '')
		select('FileChooser', commonBits.sampleDir() +  'xmlTreeSaveAms_PODownload_20041231.xml')
		click('Right')
		select('TabbedPane', '')
#		select('Table', 'cell:Equivalent Record,0(-1)')
#		select('Table', '3', 'Equivalent Record,0')
#		select('Table', '2', 'Equivalent Record,1')
#		select('Table', '4', 'Equivalent Record,2')
		select('Table', 'ams_PO_Download__Detail', 'Equivalent Record,0')
		select('Table', 'ams_PO_Download__Header', 'Equivalent Record,1')
		select('Table', 'ams_PO_Download__Allocation', 'Equivalent Record,2')
		select('Table', 'cell:Equivalent Record,2(4)')
		click('Right')
		select('TabbedPane', '')
		click('Compare')
		assert_p('TextPane', 'Text', 'Files are Identical !!!')

	close()
