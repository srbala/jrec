useFixture(RecordEditor)

def test():
	from Modules import commonBits
	java_recorded_version = '1.6.0_03'

	if window('Record Editor'):
		select('FileChooser', commonBits.sampleDir() + 'zAms_LocDownload_20041228.csv')
		commonBits.setRecordLayout(select, 'Generic CSV - enter details')
		commonBits.doEdit(click)


		if window(''):
#			select('Table', '')
			select('CheckBox', 'false')
			assert_p('Table', 'Text', '5839', 'B,1')
			select('Table', 'cell:C,0(Loc_Type)')
			assert_p('Table', 'Text', 'DC', 'C,1')
			select('Table', 'cell:D,2(VIC West Ad Support)')
			assert_p('Table', 'Text', 'WA Ad Support', 'D,4')
			select('Table', 'cell:D,2(VIC West Ad Support)')
			select('CheckBox', 'true')
#			select('Table', '')
			assert_p('Table', 'Text', '5839', 'Loc_Nbr,0')
			select('Table', 'cell:Loc_Name,1(VIC West Ad Support)')
			assert_p('Table', 'Text', 'VIC West Ad Support', 'Loc_Name,1')
			select('Table', 'cell:Loc_Name,1(VIC West Ad Support)')
			commonBits.doSleep()

			click(commonBits.fl('Go'))
			commonBits.doSleep()

		close()

		commonBits.doSleep()

		commonBits.doSleep()


		select('Table', 'cell:4|Loc_Name,0(DC - Taras Ave)')
		assert_p('Table', 'Text', 'DC - Taras Ave', '4|Loc_Name,0')
		select('Table', 'cell:4|Loc_Name,4(Bankstown)')
		assert_p('Table', 'Text', 'Bankstown', '4|Loc_Name,4')
		select('Table', 'cell:4|Loc_Name,6(Blacktown)')
		assert_p('Table', 'Text', 'Rockdale', '4|Loc_Name,7')
		select('Table', 'cell:4|Loc_Name,2(NSW North Sydney Ad Support)')
		rightclick('Table', '3|Loc_Type,2')
		select_menu( commonBits.fl('Edit Record'))
#		select('Table1', 'cell:4|Loc_Name,2(NSW North Sydney Ad Support)')
		select('Table', 'cell:' + commonBits.fl('Data') + ',2(DC)')
		assert_p('Table', 'Content', '[[Brand_Id, 1, , TAR, TAR], [Loc_Nbr, 2, , 5853, 5853], [Loc_Type, 3, , DC, DC], [Loc_Name, 4, , NSW North Sydney Ad Support, NSW North Sydney Ad Support], [Loc_Addr_Ln1, 5, , , ], [Loc_Addr_Ln2, 6, , , ], [Loc_Addr_Ln3, 7, , , ], [Loc_Postcode, 8, , , ], [Loc_State, 9, , , ], [Loc_Actv_Ind, 10, , A, A], [K, 11, , , ]]')
		select('Table', 'cell:' + commonBits.fl('Data') + ',3(NSW North Sydney Ad Support)')
		assert_p('Table', 'Text', 'NSW North Sydney Ad Support', commonBits.fl('Data') + ',3')
		select('Table', 'cell:' + commonBits.fl('Data') + ',3(NSW North Sydney Ad Support)')
		click('Right')
		click('Right')
		select('Table', 'cell:' + commonBits.fl('Data') + ',6( 39-41 Allingham Street)')
		assert_p('Table', 'Text', ' 39-41 Allingham Street', commonBits.fl('Data') + ',6')
		select('Table', 'cell:' + commonBits.fl('Data') + ',4(Bankstown)')
		assert_p('Table', 'Text', 'Bankstown', commonBits.fl('Data') + ',4')
		select('Table', 'cell:' + commonBits.fl('Data') + ',1(5015)')
		assert_p('Table', 'Content', '[[Brand_Id, 1, , TAR, TAR], [Loc_Nbr, 2, , 5015, 5015], [Loc_Type, 3, , ST, ST], [Loc_Name, 4, , Bankstown, Bankstown], [Loc_Addr_Ln1, 5, , Bankstown, Bankstown], [Loc_Addr_Ln2, 6, , Unit 2, Unit 2], [Loc_Addr_Ln3, 7, ,  39-41 Allingham Street,  39-41 Allingham Street], [Loc_Postcode, 8, , Condell Park, Condell Park], [Loc_State, 9, , 2200, 2200], [Loc_Actv_Ind, 10, , NSW, NSW], [K, 11, , A, A]]')
	close()
