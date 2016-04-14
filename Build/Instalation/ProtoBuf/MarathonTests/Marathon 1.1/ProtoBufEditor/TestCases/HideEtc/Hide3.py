useFixture(default)

def test():
	from Modules import commonBits
	java_recorded_version = '1.6.0_17'

	if window(commonBits.applicationName()):
		select('FileNameTxtFld', commonBits.sampleDir() +  'Ams_LocDownload_20041228.bin')
		click('Edit1')
		select('LinesTbl', 'cell:2|Loc_Nbr,0(5839)')
		rightclick('LinesTbl', '1|Brand_Id,9')
##		select('Table', 'cell:2|Loc_Nbr,0(5839)')
		select_menu('Edit Record')
###		select('Table1', 'cell:2|Loc_Nbr,0(5839)')
		select_menu('Edit>>Show / Hide Fields')
##		click('MetalInternalFrameTitlePane', 210, 10)
		assert_p('Table', 'Content', '[[Brand_Id, true], [Loc_Nbr, true], [Loc_Type, true], [Loc_Name, true], [Loc_Addr_Ln1, true], [Loc_Addr_Ln2, true], [Loc_Addr_Ln3, true], [Loc_Postcode, true], [Loc_State, true], [Loc_Actv_Ind, true]]')
		select('Table', 'cell:Show,0(true)')
		select('Table', 'cell:Show,2(true)')
		select('Table', 'cell:Show,5(true)')
		select('Table', 'cell:Show,6(true)')
		select('Table', 'cell:Show,7(true)')
		select('Table', 'cell:Show,8(true)')
		select('Table', 'cell:Show,9(true)')
		click('Go')
		select_menu('Window>>Ams_LocDownload_20041228.bin>>Record:')
##		click('JTableHeader', 'Ctrl+Button2', 'Data')
##		select('Table', '')
		assert_p('BaseLineAsColumn$LineAsColTbl', 'Content', '[[Loc_Nbr, 2, , 5052, 5052], [Loc_Name, 4, , Eastwood, Eastwood], [Loc_Addr_Ln1, 5, , Marayong Offsite Reserve, Marayong Offsite Reserve]]')
###		zzzz
		select_menu('Edit>>Show / Hide Fields')
		select('Table', 'cell:Show,0(false)')

		select('Table', 'cell:Show,8(false)')
		select('Table', 'cell:Show,9(false)')
		select('Table', 'cell:Show,9(true)')
		click('Go')
		select('BaseLineAsColumn$LineAsColTbl', 'cell:Data,2(Eastwood)')
		assert_p('BaseLineAsColumn$LineAsColTbl', 'Content', '[[Brand_Id, 1, , TAR, TAR], [Loc_Nbr, 2, , 5052, 5052], [Loc_Name, 4, , Eastwood, Eastwood], [Loc_Addr_Ln1, 5, , Marayong Offsite Reserve, Marayong Offsite Reserve], [Loc_State, 9, , NSW, NSW]]')
		select('BaseLineAsColumn$LineAsColTbl', 'cell:Data,2(Eastwood)')
		select_menu('Edit>>Show / Hide Fields')
##		select('Table1', 'cell:Data,2(Eastwood)')
		select('Table', 'cell:Show,9(false)')
		click('Go')
		select_menu('Window>>Ams_LocDownload_20041228.bin>>Record:')
		select('BaseLineAsColumn$LineAsColTbl', 'cell:Data,3(Marayong Offsite Reserve)')
		assert_p('BaseLineAsColumn$LineAsColTbl', 'Content', '[[Brand_Id, 1, , TAR, TAR], [Loc_Nbr, 2, , 5052, 5052], [Loc_Name, 4, , Eastwood, Eastwood], [Loc_Addr_Ln1, 5, , Marayong Offsite Reserve, Marayong Offsite Reserve], [Loc_State, 9, , NSW, NSW], [Loc_Actv_Ind, 10, , A, A]]')
		select('BaseLineAsColumn$LineAsColTbl', 'cell:Data,3(Marayong Offsite Reserve)')
		select_menu('Edit>>Show / Hide Fields')
##		select('Table1', 'cell:Data,3(Marayong Offsite Reserve)')
		select('Table', 'cell:Show,7(false)')
		select('Table', 'cell:Show,6(false)')
		select('Table', 'cell:Show,5(false)')
		click('Go')
		select_menu('Window>>Ams_LocDownload_20041228.bin>>Record:')
		select('BaseLineAsColumn$LineAsColTbl', 'cell:Data,3(Marayong Offsite Reserve)')
		assert_p('BaseLineAsColumn$LineAsColTbl', 'Content', '[[Brand_Id, 1, , TAR, TAR], [Loc_Nbr, 2, , 5052, 5052], [Loc_Name, 4, , Eastwood, Eastwood], [Loc_Addr_Ln1, 5, , Marayong Offsite Reserve, Marayong Offsite Reserve], [Loc_Addr_Ln2, 6, , 11 Melissa Place, 11 Melissa Place], [Loc_Addr_Ln3, 7, , Marayong, Marayong], [Loc_Postcode, 8, , 2148, 2148], [Loc_State, 9, , NSW, NSW], [Loc_Actv_Ind, 10, , A, A]]')
		select('BaseLineAsColumn$LineAsColTbl', 'cell:Data,3(Marayong Offsite Reserve)')
		select_menu('Edit>>Show / Hide Fields')
##		select('Table1', 'cell:Data,3(Marayong Offsite Reserve)')
		select('Table', 'cell:Field,3(Loc_Name)')
		assert_p('Table', 'Content', '[[Brand_Id, true], [Loc_Nbr, true], [Loc_Type, false], [Loc_Name, true], [Loc_Addr_Ln1, true], [Loc_Addr_Ln2, true], [Loc_Addr_Ln3, true], [Loc_Postcode, true], [Loc_State, true], [Loc_Actv_Ind, true]]')
##		select('Table', 'true', 'Show,2')
		select('Table', 'cell:Show,2(true)')
		click('Go')
		select_menu('Window>>Ams_LocDownload_20041228.bin>>Record:')
		select('BaseLineAsColumn$LineAsColTbl', 'cell:Data,5(11 Melissa Place)')
		assert_p('BaseLineAsColumn$LineAsColTbl', 'Content', '[[Brand_Id, 1, , TAR, TAR], [Loc_Nbr, 2, , 5052, 5052], [Loc_Type, 3, , ST, ST], [Loc_Name, 4, , Eastwood, Eastwood], [Loc_Addr_Ln1, 5, , Marayong Offsite Reserve, Marayong Offsite Reserve], [Loc_Addr_Ln2, 6, , 11 Melissa Place, 11 Melissa Place], [Loc_Addr_Ln3, 7, , Marayong, Marayong], [Loc_Postcode, 8, , 2148, 2148], [Loc_State, 9, , NSW, NSW], [Loc_Actv_Ind, 10, , A, A]]')
		select('BaseLineAsColumn$LineAsColTbl', 'cell:Data,5(11 Melissa Place)')
		select_menu('Edit>>Show / Hide Fields')
##		select('Table1', 'cell:Data,5(11 Melissa Place)')
		select('Table', 'cell:Field,3(Loc_Name)')
		assert_p('Table', 'Content', '[[Brand_Id, true], [Loc_Nbr, true], [Loc_Type, true], [Loc_Name, true], [Loc_Addr_Ln1, true], [Loc_Addr_Ln2, true], [Loc_Addr_Ln3, true], [Loc_Postcode, true], [Loc_State, true], [Loc_Actv_Ind, true]]')
		select('Table', 'false', 'Show,0')
		select('Table', 'false', 'Show,2')
		select('Table', 'false', 'Show,5')
		select('Table', 'false', 'Show,6')
##		select('Table', 'cell:Show,6(false)')
		click('Go')
		select_menu('Window>>Ams_LocDownload_20041228.bin>>Record:')
		select('BaseLineAsColumn$LineAsColTbl', 'cell:Data,4(NSW)')
		assert_p('BaseLineAsColumn$LineAsColTbl', 'Content', '[[Loc_Nbr, 2, , 5052, 5052], [Loc_Name, 4, , Eastwood, Eastwood], [Loc_Addr_Ln1, 5, , Marayong Offsite Reserve, Marayong Offsite Reserve], [Loc_Postcode, 8, , 2148, 2148], [Loc_State, 9, , NSW, NSW], [Loc_Actv_Ind, 10, , A, A]]')
		select('BaseLineAsColumn$LineAsColTbl', 'cell:Data,4(NSW)')
		click('Right')
		select('BaseLineAsColumn$LineAsColTbl', 'cell:Data,3(2040)')
		assert_p('BaseLineAsColumn$LineAsColTbl', 'Content', '[[Loc_Nbr, 2, , 5055, 5055], [Loc_Name, 4, , Leichhardt, Leichhardt], [Loc_Addr_Ln1, 5, , Marketown, Marketown], [Loc_Postcode, 8, , 2040, 2040], [Loc_State, 9, , NSW, NSW], [Loc_Actv_Ind, 10, , A, A]]')
		select('BaseLineAsColumn$LineAsColTbl', 'cell:Data,3(2040)')
		click('Right')
		select('BaseLineAsColumn$LineAsColTbl', 'cell:Data,3(2760)')
		assert_p('BaseLineAsColumn$LineAsColTbl', 'Content', '[[Loc_Nbr, 2, , 5060, 5060], [Loc_Name, 4, , St Marys, St Marys], [Loc_Addr_Ln1, 5, , St. Mary\'s, St. Mary\'s], [Loc_Postcode, 8, , 2760, 2760], [Loc_State, 9, , NSW, NSW], [Loc_Actv_Ind, 10, , A, A]]')
		select('BaseLineAsColumn$LineAsColTbl', 'cell:Data,3(2760)')
		select_menu('Edit>>Show / Hide Fields')
##		select('Table1', 'cell:Data,3(2760)')
		select('Table', 'true', 'Show,0')
		select('BaseLineAsColumn$LineAsColTbl', 'cell:Field,4(Loc_Addr_Ln1)')
		assert_p('Table', 'Content', '[[Brand_Id, true], [Loc_Nbr, true], [Loc_Type, false], [Loc_Name, true], [Loc_Addr_Ln1, true], [Loc_Addr_Ln2, false], [Loc_Addr_Ln3, false], [Loc_Postcode, true], [Loc_State, true], [Loc_Actv_Ind, true]]')
		select('Table', 'true', 'Show,2')
		select('Table', 'true', 'Show,5')
		select('Table', 'true', 'Show,6')
##		select('Table', 'cell:Show,6(true)')
		click('Go')
		select_menu('Window>>Ams_LocDownload_20041228.bin>>Record:')
		select('BaseLineAsColumn$LineAsColTbl', 'cell:Data,4(St. Mary\'s)')
		assert_p('BaseLineAsColumn$LineAsColTbl', 'Content', '[[Brand_Id, 1, , TAR, TAR], [Loc_Nbr, 2, , 5060, 5060], [Loc_Type, 3, , ST, ST], [Loc_Name, 4, , St Marys, St Marys], [Loc_Addr_Ln1, 5, , St. Mary\'s, St. Mary\'s], [Loc_Addr_Ln2, 6, , Charles Hackett Drive, Charles Hackett Drive], [Loc_Addr_Ln3, 7, , St Mary\'s, St Mary\'s], [Loc_Postcode, 8, , 2760, 2760], [Loc_State, 9, , NSW, NSW], [Loc_Actv_Ind, 10, , A, A]]')

		select('BaseLineAsColumn$LineAsColTbl', 'cell:Data,4(St. Mary\'s)')
		click('BasicInternalFrameTitlePane$NoFocusButton2')
	close()
