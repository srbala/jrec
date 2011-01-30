useFixture(default)

def test():
	from Modules import commonBits
	java_recorded_version = '1.6.0_03'

	if window('Record Editor'):
		select('FileChooser', commonBits.sampleDir() + 'zzAms_LocDownload_tab.csv')
		click('Layout Wizard')
		select('Delimited Fields', 'true')
##		select('ComboBox', 'Delimited Fields')
##		select('TextField2', 'Wizard - AmsLocation : TabCsv')
		click('Right')
		select('TabbedPane', '')
		assert_p('ComboBox', 'Text', '<Tab>')
		assert_p('ComboBox1', 'Content', '[[<None>, <Default>, ", \', `]]')
		assert_p('CheckBox', 'Text', 'true')
##		assert_p('BmKeyedComboBox', 'Text', '0')
		assert_p('BmKeyedComboBox', 'Text', 'Basic Parser')
		select('CheckBox', 'false')
		select('Table', 'cell:B,3(5853)')
		assert_p('Table', 'Text', '5866', 'B,4')
		select('Table', 'cell:D,5(Bankstown)')
		assert_p('Table', 'Text', 'Bankstown', 'D,5')
		select('Table', 'cell:D,8(Rockdale)')
		assert_p('Table', 'Text', 'Miranda', 'D,9')
		select('Table', 'cell:D,8(Rockdale)')
		select('CheckBox', 'true')
		select('Table', 'cell:Loc_Name,6(Blacktown)')
		assert_p('Table', 'Text', 'Blacktown', 'Loc_Name,6')
		select('Table', 'cell:Loc_Name,6(Blacktown)')
		click('Right')


		#   Save Layout panel
		#   -----------------
		select('TabbedPane', '')
		select('TextField', 'Wizard - AmsLocation : TabCsv')
##		select('BmKeyedComboBox', '7')
		click('Right')

		select('Table', 'cell:4|Loc_Name,4(Bankstown)')
		assert_p('Table', 'Text', 'Miranda', '4|Loc_Name,8')
		select('Table', 'cell:4|Loc_Name,9(Eastwood)')
		assert_p('Table', 'Text', 'St Marys', '4|Loc_Name,11')
		select('Table', 'rows:[11,12,13,14],columns:[4|Loc_Name]')
		select_menu('View>>Column View #{Selected Records#}')
##		select('Table2', 'rows:[11,12,13,14],columns:[4|Loc_Name]')
		select('Table', 'cell:Row 1,4(St. Mary\'s)')
		assert_p('Table', 'Text', 'St Mary\'s', 'Row 1,6')
		select('Table', 'cell:Row 1,1(5060)')
		assert_p('Table', 'Text', 'St Mary\'s', 'Row 1,6')
		select('Table', 'cell:Row 1,1(5060)')
		assert_p('Table', 'Content', '[[TAR, TAR, TAR, TAR], [5060, 5070, 5074, 5078], [ST, ST, ST, ST], [St Marys, Bass Hill, Campbelltown, Warringah Mall], [St. Mary\'s, Bass Hill Plaza, Campbelltown Mall, Frenchs Forest], [Charles Hackett Drive, 753 Hume Highway, 303 Queen Street, Units 2-3], [St Mary\'s, Bass Hill, Campbelltown,  14 Aquatic Drive], [2760, 2197, 2560, Frenchs Forest], [NSW, NSW, NSW, 2086], [A, A, A, NSW]]')
		select('Table', 'cell:Row 1,1(5060)')
		select('Table1', 'cell:Field,1(Loc_Nbr)')
		assert_p('Table1', 'Text', 'Loc_Addr_Ln2', 'Field,5')
		select('Table1', 'cell:Field,1(Loc_Nbr)')
		assert_p('Table1', 'Content', '[[Brand_Id, 1, ], [Loc_Nbr, 2, ], [Loc_Type, 3, ], [Loc_Name, 4, ], [Loc_Addr_Ln1, 5, ], [Loc_Addr_Ln2, 6, ], [Loc_Addr_Ln3, 7, ], [Loc_Postcode, 8, ], [Loc_State, 9, ], [Loc_Actv_Ind, 10, ]]')
		select('Table1', 'cell:Field,1(Loc_Nbr)')
		commonBits.closeWindow(click)
		##click('BasicInternalFrameTitlePane$NoFocusButton2')
		select('Table', 'rows:[11,12,13,14],columns:[4|Loc_Name]')
		select('Table', 'rows:[11,12,13,14],columns:[4|Loc_Name]')
		commonBits.closeWindow(click)
		##click('BasicInternalFrameTitlePane$NoFocusButton2')
		select_menu('Record Layouts>>Edit Layout')
		select('TextField', 'Wizard - AmsLocation : TabCsv%')
		select('TextField1', '%')

#		select('TabbedPane', 'Extras')
#		select('TabbedPane', 'Extras')
#		select('TabbedPane', 'Fields')
#		select('TabbedPane', 'Extras')
#		select('TabbedPane', 'Extras')
#		select('TabbedPane', 'Fields')
		click('Delete3')

		if window('Delete: Wizard - AmsLocation : TabCsv'):
			click('Yes')
		close()

		select('TabbedPane', 'Extras')
		select('TabbedPane', 'Extras')
		select('TabbedPane', 'Fields')
		select('TabbedPane', 'Extras')
		select('TabbedPane', 'Extras')
		select('TabbedPane', 'Fields')
	close()
