useFixture(default)

def test():
	from Modules import commonBits
	java_recorded_version = '1.6.0_22'

	if window('Record Editor'):
		select('File_Txt', commonBits.sampleDir() + 'Ams_PODownload_20041231.txt')
		click('Edit1')
		assert_p('LineList.Layouts_Txt', 'Text', 'Prefered')
		select_menu('View>>Record Based Tree')
		select('Recs_JTbl', 'ams PO Download: Header', 'Parent Record,0')
		select('Recs_JTbl', 'ams PO Download: Detail', 'Parent Record,2')
		select('Recs_JTbl', 'cell:Parent Record,2(0)')
		click('Build')
		select('LineTree.FileDisplay_JTbl', 'cell:Record Type,0(H1)')
		click('Find')
		select('Find.Search For_Txt', '00')
		click('Find1')
		assert_p('TextField', 'Text', 'Found (line, field Num, field position)=1, 6, 0')
		click('Find1')
		assert_p('TextField', 'Text', 'Found (line, field Num, field position)=1, 8, 1')
		click('Find1')
		assert_p('TextField', 'Text', 'Found (line, field Num, field position)=2, 1, 2')
		click('Find1')
		assert_p('TextField', 'Text', 'Found (line, field Num, field position)=2, 1, 4')
		assert_p('TextField', 'Text', 'Found (line, field Num, field position)=2, 1, 4')
		click('Find1')
		assert_p('TextField', 'Text', 'Found (line, field Num, field position)=2, 2, 2')
		click('Find1')
		assert_p('TextField', 'Text', 'Found (line, field Num, field position)=2, 3, 5')
		click('Find1')
		assert_p('TextField', 'Text', 'Found (line, field Num, field position)=2, 3, 7')
		click('Find1')
		click('Find1')
		assert_p('TextField', 'Text', 'Found (line, field Num, field position)=2, 3, 11')
		click('Find1')
		assert_p('TextField', 'Text', 'Found (line, field Num, field position)=2, 8, 11')
		click('Find1')
		assert_p('TextField', 'Text', 'Found (line, field Num, field position)=4, 1, 2')
		click('Find1')
		click('Find1')
		assert_p('TextField', 'Text', 'Found (line, field Num, field position)=4, 2, 6')
		click('Find1')
		assert_p('TextField', 'Text', 'Found (line, field Num, field position)=4, 8, 9')
		click('Find1')
		assert_p('TextField', 'Text', 'Found (line, field Num, field position)=6, 1, 3')
		click('Find1')
		assert_p('TextField', 'Text', 'Found (line, field Num, field position)=6, 1, 5')
		click('Find1')
		assert_p('TextField', 'Text', 'Found (line, field Num, field position)=6, 2, 6')
		click('Find1')
		assert_p('TextField', 'Text', 'Found (line, field Num, field position)=6, 8, 11')
		click('Find1')
		assert_p('TextField', 'Text', 'Found (line, field Num, field position)=9, 1, 2')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
	close()