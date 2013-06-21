useFixture(RecordEditor)

def test():
	from Modules import commonBits
	java_recorded_version = '1.5.0_11'

	if window('Record Editor'):
		select('FileChooser', commonBits.sampleDir() + 'Ams_LocDownload_20041228.txt')
		commonBits.setRecordLayout(select, 'ams Store')

		click(commonBits.fl('Edit') + '1')
		rightclick('Table', '10 - 35|Loc Name,2')
		select_menu(commonBits.fl('Edit Record'))
		click('Find1')
		#click('MetalInternalFrameTitlePane', 203, 17)
		select('TextField', 'West')
		commonBits.find(click)
		select('Table', 'cell:' + commonBits.fl('Data') + ',3(Miranda)')
		select('Table', 'cell:' + commonBits.fl('Data') + ',3(Miranda)')
		assert_p('Table', 'Content', '[[Brand Id, 1, 3, TAR, TAR], [Loc Nbr, 4, 4, 5037, 5037], [Loc Type, 8, 2, ST, ST], [Loc Name, 10, 35, Miranda, Miranda], [Loc Addr Ln1, 45, 40, Westfield Shoppingtown, Westfield Shoppingtown], [Loc Addr Ln2, 85, 40, Cnr. Urunga Pde & The Kingsway, Cnr. Urunga Pde & The Kingsway], [Loc Addr Ln3, 125, 35, Miranda, Miranda], [Loc Postcode, 160, 10, 2228, 2228], [Loc State, 170, 3, NSW, NSW], [Loc Actv Ind, 173, 1, A, A]]')
		select('Table', 'cell:' + commonBits.fl('Data') + ',3(Miranda)')
		commonBits.find(click)
		select('TextField', 'Liverpool')
		commonBits.find(click)
		select('Table', 'cell:' + commonBits.fl('Data') + ',3(Liverpool)')
		assert_p('Table', 'Content', '[[Brand Id, 1, 3, TAR, TAR], [Loc Nbr, 4, 4, 5093, 5093], [Loc Type, 8, 2, ST, ST], [Loc Name, 10, 35, Liverpool, Liverpool], [Loc Addr Ln1, 45, 40, Westfield Phoenix Plaza, Westfield Phoenix Plaza], [Loc Addr Ln2, 85, 40, Northumberland Street, Northumberland Street], [Loc Addr Ln3, 125, 35, Liverpool, Liverpool], [Loc Postcode, 160, 10, 2170, 2170], [Loc State, 170, 3, NSW, NSW], [Loc Actv Ind, 173, 1, A, A]]')
		select('Table', 'cell:' + commonBits.fl('Data') + ',3(Liverpool)')
		##commonBits.find(click)
		select_menu(commonBits.fl('Window') + '>>Ams_LocDownload_20041228.txt>>' + commonBits.fl('Find'))
		select('TextField', 'Eastgarden')

		commonBits.find(click)	
		select('Table', 'cell:' + commonBits.fl('Data') + ',3(Eastgarden)')
		assert_p('Table', 'Content', '[[Brand Id, 1, 3, TAR, TAR], [Loc Nbr, 4, 4, 5095, 5095], [Loc Type, 8, 2, ST, ST], [Loc Name, 10, 35, Eastgarden, Eastgarden], [Loc Addr Ln1, 45, 40, Westfield Shoppingtown Eastgardens, Westfield Shoppingtown Eastgardens], [Loc Addr Ln2, 85, 40, 152 Bunnerong Road, 152 Bunnerong Road], [Loc Addr Ln3, 125, 35, Eastgardens, Eastgardens], [Loc Postcode, 160, 10, 2036, 2036], [Loc State, 170, 3, NSW, NSW], [Loc Actv Ind, 173, 1, A, A]]')

		assert_p('Table', 'Content', '[[Brand Id, 1, 3, TAR, TAR], [Loc Nbr, 4, 4, 5095, 5095], [Loc Type, 8, 2, ST, ST], [Loc Name, 10, 35, Eastgarden, Eastgarden], [Loc Addr Ln1, 45, 40, Westfield Shoppingtown Eastgardens, Westfield Shoppingtown Eastgardens], [Loc Addr Ln2, 85, 40, 152 Bunnerong Road, 152 Bunnerong Road], [Loc Addr Ln3, 125, 35, Eastgardens, Eastgardens], [Loc Postcode, 160, 10, 2036, 2036], [Loc State, 170, 3, NSW, NSW], [Loc Actv Ind, 173, 1, A, A]]')

		commonBits.find(click)	
		select('Table', 'cell:' + commonBits.fl('Data') + ',3(Eastgarden)')
		commonBits.find(click)
		select('Table', 'cell:' + commonBits.fl('Data') + ',3(Liverpool)')
		#assert_p('Table', 'Content', '[[Brand Id, 1, 3, TAR, TAR], [Loc Nbr, 4, 4, 5093, 5093], [Loc Type, 8, 2, ST, ST], [Loc Name, 10, 35, Liverpool, Liverpool], [Loc Addr Ln1, 45, 40, Westfield Phoenix Plaza, Westfield Phoenix Plaza], [Loc Addr Ln2, 85, 40, Northumberland Street, Northumberland Street], [Loc Addr Ln3, 125, 35, Liverpool, Liverpool], [Loc Postcode, 160, 10, 2170, 2170], [Loc State, 170, 3, NSW, NSW], [Loc Actv Ind, 173, 1, A, A]]')
		select('Table', 'cell:' + commonBits.fl('Data') + ',3(Liverpool)')
		commonBits.find(click)
		select('Table', 'cell:' + commonBits.fl('Data') + ',3(Miranda)')
		#assert_p('Table', 'Content', '[[Brand Id, 1, 3, TAR, TAR], [Loc Nbr, 4, 4, 5037, 5037], [Loc Type, 8, 2, ST, ST], [Loc Name, 10, 35, Miranda, Miranda], [Loc Addr Ln1, 45, 40, Westfield Shoppingtown, Westfield Shoppingtown], [Loc Addr Ln2, 85, 40, Cnr. Urunga Pde & The Kingsway, Cnr. Urunga Pde & The Kingsway], [Loc Addr Ln3, 125, 35, Miranda, Miranda], [Loc Postcode, 160, 10, 2228, 2228], [Loc State, 170, 3, NSW, NSW], [Loc Actv Ind, 173, 1, A, A]]')
		select('Table', 'cell:' + commonBits.fl('Data') + ',3(Miranda)')
		select('ComboBox', 'Loc Addr Ln1')
		commonBits.find(click)
		#assert_p('Table', 'Content', '[[Brand Id, 1, 3, TAR, TAR], [Loc Nbr, 4, 4, 5093, 5093], [Loc Type, 8, 2, ST, ST], [Loc Name, 10, 35, Liverpool, Liverpool], [Loc Addr Ln1, 45, 40, Westfield Phoenix Plaza, Westfield Phoenix Plaza], [Loc Addr Ln2, 85, 40, Northumberland Street, Northumberland Street], [Loc Addr Ln3, 125, 35, Liverpool, Liverpool], [Loc Postcode, 160, 10, 2170, 2170], [Loc State, 170, 3, NSW, NSW], [Loc Actv Ind, 173, 1, A, A]]')
		commonBits.find(click)
		select('Table', 'cell:' + commonBits.fl('Data') + ',5(152 Bunnerong Road)')
		#assert_p('Table', 'Content', '[[Brand Id, 1, 3, TAR, TAR], [Loc Nbr, 4, 4, 5095, 5095], [Loc Type, 8, 2, ST, ST], [Loc Name, 10, 35, Eastgarden, Eastgarden], [Loc Addr Ln1, 45, 40, Westfield Shoppingtown Eastgardens, Westfield Shoppingtown Eastgardens], [Loc Addr Ln2, 85, 40, 152 Bunnerong Road, 152 Bunnerong Road], [Loc Addr Ln3, 125, 35, Eastgardens, Eastgardens], [Loc Postcode, 160, 10, 2036, 2036], [Loc State, 170, 3, NSW, NSW], [Loc Actv Ind, 173, 1, A, A]]')
		select('Table', 'cell:' + commonBits.fl('Data') + ',5(152 Bunnerong Road)')
		commonBits.find(click)

		if window(''):
			click('No')
		close()

		select('TextField', 'nsw')
		commonBits.find(click)
		select('Table', 'cell:' + commonBits.fl('Data') + ',3(State  Warehouse NSW)')
##		assert_p('Table', 'Content', '[[Brand Id, 1, 3, TAR, TAR], [Loc Nbr, 4, 4, 5954, 5954], [Loc Type, 8, 2, DC, DC], [Loc Name, 10, 35, State  Warehouse NSW, State  Warehouse NSW], [Loc Addr Ln1, 45, 40, Target State Warehouse NSW (Westgate), Target State Warehouse NSW (Westgate)], [Loc Addr Ln2, 85, 40, Warehouse D Murtha Street, Warehouse D Murtha Street], [Loc Addr Ln3, 125, 35, Arndell Park, Arndell Park], [Loc Postcode, 160, 10, 2148, 2148], [Loc State, 170, 3, NSW, NSW], [Loc Actv Ind, 173, 1, A, A]]')
		select('Table', 'cell:' + commonBits.fl('Data') + ',3(State  Warehouse NSW)')
		select('ComboBox1', ' = ')
		commonBits.find(click)
		select('Table', 'cell:' + commonBits.fl('Data') + ',4(Shopping Centre)')
##		click('BasicInternalFrameTitlePane$NoFocusButton5')
		commonBits.closeWindow(click)
		##click('BasicInternalFrameTitlePane$NoFocusButton2')
##commonBits.closeWindow(click)
		##click('BasicInternalFrameTitlePane$NoFocusButton2')
	close()
