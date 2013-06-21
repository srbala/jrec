useFixture(default)

def test():
	from Modules import commonBits
	java_recorded_version = '1.6.0_22'

	if window('Record Editor'):
		select('File_Txt', commonBits.sampleDir() + 'po/TstDupFilter01.po')
		click('Edit1')
##		select('TabbedPane', 'Fuzzy/Blank')
##		select('Table', '')


		select('TabbedPane', 'PO List')

		rightclick('Table', 'Line,0')
		select_menu('Show Duplicate Rows')
		select('PoDuplicateFilter.Remove Blank Duplicate Transalations_Chk', 'false')
		click('Generate Duplicate View')
		select('TabbedPane', 'Duplicates')
		select('TabbedPane', 'Duplicates')
		select('TabbedPane', 'Duplicates')
		click('Duplicates')
		assert_p('Table2', 'Content', '[[, 1], [, 2], [, 3], [, 4], [, 5], [, 6]]')
		assert_p('TextArea6', 'Text', '''---------------------------------------------------------------------------------

Use: Combobox_Entry 
 id:    Panel:  
''')

		assert_p('TextArea7', 'Text', '< (Numeric)')
		assert_p('TextArea8', 'Text', '`!< (Numeric)!`')


		click('Fuzzy/Blank')
		select('TabbedPane', 'Fuzzy/Blank')
		assert_p('PoList.FileDisplay_JTbl1', 'Content', '''[[<None>, , Use: Combobox_Entry 
 id:    Panel:  
Combo- Csv_Quote], [< (Numeric), , Use: Combobox_Entry 
 id:    Panel:  
]]''')
		click('PO List')
		select('TabbedPane', 'PO List')
		assert_p('PoList.FileDisplay_JTbl', 'Content', '''[[<= (Text), `!<= (Text) 1!`, Use: Combobox_Entry 
 id:    Panel:  

 Duplicate (3)], [<All>, `!<All>!`, Use: Combobox_Entry 
 id:    Panel:  
Combo- Layout Selection], [<None>, , Use: Combobox_Entry 
 id:    Panel:  
Combo- Csv_Quote], [< (Numeric), `!< (Numeric)!`, ---------------------------------------------------------------------------------

Use: Combobox_Entry 
 id:    Panel:  
], [< (Numeric), , Use: Combobox_Entry 
 id:    Panel:  
], [<All>, `!<All>!`, Use: Combobox_Entry 
 id:    Panel:  
Combo- Layout Selection], [<None>, `!<None>!`, Use: Combobox_Entry 
 id:    Panel:  
Combo- Csv_Quote], [<= (Text), `!<= (Text)!`, ---------------------------------------------------------------------------------

Use: Combobox_Entry 
 id:    Panel:  
]]''')
##		click('BasicInternalFrameTitlePane$NoFocusButton2')

##		if window(r'Save Changes to file: C:\Users\BruceTst/RecordEditor_HSQL\SampleFiles/po/TstDupFilter01.po'):
##			click('No')
##		close()
	close()
