useFixture(default)

def test():
	from Modules import commonBits
	java_recorded_version = '1.6.0_22'

	if window('Record Layout Definitions'):
		click('*')
		select('RecordList.Record Name_Txt', 'xxzzxx')

		select('RecordList.Description_Txt', '%')


		assert_p('ChildRecordsJTbl', 'Content', '[[, ams PO Download: Allocation, , , , , ams PO Download: Detail], [, ams PO Download: Detail, , , , , ]]')
		commonBits.delete3(click)
		if window(commonBits.fl('Delete: xxzzxx')):
			click('Yes')
		close()


		select('RecordList.Record Name_Txt', 'xxzzxx11')

##		select('TabbedPane', 'Child Records')
		select('RecordList.Description_Txt', '%%')

##		select('TabbedPane', 'Child Records')
		assert_p('ChildRecordsJTbl', 'Content', '[[, ams PO Download: Allocation, , , , , ams PO Download: Detail], [, ams PO Download: Detail, , , , , ]]')
		commonBits.delete3(click)
		if window(commonBits.fl('Delete: xxzzxx11')):
			click('Yes')
		close()


		click('BasicInternalFrameTitlePane$NoFocusButton2')
	close()
