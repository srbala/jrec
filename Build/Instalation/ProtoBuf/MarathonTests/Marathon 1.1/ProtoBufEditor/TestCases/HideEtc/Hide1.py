useFixture(default)

def test():
	from Modules import commonBits
	java_recorded_version = '1.6.0_17'
	if window(commonBits.applicationName()):
		select('FileNameTxtFld', commonBits.sampleDir() +  'Ams_LocDownload_20041228.bin')
		click('Edit1')
		select('LinesTbl', 'rows:[3,4,5,6,7,8,9,10,11],columns:[4|Loc_Name]')
		select_menu('View>>Table View #{Selected Records#}')
##		select('Table2', 'rows:[3,4,5,6,7,8,9,10,11],columns:[4|Loc_Name]')
		select('LinesTbl', 'cell:4|Loc_Name,3(Blacktown)')
		assert_p('LinesTbl', 'Content', '[[TAR, 5866, DC, WA Ad Support, , , , , , A], [TAR, 5015, ST, Bankstown, Bankstown, Unit 2, 39-41 Allingham Street, Condell Park, 2200, NSW, A], [TAR, 5019, ST, Penrith, Penrith, 58 Leland Street, Penrith, 2750, NSW, A], [TAR, 5033, ST, Blacktown, Marayong, Dock 2, 11 Melissa Place, Marayong, 2148, NSW, A], [TAR, 5035, ST, Rockdale, Building B,  Portside DC, 2-8 Mc Pherson Street, Botany, 2019, NSW, A], [TAR, 5037, ST, Miranda, Westfield Shoppingtown, Cnr. Urunga Pde & The Kingsway, Miranda, 2228, NSW, A], [TAR, 5052, ST, Eastwood, Marayong Offsite Reserve, 11 Melissa Place, Marayong, 2148, NSW, A], [TAR, 5055, ST, Leichhardt, Marketown, Marion Street, Leichhardt, 2040, NSW, A], [TAR, 5060, ST, St Marys, St. Mary\'s, Charles Hackett Drive, St Mary\'s, 2760, NSW, A]]')
		select('LinesTbl', 'cell:1|Brand_Id,1(TAR)')
		rightclick('LinesTbl', '1|Brand_Id,1')
		select_menu('Hide Column')
		select('LinesTbl', 'cell:7|Loc_Addr_Ln3,1(Condell Park)')
		rightclick('LinesTbl', '7|Loc_Addr_Ln3,1')
		select_menu('Hide Column')
		select('LinesTbl', 'cell:8|Loc_Postcode,1(2200)')
		rightclick('LinesTbl', '8|Loc_Postcode,1')
		select_menu('Hide Column')
		select('LinesTbl', 'cell:9|Loc_State,1(NSW)')
		rightclick('LinesTbl', '9|Loc_State,1')
		select_menu('Hide Column')
		select('LinesTbl', 'cell:5|Loc_Addr_Ln1,2(Penrith)')
		assert_p('LinesTbl', 'Content', '[[5866, DC, WA Ad Support, , , A], [5015, ST, Bankstown, Bankstown, Unit 2, 39-41 Allingham Street, A], [5019, ST, Penrith, Penrith, 58 Leland Street, A], [5033, ST, Blacktown, Marayong, Dock 2, 11 Melissa Place, A], [5035, ST, Rockdale, Building B,  Portside DC, 2-8 Mc Pherson Street, A], [5037, ST, Miranda, Westfield Shoppingtown, Cnr. Urunga Pde & The Kingsway, A], [5052, ST, Eastwood, Marayong Offsite Reserve, 11 Melissa Place, A], [5055, ST, Leichhardt, Marketown, Marion Street, A], [5060, ST, St Marys, St. Mary\'s, Charles Hackett Drive, A]]')
		select('LinesTbl', 'cell:5|Loc_Addr_Ln1,2(Penrith)')
		rightclick('LinesTbl', '6|Loc_Addr_Ln2,3')
		select_menu('Show Column>>Brand_Id')
		select('LinesTbl', 'cell:5|Loc_Addr_Ln1,5(Westfield Shoppingtown)')
		assert_p('LinesTbl', 'Content', '[[TAR, 5866, DC, WA Ad Support, , , A], [TAR, 5015, ST, Bankstown, Bankstown, Unit 2, 39-41 Allingham Street, A], [TAR, 5019, ST, Penrith, Penrith, 58 Leland Street, A], [TAR, 5033, ST, Blacktown, Marayong, Dock 2, 11 Melissa Place, A], [TAR, 5035, ST, Rockdale, Building B,  Portside DC, 2-8 Mc Pherson Street, A], [TAR, 5037, ST, Miranda, Westfield Shoppingtown, Cnr. Urunga Pde & The Kingsway, A], [TAR, 5052, ST, Eastwood, Marayong Offsite Reserve, 11 Melissa Place, A], [TAR, 5055, ST, Leichhardt, Marketown, Marion Street, A], [TAR, 5060, ST, St Marys, St. Mary\'s, Charles Hackett Drive, A]]')
		select('LinesTbl', 'cell:6|Loc_Addr_Ln2,6(11 Melissa Place)')
		rightclick('LinesTbl', '6|Loc_Addr_Ln2,6')
		select_menu('Show Column>>Loc_Postcode')
		select('LinesTbl', 'cell:6|Loc_Addr_Ln2,5(Cnr. Urunga Pde & The Kingsway)')
		assert_p('LinesTbl', 'Content', '[[TAR, 5866, DC, WA Ad Support, , , , A], [TAR, 5015, ST, Bankstown, Bankstown, Unit 2, 39-41 Allingham Street, 2200, A], [TAR, 5019, ST, Penrith, Penrith, 58 Leland Street, 2750, A], [TAR, 5033, ST, Blacktown, Marayong, Dock 2, 11 Melissa Place, 2148, A], [TAR, 5035, ST, Rockdale, Building B,  Portside DC, 2-8 Mc Pherson Street, 2019, A], [TAR, 5037, ST, Miranda, Westfield Shoppingtown, Cnr. Urunga Pde & The Kingsway, 2228, A], [TAR, 5052, ST, Eastwood, Marayong Offsite Reserve, 11 Melissa Place, 2148, A], [TAR, 5055, ST, Leichhardt, Marketown, Marion Street, 2040, A], [TAR, 5060, ST, St Marys, St. Mary\'s, Charles Hackett Drive, 2760, A]]')
		select('LinesTbl', 'cell:6|Loc_Addr_Ln2,5(Cnr. Urunga Pde & The Kingsway)')
		rightclick('LinesTbl', '8|Loc_Postcode,6')
		select_menu('Show Column>>Loc_Addr_Ln3')
		select('LinesTbl', 'cell:6|Loc_Addr_Ln2,5(Cnr. Urunga Pde & The Kingsway)')
		rightclick('LinesTbl', '8|Loc_Postcode,6')
		select_menu('Show Column>>Loc_State')
		select('LinesTbl', 'cell:9|Loc_State,3(NSW)')
##		assert_p('LinesTbl', 'Content', '[[TAR, 5866, DC, WA Ad Support, , , , , , A], [TAR, 5015, ST, Bankstown, Bankstown, Unit 2, 39-41 Allingham Street, NSW, Condell Park, 2200, A], [TAR, 5019, ST, Penrith, Penrith, 58 Leland Street, NSW, Penrith, 2750, A], [TAR, 5033, ST, Blacktown, Marayong, Dock 2, 11 Melissa Place, NSW, Marayong, 2148, A], [TAR, 5035, ST, Rockdale, Building B,  Portside DC, 2-8 Mc Pherson Street, NSW, Botany, 2019, A], [TAR, 5037, ST, Miranda, Westfield Shoppingtown, Cnr. Urunga Pde & The Kingsway, NSW, Miranda, 2228, A], [TAR, 5052, ST, Eastwood, Marayong Offsite Reserve, 11 Melissa Place, NSW, Marayong, 2148, A], [TAR, 5055, ST, Leichhardt, Marketown, Marion Street, NSW, Leichhardt, 2040, A], [TAR, 5060, ST, St Marys, St. Mary\'s, Charles Hackett Drive, NSW, St Mary\'s, 2760, A]]')
		assert_p('LinesTbl', 'Content', '[[TAR, 5866, DC, WA Ad Support, , , , , , A], [TAR, 5015, ST, Bankstown, Bankstown, Unit 2, 39-41 Allingham Street, Condell Park, 2200, NSW, A], [TAR, 5019, ST, Penrith, Penrith, 58 Leland Street, Penrith, 2750, NSW, A], [TAR, 5033, ST, Blacktown, Marayong, Dock 2, 11 Melissa Place, Marayong, 2148, NSW, A], [TAR, 5035, ST, Rockdale, Building B,  Portside DC, 2-8 Mc Pherson Street, Botany, 2019, NSW, A], [TAR, 5037, ST, Miranda, Westfield Shoppingtown, Cnr. Urunga Pde & The Kingsway, Miranda, 2228, NSW, A], [TAR, 5052, ST, Eastwood, Marayong Offsite Reserve, 11 Melissa Place, Marayong, 2148, NSW, A], [TAR, 5055, ST, Leichhardt, Marketown, Marion Street, Leichhardt, 2040, NSW, A], [TAR, 5060, ST, St Marys, St. Mary\'s, Charles Hackett Drive, St Mary\'s, 2760, NSW, A]]')
	close()
