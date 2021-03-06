useFixture(RecordEditor)

def test():
	from Modules import commonBits
	java_recorded_version = '1.5.0_11'

	if window('Record Editor'):
		select('FileChooser', commonBits.sampleDir() + 'Ams_LocDownload_20041228.txt')
		click(commonBits.fl('Edit') + '1')
		select('Table', 'rows:[2,3,4,5,6,7,8,9],columns:[10 - 35|Loc Name]')
		select_menu(commonBits.fl('View') + '>>' + commonBits.fl('Table View #{Selected Records#}'))
##		select('Table2', 'rows:[2,3,4,5,6,7,8,9],columns:[10 - 35|Loc Name]')
		select('Table', 'rows:[1,2],columns:[8 - 2|Loc Type]')
		select_menu(commonBits.fl('Edit') + '>>' + commonBits.fl('Copy Record#{s#}'))
		select('Table', 'cell:8 - 2|Loc Type,5(ST)')
		select_menu(commonBits.fl('Edit') + '>>' + commonBits.fl('Paste Record#{s#}'))

		select('Table', 'cell:10 - 35|Loc Name,3(Penrith)')
		assert_p('Table', 'Content', '[[TAR, 5853, DC, NSW North Sydney Ad Support, , , , , , A], [TAR, 5866, DC, WA Ad Support, , , , , , A], [TAR, 5015, ST, Bankstown, Bankstown, Unit 2, 39-41 Allingham Street, Condell Park, 2200, NSW, A], [TAR, 5019, ST, Penrith, Penrith, 58 Leland Street, Penrith, 2750, NSW, A], [TAR, 5033, ST, Blacktown, Marayong, Dock 2, 11 Melissa Place, Marayong, 2148, NSW, A], [TAR, 5035, ST, Rockdale, Building B,  Portside DC, 2-8 Mc Pherson Street, Botany, 2019, NSW, A], [TAR, 5866, DC, WA Ad Support, , , , , , A], [TAR, 5015, ST, Bankstown, Bankstown, Unit 2, 39-41 Allingham Street, Condell Park, 2200, NSW, A], [TAR, 5037, ST, Miranda, Westfield Shoppingtown, Cnr. Urunga Pde & The Kingsway, Miranda, 2228, NSW, A], [TAR, 5052, ST, Eastwood, Marayong Offsite Reserve, 11 Melissa Place, Marayong, 2148, NSW, A]]')
		select('Table', 'cell:10 - 35|Loc Name,4(Blacktown)')
		assert_p('Table', 'RowCount', '10')
		select('Table', 'rows:[1,2],columns:[10 - 35|Loc Name]')
		select_menu(commonBits.fl('Edit') + '>>' + commonBits.fl('Cut Record#{s#}'))
		select('Table', 'cell:10 - 35|Loc Name,4(WA Ad Support)')
		assert_p('Table', 'Content', '[[TAR, 5853, DC, NSW North Sydney Ad Support, , , , , , A], [TAR, 5019, ST, Penrith, Penrith, 58 Leland Street, Penrith, 2750, NSW, A], [TAR, 5033, ST, Blacktown, Marayong, Dock 2, 11 Melissa Place, Marayong, 2148, NSW, A], [TAR, 5035, ST, Rockdale, Building B,  Portside DC, 2-8 Mc Pherson Street, Botany, 2019, NSW, A], [TAR, 5866, DC, WA Ad Support, , , , , , A], [TAR, 5015, ST, Bankstown, Bankstown, Unit 2, 39-41 Allingham Street, Condell Park, 2200, NSW, A], [TAR, 5037, ST, Miranda, Westfield Shoppingtown, Cnr. Urunga Pde & The Kingsway, Miranda, 2228, NSW, A], [TAR, 5052, ST, Eastwood, Marayong Offsite Reserve, 11 Melissa Place, Marayong, 2148, NSW, A]]')
		select('Table', 'cell:10 - 35|Loc Name,5(Bankstown)')
		assert_p('Table', 'Content', '[[TAR, 5853, DC, NSW North Sydney Ad Support, , , , , , A], [TAR, 5019, ST, Penrith, Penrith, 58 Leland Street, Penrith, 2750, NSW, A], [TAR, 5033, ST, Blacktown, Marayong, Dock 2, 11 Melissa Place, Marayong, 2148, NSW, A], [TAR, 5035, ST, Rockdale, Building B,  Portside DC, 2-8 Mc Pherson Street, Botany, 2019, NSW, A], [TAR, 5866, DC, WA Ad Support, , , , , , A], [TAR, 5015, ST, Bankstown, Bankstown, Unit 2, 39-41 Allingham Street, Condell Park, 2200, NSW, A], [TAR, 5037, ST, Miranda, Westfield Shoppingtown, Cnr. Urunga Pde & The Kingsway, Miranda, 2228, NSW, A], [TAR, 5052, ST, Eastwood, Marayong Offsite Reserve, 11 Melissa Place, Marayong, 2148, NSW, A]]')
		select('Table', 'cell:10 - 35|Loc Name,6(Miranda)')
		select_menu(commonBits.fl('Edit') + '>>' + commonBits.fl('Paste Record#{s#} Prior'))

		select('Table', 'cell:10 - 35|Loc Name,4(WA Ad Support)')
		assert_p('Table', 'RowCount', '10')
		select('Table', 'cell:10 - 35|Loc Name,3(Rockdale)')
		assert_p('Table', 'Content', '[[TAR, 5853, DC, NSW North Sydney Ad Support, , , , , , A], [TAR, 5019, ST, Penrith, Penrith, 58 Leland Street, Penrith, 2750, NSW, A], [TAR, 5033, ST, Blacktown, Marayong, Dock 2, 11 Melissa Place, Marayong, 2148, NSW, A], [TAR, 5035, ST, Rockdale, Building B,  Portside DC, 2-8 Mc Pherson Street, Botany, 2019, NSW, A], [TAR, 5866, DC, WA Ad Support, , , , , , A], [TAR, 5015, ST, Bankstown, Bankstown, Unit 2, 39-41 Allingham Street, Condell Park, 2200, NSW, A], [TAR, 5866, DC, WA Ad Support, , , , , , A], [TAR, 5015, ST, Bankstown, Bankstown, Unit 2, 39-41 Allingham Street, Condell Park, 2200, NSW, A], [TAR, 5037, ST, Miranda, Westfield Shoppingtown, Cnr. Urunga Pde & The Kingsway, Miranda, 2228, NSW, A], [TAR, 5052, ST, Eastwood, Marayong Offsite Reserve, 11 Melissa Place, Marayong, 2148, NSW, A]]')
		select('Table', 'rows:[6,7,8],columns:[10 - 35|Loc Name]')
		select_menu(commonBits.fl('Edit') + '>>' + commonBits.fl('Delete Record#{s#}'))
		select('Table', 'cell:10 - 35|Loc Name,3(Rockdale)')
		assert_p('Table', 'RowCount', '7')
		select('Table', 'cell:10 - 35|Loc Name,2(Blacktown)')
		assert_p('Table', 'Content', '[[TAR, 5853, DC, NSW North Sydney Ad Support, , , , , , A], [TAR, 5019, ST, Penrith, Penrith, 58 Leland Street, Penrith, 2750, NSW, A], [TAR, 5033, ST, Blacktown, Marayong, Dock 2, 11 Melissa Place, Marayong, 2148, NSW, A], [TAR, 5035, ST, Rockdale, Building B,  Portside DC, 2-8 Mc Pherson Street, Botany, 2019, NSW, A], [TAR, 5866, DC, WA Ad Support, , , , , , A], [TAR, 5015, ST, Bankstown, Bankstown, Unit 2, 39-41 Allingham Street, Condell Park, 2200, NSW, A], [TAR, 5052, ST, Eastwood, Marayong Offsite Reserve, 11 Melissa Place, Marayong, 2148, NSW, A]]')
		select('Table', 'rows:[4,5],columns:[10 - 35|Loc Name]')
		commonBits.closeWindow(click)
		##click('BasicInternalFrameTitlePane$NoFocusButton2')
		commonBits.closeWindow(click)
		##click('BasicInternalFrameTitlePane$NoFocusButton2')

		if window(commonBits.fl('Save Changes to file: ' + commonBits.sampleDir() + 'Ams_LocDownload_20041228.txt')):
			click('No')
		close()
	close()
