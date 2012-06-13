useFixture(default)

def test():
	java_recorded_version = '1.6.0_22'

	if window('Record Editor'):
		select_menu('Record Layouts>>Create Layout')

		select('RecordDef.Record Name_Txt', 'zx33xzFLDg543')
		select('RecordDef.Record Type_Txt', 'Group of Records')

		select('RecordDef.System_Txt', 'Unkown')
		click('Insert')
		click('Insert')
		click('Insert')
		select('ChildRecordsJTbl', 'cell:Child Record,0()')
		select('ChildRecordsJTbl', 'zx33xzFLD1', 'Child Record,0')
		select('ChildRecordsJTbl', 'zx33xzFLD2', 'Child Record,1')
		select('ChildRecordsJTbl', 'zx33xzFLD3', 'Child Record,2')
		select('ChildRecordsJTbl', 'cell:Child Record,2(zx33xzFLD3)')
		rightclick('ChildRecordsJTbl', 'Field Value,0')
		select_menu('Edit Record Selections')
		click('Insert')
		click('Insert')
		click('Insert')
#		select('RecordSelectionJTbl', 'And')
		rightclick('RecordSelectionJTbl', 'and,1')
#		select('RecordSelectionJTbl', 'And')
		rightclick('RecordSelectionJTbl', 'and,2')
		select('RecordSelectionJTbl', 'cell:Field,0()')
		select('RecordSelectionJTbl', 'fld 11', 'Field,0')
		select('RecordSelectionJTbl', 'fld 11', 'Field,1')
		select('RecordSelectionJTbl', 'fld 11', 'Field,2')
		select('RecordSelectionJTbl', '123', 'Field Value,0')
		select('RecordSelectionJTbl', '321', 'Field Value,1')
		select('RecordSelectionJTbl', '121', 'Field Value,2')
		select('TabbedPane', 'zx33xzFLD2')
		click('Insert1')
		select('RecordSelectionJTbl1', 'cell:Field,0()')
		select('RecordSelectionJTbl1', 'fld 21', 'Field,0')
		select('RecordSelectionJTbl1', '21', 'Field Value,0')
		select('RecordSelectionJTbl1', 'cell:Field Value,0()')
		click('Insert1')
		select('RecordSelectionJTbl1', 'cell:Field,1()')
		select('RecordSelectionJTbl1', 'fld 21', 'Field,1')
		select('RecordSelectionJTbl1', '22', 'Field Value,1')
		select('RecordSelectionJTbl1', 'cell:Field Value,1()')
		rightclick('RecordSelectionJTbl1', 'and,1')
		select('TabbedPane', 'zx33xzFLD3')
		click('Insert2')
		select('RecordSelectionJTbl2', 'cell:Field,0()')
		select('RecordSelectionJTbl2', 'fld 31', 'Field,0')
		select('RecordSelectionJTbl2', '31', 'Field Value,0')
		select('TabbedPane', 'Summary')
		select('JTreeTable', 'cell:Boolean op 3  ,2(  )')
		select('JTreeTable', 'cell:Boolean op 3  ,2(  )')
		assert_p('JTreeTable', 'Content', '[[, ,   ,   ,   , , =, ], [, , And  ,   ,   , fld 11, =, 123], [, ,   , Or  ,   , fld 11, =, 321], [, ,   , Or  ,   , fld 11, =, 121], [, ,   ,   ,   , , =, ], [, , And  ,   ,   , fld 21, =, 21], [, ,   , Or  ,   , fld 21, =, 22], [, ,   ,   ,   , , =, ], [, , And  ,   ,   , fld 31, =, 31]]')
		select('JTreeTable', '3219', 'Test Value ,2')
		select('JTreeTable', '12399', 'Test Value ,1')
		select('JTreeTable', '121876', 'Test Value ,3')
		select('JTreeTable', 'fld 12', 'Field Name   ,2')
		select('JTreeTable', 'fld 22', 'Field Name   ,6')
		select('JTreeTable', '219', 'Test Value ,5')
		select('JTreeTable', 'ff', 'Field Name   ,4')
		select('JTreeTable', 'vv', 'Test Value ,4')
		select('JTreeTable', '99', 'Field Name   ,7')
		select('JTreeTable', '99', 'Test Value ,7')
		select('JTreeTable', 'cell:Test Value ,6(22)')
		assert_p('JTreeTable', 'Content', '[[, ,   ,   ,   , , =, ], [, , And  ,   ,   , fld 11, =, 12399], [, ,   , Or  ,   , fld 12, =, 3219], [, ,   , Or  ,   , fld 11, =, 121876], [, ,   ,   ,   , ff, =, vv], [, , And  ,   ,   , fld 21, =, 219], [, ,   , Or  ,   , fld 22, =, 22], [, ,   ,   ,   , 99, =, 99], [, , And  ,   ,   , fld 31, =, 31]]')
		select('TabbedPane', 'zx33xzFLD3')
		assert_p('TabbedPane', 'Content', '[[zx33xzFLD1, zx33xzFLD2, zx33xzFLD3, Summary]]')
		assert_p('RecordSelectionJTbl2', 'Content', '[[, , fld 31, =, 31]]')
		select('TabbedPane', 'zx33xzFLD2')
		assert_p('RecordSelectionJTbl1', 'Content', '[[, , fld 21, =, 219], [Or, , fld 22, =, 22]]')
		select('TabbedPane', 'zx33xzFLD1')
		assert_p('RecordSelectionJTbl', 'Content', '[[, , fld 11, =, 12399], [Or, , fld 12, =, 3219], [Or, , fld 11, =, 121876]]')
		select('RecordSelectionJTbl', '32197', 'Field Value,1')
		select('RecordSelectionJTbl', '1218765', 'Field Value,2')
		select('RecordSelectionJTbl', 'fld 13', 'Field,2')
		select('RecordSelectionJTbl', 'cell:Field,2(fld 13)')
		assert_p('RecordSelectionJTbl', 'Content', '[[, , fld 11, =, 12399], [Or, , fld 12, =, 32197], [Or, , fld 13, =, 1218765]]')
		select('TabbedPane', 'Summary')
		assert_p('JTreeTable', 'Content', '[[, ,   ,   ,   , , =, ], [, , And  ,   ,   , fld 11, =, 12399], [, ,   , Or  ,   , fld 12, =, 32197], [, ,   , Or  ,   , fld 13, =, 1218765], [, ,   ,   ,   , ff, =, vv], [, , And  ,   ,   , fld 21, =, 219], [, ,   , Or  ,   , fld 22, =, 22], [, ,   ,   ,   , 99, =, 99], [, , And  ,   ,   , fld 31, =, 31]]')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
		assert_p('ChildRecordsJTbl', 'Content', '[[, zx33xzFLD1, , , , , ], [, zx33xzFLD2, , ff, vv, , ], [, zx33xzFLD3, , 99, 99, , ]]')

		click('BasicInternalFrameTitlePane$NoFocusButton2')
		select_menu('Record Layouts>>Edit Layout')
		select('RecordList.Record Name_Txt', 'zx33xzFLDg543')

		select('RecordList.Description_Txt', '%')

		assert_p('ChildRecordsJTbl', 'Content', '[[, zx33xzFLD1, , , , , ], [, zx33xzFLD2, , ff, vv, , ], [, zx33xzFLD3, , 99, 99, , ]]')
##		select('ChildRecordsJTbl', '')
		rightclick('ChildRecordsJTbl', 'Field,0')
		select_menu('View Record Selections Tree')
##		select('TabbedPane1', 'Summary')
		assert_p('JTreeTable', 'Content', '[[, ,   ,   ,   , , =, ], [, , And  ,   ,   , fld 11, =, 12399], [, ,   , Or  ,   , fld 12, =, 32197], [, ,   , Or  ,   , fld 13, =, 1218765], [, ,   ,   ,   , ff, =, vv], [, , And  ,   ,   , fld 21, =, 219], [, ,   , Or  ,   , fld 22, =, 22], [, ,   ,   ,   , 99, =, 99], [, , And  ,   ,   , fld 31, =, 31]]')
		select('TabbedPane', 'zx33xzFLD3')
		assert_p('RecordSelectionJTbl2', 'Content', '[[, , fld 31, =, 31]]')
		select('TabbedPane', 'zx33xzFLD2')
		assert_p('RecordSelectionJTbl1', 'Content', '[[, , fld 21, =, 219], [Or, , fld 22, =, 22]]')
		select('TabbedPane', 'zx33xzFLD1')
		assert_p('RecordSelectionJTbl', 'Content', '[[, , fld 11, =, 12399], [Or, , fld 12, =, 32197], [Or, , fld 13, =, 1218765]]')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
	close()