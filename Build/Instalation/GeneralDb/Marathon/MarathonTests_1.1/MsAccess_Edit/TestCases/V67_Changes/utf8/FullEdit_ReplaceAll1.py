useFixture(default)

def test():
	from Modules import commonBits
	java_recorded_version = '1.5.0_11'

	if window('Record Editor'):
		select('FileChooser', commonBits.sampleDir() + 'utf8a_Ams_LocDownload_20041228.txt')
		commonBits.setRecordLayout(select, 'utf8_ams Store')

		click('Edit1')
		click('Find1')
		#click('MetalInternalFrameTitlePane', 199, 13)
		select('TextField', 'West')
		select('TextField1', 'West_')
		select('ComboBox', 'Loc Addr Ln1')
		click('Replace All')
		commonBits.closeWindow(click)
		##click('BasicInternalFrameTitlePane$NoFocusButton2')
		select('Table', 'cell:45 - 40|Loc Addr Ln1,0()')
		rightclick('Table', '4 - 4|Loc Nbr,0')
		select_menu('Edit Record')
		click('Find1')
		#click('MetalInternalFrameTitlePane', 211, 10)
		select('TextField', 'West_')
		##click('Find1')
		commonBits.find(click)

		select('Table', 'cell:Data,4(West_field Shoppingtown)')
		select('Table', 'cell:Data,4(West_field Shoppingtown)')
		assert_p('Table', 'Text', 'Cnr. Urunga Pde & The Kingsway', 'Data,5')
		
		select('Table', 'cell:Data,4(West_field Shoppingtown)')
		select('Table', 'cell:Data,5(Cnr. Urunga Pde & The Kingsway)')
##		assert_p('Table', 'Content', '[[Brand Id, 1, 3, TAR, TAR], [Loc Nbr, 4, 4, 5037, 5037], [Loc Type, 8, 2, ST, ST], [Loc Name, 10, 35, Miranda, Miranda], [Loc Addr Ln1, 45, 40, West_field Shoppingtown, West_field Shoppingtown], [Loc Addr Ln2, 85, 40, Cnr. Urunga Pde & The Kingsway, Cnr. Urunga Pde & The Kingsway], [Loc Addr Ln3, 125, 35, Miranda, Miranda], [Loc Postcode, 160, 10, 2228, 2228], [Loc State, 170, 3, NSW, NSW], [Loc Actv Ind, 173, 1, A, A]]')
		if commonBits.isMissingCol():
			assert_p('Table', 'Content', '[[Brand Id, 1, 3, TAR, TAR], [Loc Nbr, 4, 4, 5037, 5037], [Loc Type, 8, 2, ST, ST], [Loc Name, 10, 35, Miranda, Miranda], [Loc Addr Ln1, 45, 40, West_field Shoppingtown, West_field Shoppingtown], [Loc Addr Ln2, 85, 40, Cnr. Urunga Pde & The Kingsway, Cnr. Urunga Pde & The Kingsway], [Loc Addr Ln3, 125, 35, Miranda, Miranda], [Loc Postcode, 160, 10, 2228, 2228], [Loc State, 170, 3, NSW, NSW]]')
		else:
			assert_p('Table', 'Content', '[[Brand Id, 1, 3, TAR, TAR], [Loc Nbr, 4, 4, 5037, 5037], [Loc Type, 8, 2, ST, ST], [Loc Name, 10, 35, Miranda, Miranda], [Loc Addr Ln1, 45, 40, West_field Shoppingtown, West_field Shoppingtown], [Loc Addr Ln2, 85, 40, Cnr. Urunga Pde & The Kingsway, Cnr. Urunga Pde & The Kingsway], [Loc Addr Ln3, 125, 35, Miranda, Miranda], [Loc Postcode, 160, 10, 2228, 2228], [Loc State, 170, 3, NSW, NSW], [Loc Actv Ind, 173, 1, A, A]]')
##		assert_p('Table', 'Content', '[[Brand Id, 1, 3, TAR, TAR], [Loc Nbr, 4, 4, 5037, 5037], [Loc Type, 8, 2, ST, ST], [Loc Name, 10, 35, Miranda, Miranda], [Loc Addr Ln1, 45, 40, West_field Shoppingtown, West_field Shoppingtown], [Loc Addr Ln2, 85, 40, Cnr. Urunga Pde & The Kingsway, Cnr. Urunga Pde & The Kingsway], [Loc Addr Ln3, 125, 35, Miranda, Miranda], [Loc Postcode, 160, 10, 2228, 2228], [Loc State, 170, 3, NSW, NSW], [Loc Actv Ind, 173, 1, A, A]]')
		select('Table', 'cell:Data,5(Cnr. Urunga Pde & The Kingsway)')
		click('Find1')
		select('TextField', 'West_')
		##click('Find1')
		commonBits.find(click)

		select('Table', 'cell:Data,4(West_field Phoenix Plaza)')
		assert_p('Table', 'Text', 'Northumberland Street', 'Data,5')
		select('Table', 'cell:Data,5(Northumberland Street)')
##		assert_p('Table', 'Content', '[[Brand Id, 1, 3, TAR, TAR], [Loc Nbr, 4, 4, 5093, 5093], [Loc Type, 8, 2, ST, ST], [Loc Name, 10, 35, Liverpool, Liverpool], [Loc Addr Ln1, 45, 40, West_field Phoenix Plaza, West_field Phoenix Plaza], [Loc Addr Ln2, 85, 40, Northumberland Street, Northumberland Street], [Loc Addr Ln3, 125, 35, Liverpool, Liverpool], [Loc Postcode, 160, 10, 2170, 2170], [Loc State, 170, 3, NSW, NSW], [Loc Actv Ind, 173, 1, A, A]]')
		if commonBits.isMissingCol():
			assert_p('Table', 'Content', '[[Brand Id, 1, 3, TAR, TAR], [Loc Nbr, 4, 4, 5093, 5093], [Loc Type, 8, 2, ST, ST], [Loc Name, 10, 35, Liverpool, Liverpool], [Loc Addr Ln1, 45, 40, West_field Phoenix Plaza, West_field Phoenix Plaza], [Loc Addr Ln2, 85, 40, Northumberland Street, Northumberland Street], [Loc Addr Ln3, 125, 35, Liverpool, Liverpool], [Loc Postcode, 160, 10, 2170, 2170], [Loc State, 170, 3, NSW, NSW]]')
		else:
			assert_p('Table', 'Content', '[[Brand Id, 1, 3, TAR, TAR], [Loc Nbr, 4, 4, 5093, 5093], [Loc Type, 8, 2, ST, ST], [Loc Name, 10, 35, Liverpool, Liverpool], [Loc Addr Ln1, 45, 40, West_field Phoenix Plaza, West_field Phoenix Plaza], [Loc Addr Ln2, 85, 40, Northumberland Street, Northumberland Street], [Loc Addr Ln3, 125, 35, Liverpool, Liverpool], [Loc Postcode, 160, 10, 2170, 2170], [Loc State, 170, 3, NSW, NSW], [Loc Actv Ind, 173, 1, A, A]]')
##		assert_p('Table', 'Content', '[[Brand Id, 1, 3, TAR, TAR], [Loc Nbr, 4, 4, 5093, 5093], [Loc Type, 8, 2, ST, ST], [Loc Name, 10, 35, Liverpool, Liverpool], [Loc Addr Ln1, 45, 40, West_field Phoenix Plaza, West_field Phoenix Plaza], [Loc Addr Ln2, 85, 40, Northumberland Street, Northumberland Street], [Loc Addr Ln3, 125, 35, Liverpool, Liverpool], [Loc Postcode, 160, 10, 2170, 2170], [Loc State, 170, 3, NSW, NSW], [Loc Actv Ind, 173, 1, A, A]]')
		select('Table', 'cell:Data,5(Northumberland Street)')
		click('Find1')
		select('TextField', 'West_')
		##click('Find1')
		commonBits.find(click)

		select('Table', 'cell:Data,4(West_field Shoppingtown Eastgardens)')
		assert_p('Table', 'Text', 'cell:Data,4(West_field Shoppingtown Eastgardens)')
		select('Table', 'cell:Data,5(152 Bunnerong Road)')
##		assert_p('Table', 'Content', '[[Brand Id, 1, 3, TAR, TAR], [Loc Nbr, 4, 4, 5095, 5095], [Loc Type, 8, 2, ST, ST], [Loc Name, 10, 35, Eastgarden, Eastgarden], [Loc Addr Ln1, 45, 40, West_field Shoppingtown Eastgardens, West_field Shoppingtown Eastgardens], [Loc Addr Ln2, 85, 40, 152 Bunnerong Road, 152 Bunnerong Road], [Loc Addr Ln3, 125, 35, Eastgardens, Eastgardens], [Loc Postcode, 160, 10, 2036, 2036], [Loc State, 170, 3, NSW, NSW], [Loc Actv Ind, 173, 1, A, A]]')
		if commonBits.isMissingCol():
			assert_p('Table', 'Content', '[[Brand Id, 1, 3, TAR, TAR], [Loc Nbr, 4, 4, 5095, 5095], [Loc Type, 8, 2, ST, ST], [Loc Name, 10, 35, Eastgarden, Eastgarden], [Loc Addr Ln1, 45, 40, West_field Shoppingtown Eastgardens, West_field Shoppingtown Eastgardens], [Loc Addr Ln2, 85, 40, 152 Bunnerong Road, 152 Bunnerong Road], [Loc Addr Ln3, 125, 35, Eastgardens, Eastgardens], [Loc Postcode, 160, 10, 2036, 2036], [Loc State, 170, 3, NSW, NSW]]')
		else:
			assert_p('Table', 'Content', '[[Brand Id, 1, 3, TAR, TAR], [Loc Nbr, 4, 4, 5095, 5095], [Loc Type, 8, 2, ST, ST], [Loc Name, 10, 35, Eastgarden, Eastgarden], [Loc Addr Ln1, 45, 40, West_field Shoppingtown Eastgardens, West_field Shoppingtown Eastgardens], [Loc Addr Ln2, 85, 40, 152 Bunnerong Road, 152 Bunnerong Road], [Loc Addr Ln3, 125, 35, Eastgardens, Eastgardens], [Loc Postcode, 160, 10, 2036, 2036], [Loc State, 170, 3, NSW, NSW], [Loc Actv Ind, 173, 1, A, A]]')
##		assert_p('Table', 'Content', '[[Brand Id, 1, 3, TAR, TAR], [Loc Nbr, 4, 4, 5095, 5095], [Loc Type, 8, 2, ST, ST], [Loc Name, 10, 35, Eastgarden, Eastgarden], [Loc Addr Ln1, 45, 40, West_field Shoppingtown Eastgardens, West_field Shoppingtown Eastgardens], [Loc Addr Ln2, 85, 40, 152 Bunnerong Road, 152 Bunnerong Road], [Loc Addr Ln3, 125, 35, Eastgardens, Eastgardens], [Loc Postcode, 160, 10, 2036, 2036], [Loc State, 170, 3, NSW, NSW], [Loc Actv Ind, 173, 1, A, A]]')
		select('Table', 'cell:Data,5(152 Bunnerong Road)')
		click('Find1')
		select('TextField', 'West_')
		##click('Find1')
		commonBits.find(click)

		select('Table', 'cell:Data,4(West_field Shopping Centre)')
		assert_p('Table', 'Text', 'George Street', 'Data,5')
		select('Table', 'cell:Data,6(Hornsby)')
##		assert_p('Table', 'Content', '[[Brand Id, 1, 3, TAR, TAR], [Loc Nbr, 4, 4, 5169, 5169], [Loc Type, 8, 2, ST, ST], [Loc Name, 10, 35, Hornsby, Hornsby], [Loc Addr Ln1, 45, 40, West_field Shopping Centre, West_field Shopping Centre], [Loc Addr Ln2, 85, 40, George Street, George Street], [Loc Addr Ln3, 125, 35, Hornsby, Hornsby], [Loc Postcode, 160, 10, 2077, 2077], [Loc State, 170, 3, NSW, NSW], [Loc Actv Ind, 173, 1, A, A]]')
		if commonBits.isMissingCol():
			assert_p('Table', 'Content', '[[Brand Id, 1, 3, TAR, TAR], [Loc Nbr, 4, 4, 5169, 5169], [Loc Type, 8, 2, ST, ST], [Loc Name, 10, 35, Hornsby, Hornsby], [Loc Addr Ln1, 45, 40, West_field Shopping Centre, West_field Shopping Centre], [Loc Addr Ln2, 85, 40, George Street, George Street], [Loc Addr Ln3, 125, 35, Hornsby, Hornsby], [Loc Postcode, 160, 10, 2077, 2077], [Loc State, 170, 3, NSW, NSW]]')
		else:
			assert_p('Table', 'Content', '[[Brand Id, 1, 3, TAR, TAR], [Loc Nbr, 4, 4, 5169, 5169], [Loc Type, 8, 2, ST, ST], [Loc Name, 10, 35, Hornsby, Hornsby], [Loc Addr Ln1, 45, 40, West_field Shopping Centre, West_field Shopping Centre], [Loc Addr Ln2, 85, 40, George Street, George Street], [Loc Addr Ln3, 125, 35, Hornsby, Hornsby], [Loc Postcode, 160, 10, 2077, 2077], [Loc State, 170, 3, NSW, NSW], [Loc Actv Ind, 173, 1, A, A]]')
##		assert_p('Table', 'Content', '[[Brand Id, 1, 3, TAR, TAR], [Loc Nbr, 4, 4, 5169, 5169], [Loc Type, 8, 2, ST, ST], [Loc Name, 10, 35, Hornsby, Hornsby], [Loc Addr Ln1, 45, 40, West_field Shopping Centre, West_field Shopping Centre], [Loc Addr Ln2, 85, 40, George Street, George Street], [Loc Addr Ln3, 125, 35, Hornsby, Hornsby], [Loc Postcode, 160, 10, 2077, 2077], [Loc State, 170, 3, NSW, NSW], [Loc Actv Ind, 173, 1, A, A]]')
		select('Table', 'cell:Data,6(Hornsby)')
		click('Find1')
		select('TextField', 'West_')
		##click('Find1')
		commonBits.find(click)

		select('Table', 'cell:Data,4(West_ Point Shopping Ctr)')
		assert_p('Table', 'Text', 'cell:Data,4(West_ Point Shopping Ctr)')
		select('Table', 'cell:Data,5(Balmoral Street)')
##		assert_p('Table', 'Content', '[[Brand Id, 1, 3, TAR, TAR], [Loc Nbr, 4, 4, 5178, 5178], [Loc Type, 8, 2, ST, ST], [Loc Name, 10, 35, Blacktown - Not Yet Open, Blacktown - Not Yet Open], [Loc Addr Ln1, 45, 40, West_ Point Shopping Ctr, West_ Point Shopping Ctr], [Loc Addr Ln2, 85, 40, Balmoral Street, Balmoral Street], [Loc Addr Ln3, 125, 35, Blacktown, Blacktown], [Loc Postcode, 160, 10, 2134, 2134], [Loc State, 170, 3, NSW, NSW], [Loc Actv Ind, 173, 1, A, A]]')
		if commonBits.isMissingCol():
			assert_p('Table', 'Content', '[[Brand Id, 1, 3, TAR, TAR], [Loc Nbr, 4, 4, 5178, 5178], [Loc Type, 8, 2, ST, ST], [Loc Name, 10, 35, Blacktown - Not Yet Open, Blacktown - Not Yet Open], [Loc Addr Ln1, 45, 40, West_ Point Shopping Ctr, West_ Point Shopping Ctr], [Loc Addr Ln2, 85, 40, Balmoral Street, Balmoral Street], [Loc Addr Ln3, 125, 35, Blacktown, Blacktown], [Loc Postcode, 160, 10, 2134, 2134], [Loc State, 170, 3, NSW, NSW]]')
		else:
			assert_p('Table', 'Content', '[[Brand Id, 1, 3, TAR, TAR], [Loc Nbr, 4, 4, 5178, 5178], [Loc Type, 8, 2, ST, ST], [Loc Name, 10, 35, Blacktown - Not Yet Open, Blacktown - Not Yet Open], [Loc Addr Ln1, 45, 40, West_ Point Shopping Ctr, West_ Point Shopping Ctr], [Loc Addr Ln2, 85, 40, Balmoral Street, Balmoral Street], [Loc Addr Ln3, 125, 35, Blacktown, Blacktown], [Loc Postcode, 160, 10, 2134, 2134], [Loc State, 170, 3, NSW, NSW], [Loc Actv Ind, 173, 1, A, A]]')
##		assert_p('Table', 'Content', '[[Brand Id, 1, 3, TAR, TAR], [Loc Nbr, 4, 4, 5178, 5178], [Loc Type, 8, 2, ST, ST], [Loc Name, 10, 35, Blacktown - Not Yet Open, Blacktown - Not Yet Open], [Loc Addr Ln1, 45, 40, West_ Point Shopping Ctr, West_ Point Shopping Ctr], [Loc Addr Ln2, 85, 40, Balmoral Street, Balmoral Street], [Loc Addr Ln3, 125, 35, Blacktown, Blacktown], [Loc Postcode, 160, 10, 2134, 2134], [Loc State, 170, 3, NSW, NSW], [Loc Actv Ind, 173, 1, A, A]]')
		select('Table', 'cell:Data,5(Balmoral Street)')
		click('Find1')
		select('TextField', 'West_')
		##click('Find1')
		commonBits.find(click)

		select('Table', 'cell:Data,4(West_field Shoppingtown)')
		assert_p('Table', 'Text', 'cell:Data,4(West_field Shoppingtown)')
		select('Table', 'cell:Data,5(Matthews Avenue)')
##		assert_p('Table', 'Content', '[[Brand Id, 1, 3, TAR, TAR], [Loc Nbr, 4, 4, 5168, 5168], [Loc Type, 8, 2, ST, ST], [Loc Name, 10, 35, Airport West, Airport West], [Loc Addr Ln1, 45, 40, West_field Shoppingtown, West_field Shoppingtown], [Loc Addr Ln2, 85, 40, Matthews Avenue, Matthews Avenue], [Loc Addr Ln3, 125, 35, Airport West, Airport West], [Loc Postcode, 160, 10, 3042, 3042], [Loc State, 170, 3, VIC, VIC], [Loc Actv Ind, 173, 1, A, A]]')
		if commonBits.isMissingCol():
			assert_p('Table', 'Content', '[[Brand Id, 1, 3, TAR, TAR], [Loc Nbr, 4, 4, 5168, 5168], [Loc Type, 8, 2, ST, ST], [Loc Name, 10, 35, Airport West, Airport West], [Loc Addr Ln1, 45, 40, West_field Shoppingtown, West_field Shoppingtown], [Loc Addr Ln2, 85, 40, Matthews Avenue, Matthews Avenue], [Loc Addr Ln3, 125, 35, Airport West, Airport West], [Loc Postcode, 160, 10, 3042, 3042], [Loc State, 170, 3, VIC, VIC]]')
		else:
			assert_p('Table', 'Content', '[[Brand Id, 1, 3, TAR, TAR], [Loc Nbr, 4, 4, 5168, 5168], [Loc Type, 8, 2, ST, ST], [Loc Name, 10, 35, Airport West, Airport West], [Loc Addr Ln1, 45, 40, West_field Shoppingtown, West_field Shoppingtown], [Loc Addr Ln2, 85, 40, Matthews Avenue, Matthews Avenue], [Loc Addr Ln3, 125, 35, Airport West, Airport West], [Loc Postcode, 160, 10, 3042, 3042], [Loc State, 170, 3, VIC, VIC], [Loc Actv Ind, 173, 1, A, A]]')
##		assert_p('Table', 'Content', '[[Brand Id, 1, 3, TAR, TAR], [Loc Nbr, 4, 4, 5168, 5168], [Loc Type, 8, 2, ST, ST], [Loc Name, 10, 35, Airport West, Airport West], [Loc Addr Ln1, 45, 40, West_field Shoppingtown, West_field Shoppingtown], [Loc Addr Ln2, 85, 40, Matthews Avenue, Matthews Avenue], [Loc Addr Ln3, 125, 35, Airport West, Airport West], [Loc Postcode, 160, 10, 3042, 3042], [Loc State, 170, 3, VIC, VIC], [Loc Actv Ind, 173, 1, A, A]]')
		select('Table', 'cell:Data,5(Matthews Avenue)')

		click('Find1')
		select('TextField', 'West_')
		select('ComboBox2', 'Backward')
		assert_p('ComboBox2', 'Text', 'Backward')

		##click('Find1')
		commonBits.find(click)

		select('Table', 'cell:Data,4(West_ Point Shopping Ctr)')
		assert_p('Table', 'Text', 'cell:Data,4(West_ Point Shopping Ctr)')
		select('Table', 'cell:Data,5(Balmoral Street)')

##		assert_p('Table', 'Content', '[[Brand Id, 1, 3, TAR, TAR], [Loc Nbr, 4, 4, 5178, 5178], [Loc Type, 8, 2, ST, ST], [Loc Name, 10, 35, Blacktown - Not Yet Open, Blacktown - Not Yet Open], [Loc Addr Ln1, 45, 40, West_ Point Shopping Ctr, West_ Point Shopping Ctr], [Loc Addr Ln2, 85, 40, Balmoral Street, Balmoral Street], [Loc Addr Ln3, 125, 35, Blacktown, Blacktown], [Loc Postcode, 160, 10, 2134, 2134], [Loc State, 170, 3, NSW, NSW], [Loc Actv Ind, 173, 1, A, A]]')
		if commonBits.isMissingCol():
			assert_p('Table', 'Content', '[[Brand Id, 1, 3, TAR, TAR], [Loc Nbr, 4, 4, 5178, 5178], [Loc Type, 8, 2, ST, ST], [Loc Name, 10, 35, Blacktown - Not Yet Open, Blacktown - Not Yet Open], [Loc Addr Ln1, 45, 40, West_ Point Shopping Ctr, West_ Point Shopping Ctr], [Loc Addr Ln2, 85, 40, Balmoral Street, Balmoral Street], [Loc Addr Ln3, 125, 35, Blacktown, Blacktown], [Loc Postcode, 160, 10, 2134, 2134], [Loc State, 170, 3, NSW, NSW]]')
		else:
			assert_p('Table', 'Content', '[[Brand Id, 1, 3, TAR, TAR], [Loc Nbr, 4, 4, 5178, 5178], [Loc Type, 8, 2, ST, ST], [Loc Name, 10, 35, Blacktown - Not Yet Open, Blacktown - Not Yet Open], [Loc Addr Ln1, 45, 40, West_ Point Shopping Ctr, West_ Point Shopping Ctr], [Loc Addr Ln2, 85, 40, Balmoral Street, Balmoral Street], [Loc Addr Ln3, 125, 35, Blacktown, Blacktown], [Loc Postcode, 160, 10, 2134, 2134], [Loc State, 170, 3, NSW, NSW], [Loc Actv Ind, 173, 1, A, A]]')

		select('Table', 'cell:Data,4(West_ Point Shopping Ctr)')
		click('Find1')
		select('TextField', 'West_')
		##click('Find1')
		commonBits.find(click)


		select('Table', 'cell:Data,4(West_field Shopping Centre)')
		assert_p('Table', 'Text', 'cell:Data,4(West_field Shopping Centre)')
		select('Table', 'cell:Data,5(George Street)')

##		assert_p('Table', 'Content', '[[Brand Id, 1, 3, TAR, TAR], [Loc Nbr, 4, 4, 5169, 5169], [Loc Type, 8, 2, ST, ST], [Loc Name, 10, 35, Hornsby, Hornsby], [Loc Addr Ln1, 45, 40, West_field Shopping Centre, West_field Shopping Centre], [Loc Addr Ln2, 85, 40, George Street, George Street], [Loc Addr Ln3, 125, 35, Hornsby, Hornsby], [Loc Postcode, 160, 10, 2077, 2077], [Loc State, 170, 3, NSW, NSW], [Loc Actv Ind, 173, 1, A, A]]')
		if commonBits.isMissingCol():
			assert_p('Table', 'Content', '[[Brand Id, 1, 3, TAR, TAR], [Loc Nbr, 4, 4, 5169, 5169], [Loc Type, 8, 2, ST, ST], [Loc Name, 10, 35, Hornsby, Hornsby], [Loc Addr Ln1, 45, 40, West_field Shopping Centre, West_field Shopping Centre], [Loc Addr Ln2, 85, 40, George Street, George Street], [Loc Addr Ln3, 125, 35, Hornsby, Hornsby], [Loc Postcode, 160, 10, 2077, 2077], [Loc State, 170, 3, NSW, NSW]]')
		else:
			select('Table', 'cell:Data,5(George Street)')

		commonBits.closeWindow(click)
		##click('BasicInternalFrameTitlePane$NoFocusButton2')
		commonBits.closeWindow(click)
		##click('BasicInternalFrameTitlePane$NoFocusButton2')
##		click('BasicInternalFrameTitlePane$NoFocusButton5')
		#select('Table', 'cell:10 - 35|Loc Name,1(VIC West Ad Support)')
		#click('MetalInternalFrameTitlePane', 396, 14)
		#click('BasicInternalFrameTitlePane$NoFocusButton2')

		#close()
		if window('Save Changes to file: ' + commonBits.sampleDir() + 'utf8a_Ams_LocDownload_20041228.txt'):
			click('No')
		close()
	close()
