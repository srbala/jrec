useFixture(default)
##
##  Depends on 31 running
##
def test():
	java_recorded_version = '1.6.0_22'

	if window('Record Editor'):
		select_menu('Record Layouts>>Edit Layout')
		select('RecordList.Record Name_Txt', 'zx33xzFLDg65')
		select('RecordList.Description_Txt', '%')

##		select('TabbedPane', 'Child Records')
##		select('ChildRecordsJTbl', '')
		rightclick('ChildRecordsJTbl', 'Field Value,0')
		select_menu('Edit Record Selections')
		assert_p('RecordSelectionJTbl', 'Content', '[[, , fld 11, =, 11], [Or, , fld 12, =, 12], [Or, , fld 13, =, 13]]')
		select('TabbedPane', 'zx33xzFLD2')
		assert_p('RecordSelectionJTbl1', 'Content', '[[, , fld 21, =, 21], [Or, , fld 21, =, 12]]')
		select('TabbedPane', 'zx33xzFLD3')
		assert_p('RecordSelectionJTbl2', 'Content', '[[, , fld 31, =, 31]]')
		select('TabbedPane', 'Summary')
		assert_p('JTreeTable', 'Content', '[[, ,   ,   ,   , , =, ], [, , And  ,   ,   , fld 11, =, 11], [, ,   , Or  ,   , fld 12, =, 12], [, ,   , Or  ,   , fld 13, =, 13], [, ,   ,   ,   , , =, ], [, , And  ,   ,   , fld 21, =, 21], [, ,   , Or  ,   , fld 21, =, 12], [, ,   ,   ,   , , =, ], [, , And  ,   ,   , fld 31, =, 31]]')
		select('JTreeTable', '1199', 'Test Value ,1')
		select('JTreeTable', '1288', 'Test Value ,2')
		select('JTreeTable', '1377', 'Test Value ,3')
		select('JTreeTable', 'cell:Test Value ,2(1288)')
		assert_p('JTreeTable', 'Content', '[[, ,   ,   ,   , , =, ], [, , And  ,   ,   , fld 11, =, 1199], [, ,   , Or  ,   , fld 12, =, 1288], [, ,   , Or  ,   , fld 13, =, 1377], [, ,   ,   ,   , , =, ], [, , And  ,   ,   , fld 21, =, 21], [, ,   , Or  ,   , fld 21, =, 12], [, ,   ,   ,   , , =, ], [, , And  ,   ,   , fld 31, =, 31]]')
		select('TabbedPane', 'zx33xzFLD1')
		assert_p('RecordSelectionJTbl', 'Content', '[[, , fld 11, =, 1199], [Or, , fld 12, =, 1288], [Or, , fld 13, =, 1377]]')
		select('TabbedPane', 'zx33xzFLD2')
		assert_p('RecordSelectionJTbl1', 'Content', '[[, , fld 21, =, 21], [Or, , fld 21, =, 12]]')
		select('TabbedPane', 'zx33xzFLD3')
		assert_p('RecordSelectionJTbl2', 'Content', '[[, , fld 31, =, 31]]')
		select('TabbedPane', 'Summary')
		select('JTreeTable', 'fld 13', 'Field Name   ,1')
		select('JTreeTable', 'fld 11', 'Field Name   ,2')
		select('JTreeTable', 'fld 12', 'Field Name   ,3')
		select('JTreeTable', '31987', 'Test Value ,8')
		select('JTreeTable', 'fld 32', 'Field Name   ,8')
		select('JTreeTable', 'cell:Boolean op 3  ,5(  )')
		assert_p('JTreeTable', 'Content', '[[, ,   ,   ,   , , =, ], [, , And  ,   ,   , fld 13, =, 1199], [, ,   , Or  ,   , fld 11, =, 1288], [, ,   , Or  ,   , fld 12, =, 1377], [, ,   ,   ,   , , =, ], [, , And  ,   ,   , fld 21, =, 21], [, ,   , Or  ,   , fld 21, =, 12], [, ,   ,   ,   , , =, ], [, , And  ,   ,   , fld 32, =, 31987]]')
		select('TabbedPane', 'zx33xzFLD3')
		assert_p('RecordSelectionJTbl2', 'Content', '[[, , fld 32, =, 31987]]')
		select('TabbedPane', 'zx33xzFLD2')
		assert_p('RecordSelectionJTbl1', 'Content', '[[, , fld 21, =, 21], [Or, , fld 21, =, 12]]')
		select('TabbedPane', 'zx33xzFLD1')
		assert_p('RecordSelectionJTbl', 'Content', '[[, , fld 13, =, 1199], [Or, , fld 11, =, 1288], [Or, , fld 12, =, 1377]]')
		select('TabbedPane', 'Summary')
		select('JTreeTable', 'ff', 'Field Name   ,0')
		select('JTreeTable', 'vv1', 'Test Value ,0')
		select('JTreeTable', 'gg', 'Field Name   ,7')
		select('JTreeTable', 'vv2', 'Test Value ,7')
		select('JTreeTable', 'cell:Boolean op 3  ,5(  )')
		assert_p('JTreeTable', 'Content', '[[, ,   ,   ,   , ff, =, vv1], [, , And  ,   ,   , fld 13, =, 1199], [, ,   , Or  ,   , fld 11, =, 1288], [, ,   , Or  ,   , fld 12, =, 1377], [, ,   ,   ,   , , =, ], [, , And  ,   ,   , fld 21, =, 21], [, ,   , Or  ,   , fld 21, =, 12], [, ,   ,   ,   , gg, =, vv2], [, , And  ,   ,   , fld 32, =, 31987]]')
		select('JTreeTable', 'cell:Boolean op 3  ,5(  )')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
		assert_p('ChildRecordsJTbl', 'Content', '[[, zx33xzFLD1, , ff, vv1, , zx33xzFLD3], [, zx33xzFLD2, , , , , zx33xzFLD1], [, zx33xzFLD3, , gg, vv2, , ]]')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
	close()
