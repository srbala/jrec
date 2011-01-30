useFixture(default)

def test():
	from Modules import commonBits
	import time

	java_recorded_version = '1.6.0_17'

	if window('Record Editor'):
		select('FileChooser', commonBits.sampleDir() + 'OC_VB_Test.bin')
		select('ComboBox2', 'Unknown Format')
		commonBits.doEdit(click)


		if window(''):
			select('Table', 'cell:J,1(P)')
			assert_p('Table', 'Content', '[[T, A, R, 5, 0, 1, 5, S, T, B, a, n, k, s, t, o, w, n,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  , B, a, n, k, s, t, o, w, n,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  , U, n, i, t,  , 2, ,,  , 3, 9, -, 4, 1,  , A, l, l, i, n, g, h, a, m,  , S, t, r, e, e, t,  ,  ,  ,  ,  ,  ,  ,  ,  ,  , C, o, n, d, e, l, l,  , P, a, r, k,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  , 2, 2, 0, 0,  ,  ,  ,  ,  ,  , N, S, W, A], [T, A, R, 5, 0, 1, 9, S, T, P, e, n, r, i, t, h,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  , P, e, n, r, i, t, h,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  , 5, 8,  , L, e, l, a, n, d,  , S, t, r, e, e, t,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  , P, e, n, r, i, t, h,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  , 2, 7, 5, 0,  ,  ,  ,  ,  ,  , N, S, W, A], [T, A, R, 5, 0, 3, 3, S, T, B, l, a, c, k, t, o, w, n,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  , M, a, r, a, y, o, n, g,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  , D, o, c, k,  , 2, ,,  , 1, 1,  , M, e, l, i, s, s, a,  , P, l, a, c, e,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  , M, a, r, a, y, o, n, g,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  , 2, 1, 4, 8,  ,  ,  ,  ,  ,  , N, S, W, A], [T, A, R, 5, 0, 3, 5, S, T, R, o, c, k, d, a, l, e,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  , B, u, i, l, d, i, n, g,  , B, ,,  ,  , P, o, r, t, s, i, d, e,  , D, C,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  , 2, -, 8,  , M, c,  , P, h, e, r, s, o, n,  , S, t, r, e, e, t,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  , B, o, t, a, n, y,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  , 2, 0, 1, 9,  ,  ,  ,  ,  ,  , N, S, W, A], [T, A, R, 5, 0, 3, 7, S, T, M, i, r, a, n, d, a,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  , W, e, s, t, f, i, e, l, d,  , S, h, o, p, p, i, n, g, t, o, w, n,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  , C, n, r, .,  , U, r, u, n, g, a,  , P, d, e,  , &,  , T, h, e,  , K, i, n, g, s, w, a, y,  ,  ,  ,  ,  ,  ,  ,  ,  ,  , M, i, r, a, n, d, a,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  , 2, 2, 2, 8,  ,  ,  ,  ,  ,  , N, S, W, A], [T, A, R, 5, 0, 5, 2, S, T, E, a, s, t, w, o, o, d,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  , M, a, r, a, y, o, n, g,  , O, f, f, s, i, t, e,  , R, e, s, e, r, v, e,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  , 1, 1,  , M, e, l, i, s, s, a,  , P, l, a, c, e,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  , M, a, r, a, y, o, n, g,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  ,  , 2, 1, 4, 8,  ,  ,  ,  ,  ,  , N, S, W, A]]')
			select('Table', 'cell:J,1(P)')
##			assert_p('BmKeyedComboBox', 'Text', '8')
			assert_p('BmKeyedComboBox', 'Text', 'Open Cobol VB')
			commonBits.doSleep()

			click('Go')
			commonBits.doSleep()
		close()

		commonBits.doSleep()

		commonBits.doSleep()

		select_menu('Window>>OC_VB_Test.bin>>Table: ')


		select('Table', 'cell:1 - 1|Data,1(TAR5019STPenrith                            Penrith                                 58 Leland Street                        Penrith                            2750      NSWA)')
		assert_p('Table', 'Content', '[[TAR5015STBankstown                          Bankstown                               Unit 2, 39-41 Allingham Street          Condell Park                       2200      NSWA], [TAR5019STPenrith                            Penrith                                 58 Leland Street                        Penrith                            2750      NSWA], [TAR5033STBlacktown                          Marayong                                Dock 2, 11 Melissa Place                Marayong                           2148      NSWA], [TAR5035STRockdale                           Building B,  Portside DC                2-8 Mc Pherson Street                   Botany                             2019      NSWA], [TAR5037STMiranda                            Westfield Shoppingtown                  Cnr. Urunga Pde & The Kingsway          Miranda                            2228      NSWA], [TAR5052STEastwood                           Marayong Offsite Reserve                11 Melissa Place                        Marayong                           2148      NSWA]]')
		select('Table', 'cell:1 - 1|Data,1(TAR5019STPenrith                            Penrith                                 58 Leland Street                        Penrith                            2750      NSWA)')
		select('LayoutCombo', 'Full Line')
		select('Table', 'cell:Full Line,2(TAR5033STBlacktown                          Marayong                                Dock 2, 11 Melissa Place                Marayong                           2148      NSWA)')
		assert_p('Table', 'Content', '[[TAR5015STBankstown                          Bankstown                               Unit 2, 39-41 Allingham Street          Condell Park                       2200      NSWA], [TAR5019STPenrith                            Penrith                                 58 Leland Street                        Penrith                            2750      NSWA], [TAR5033STBlacktown                          Marayong                                Dock 2, 11 Melissa Place                Marayong                           2148      NSWA], [TAR5035STRockdale                           Building B,  Portside DC                2-8 Mc Pherson Street                   Botany                             2019      NSWA], [TAR5037STMiranda                            Westfield Shoppingtown                  Cnr. Urunga Pde & The Kingsway          Miranda                            2228      NSWA], [TAR5052STEastwood                           Marayong Offsite Reserve                11 Melissa Place                        Marayong                           2148      NSWA]]')
		select('Table', 'cell:Full Line,2(TAR5033STBlacktown                          Marayong                                Dock 2, 11 Melissa Place                Marayong                           2148      NSWA)')
		select('LayoutCombo', 'Hex 1 Line')
		select('Table', 'cell:         +         1|Hex (1 Line),0([B@168442e)')
		assert_p('Table', 'Text', '54415235303135535442616e6b73746f776e202020202020202020202020202020202020202020202020202042616e6b73746f776e20202020202020202020202020202020202020202020202020202020202020556e697420322c2033392d343120416c6c696e6768616d2053747265657420202020202020202020436f6e64656c6c205061726b2020202020202020202020202020202020202020202020323230302020202020204e535741', '         +         1|Hex (1 Line),0')
		select('Table', 'cell:         +         1|Hex (1 Line),1([B@18374c9)')
		assert_p('Table', 'Text', '54415235303139535450656e726974682020202020202020202020202020202020202020202020202020202050656e726974682020202020202020202020202020202020202020202020202020202020202020203538204c656c616e642053747265657420202020202020202020202020202020202020202020202050656e7269746820202020202020202020202020202020202020202020202020202020323735302020202020204e535741', '         +         1|Hex (1 Line),1')
		select('Table', 'cell:         +         1|Hex (1 Line),2([B@c31c7d)')
		assert_p('Table', 'Text', '544152353033335354426c61636b746f776e20202020202020202020202020202020202020202020202020204d617261796f6e672020202020202020202020202020202020202020202020202020202020202020446f636b20322c203131204d656c6973736120506c616365202020202020202020202020202020204d617261796f6e67202020202020202020202020202020202020202020202020202020323134382020202020204e535741', '         +         1|Hex (1 Line),2')
		select('Table', 'cell:         +         1|Hex (1 Line),3([B@11de95a)')
		assert_p('Table', 'Text', '544152353033355354526f636b64616c652020202020202020202020202020202020202020202020202020204275696c64696e6720422c2020506f72747369646520444320202020202020202020202020202020322d38204d632050686572736f6e2053747265657420202020202020202020202020202020202020426f74616e792020202020202020202020202020202020202020202020202020202020323031392020202020204e535741', '         +         1|Hex (1 Line),3')
		select('Table', 'cell:         +         1|Hex (1 Line),4([B@1c20de3)')
		assert_p('Table', 'Text', '5441523530333753544d6972616e646120202020202020202020202020202020202020202020202020202020576573746669656c642053686f7070696e67746f776e202020202020202020202020202020202020436e722e205572756e676120506465202620546865204b696e6773776179202020202020202020204d6972616e646120202020202020202020202020202020202020202020202020202020323232382020202020204e535741', '         +         1|Hex (1 Line),4')
		select('Table', 'cell:         +         1|Hex (1 Line),5([B@3aab44)')
		assert_p('Table', 'Text', '54415235303532535445617374776f6f642020202020202020202020202020202020202020202020202020204d617261796f6e67204f6666736974652052657365727665202020202020202020202020202020203131204d656c6973736120506c6163652020202020202020202020202020202020202020202020204d617261796f6e67202020202020202020202020202020202020202020202020202020323134382020202020204e535741', '         +         1|Hex (1 Line),5')
		select('Table', 'cell:         +         1|Hex (1 Line),5([B@3aab44)')
		select('LayoutCombo', 'Hex 2 Lines (Mainframe Style)')
		select('Table', 'cell:         +         1|Hex (2 Lines),0([B@168442e)')
		assert_p('Table', 'Text', '''T A R 5 0 1 5 S T B a n k s t o w n                                                     B a n k s t o w n                                                               U n i t   2 ,   3 9 - 4 1   A l l i n g h a m   S t r e e t                     C o n d e l l   P a r k                                               2 2 0 0             N S W A 
54415235303135535442616e6b73746f776e202020202020202020202020202020202020202020202020202042616e6b73746f776e20202020202020202020202020202020202020202020202020202020202020556e697420322c2033392d343120416c6c696e6768616d2053747265657420202020202020202020436f6e64656c6c205061726b2020202020202020202020202020202020202020202020323230302020202020204e535741''', '         +         1|Hex (2 Lines),0')
		select('Table', 'cell:         +         1|Hex (2 Lines),1([B@18374c9)')
		assert_p('Table', 'Text', '''T A R 5 0 1 9 S T P e n r i t h                                                         P e n r i t h                                                                   5 8   L e l a n d   S t r e e t                                                 P e n r i t h                                                         2 7 5 0             N S W A 
54415235303139535450656e726974682020202020202020202020202020202020202020202020202020202050656e726974682020202020202020202020202020202020202020202020202020202020202020203538204c656c616e642053747265657420202020202020202020202020202020202020202020202050656e7269746820202020202020202020202020202020202020202020202020202020323735302020202020204e535741''', '         +         1|Hex (2 Lines),1')
		select('Table', 'cell:         +         1|Hex (2 Lines),2([B@c31c7d)')
		assert_p('Table', 'Text', '''T A R 5 0 3 3 S T B l a c k t o w n                                                     M a r a y o n g                                                                 D o c k   2 ,   1 1   M e l i s s a   P l a c e                                 M a r a y o n g                                                       2 1 4 8             N S W A 
544152353033335354426c61636b746f776e20202020202020202020202020202020202020202020202020204d617261796f6e672020202020202020202020202020202020202020202020202020202020202020446f636b20322c203131204d656c6973736120506c616365202020202020202020202020202020204d617261796f6e67202020202020202020202020202020202020202020202020202020323134382020202020204e535741''', '         +         1|Hex (2 Lines),2')
		select('Table', 'cell:         +         1|Hex (2 Lines),3([B@11de95a)')
		assert_p('Table', 'Text', '''T A R 5 0 3 5 S T R o c k d a l e                                                       B u i l d i n g   B ,     P o r t s i d e   D C                                 2 - 8   M c   P h e r s o n   S t r e e t                                       B o t a n y                                                           2 0 1 9             N S W A 
544152353033355354526f636b64616c652020202020202020202020202020202020202020202020202020204275696c64696e6720422c2020506f72747369646520444320202020202020202020202020202020322d38204d632050686572736f6e2053747265657420202020202020202020202020202020202020426f74616e792020202020202020202020202020202020202020202020202020202020323031392020202020204e535741''', '         +         1|Hex (2 Lines),3')
		select('Table', 'cell:         +         1|Hex (2 Lines),4([B@1c20de3)')
		assert_p('Table', 'Text', '''T A R 5 0 3 7 S T M i r a n d a                                                         W e s t f i e l d   S h o p p i n g t o w n                                     C n r .   U r u n g a   P d e   &   T h e   K i n g s w a y                     M i r a n d a                                                         2 2 2 8             N S W A 
5441523530333753544d6972616e646120202020202020202020202020202020202020202020202020202020576573746669656c642053686f7070696e67746f776e202020202020202020202020202020202020436e722e205572756e676120506465202620546865204b696e6773776179202020202020202020204d6972616e646120202020202020202020202020202020202020202020202020202020323232382020202020204e535741''', '         +         1|Hex (2 Lines),4')
		select('Table', 'cell:         +         1|Hex (2 Lines),5([B@3aab44)')
		assert_p('Table', 'Text', '''T A R 5 0 5 2 S T E a s t w o o d                                                       M a r a y o n g   O f f s i t e   R e s e r v e                                 1 1   M e l i s s a   P l a c e                                                 M a r a y o n g                                                       2 1 4 8             N S W A 
54415235303532535445617374776f6f642020202020202020202020202020202020202020202020202020204d617261796f6e67204f6666736974652052657365727665202020202020202020202020202020203131204d656c6973736120506c6163652020202020202020202020202020202020202020202020204d617261796f6e67202020202020202020202020202020202020202020202020202020323134382020202020204e535741''', '         +         1|Hex (2 Lines),5')
		select('Table', 'cell:         +         1|Hex (2 Lines),5([B@3aab44)')
		select('LayoutCombo', 'Hex 3 Lines (ISPF Edit Hex)')
		select('Table', 'cell:    +    1|Hex (SPF Edit Style),0([B@168442e)')
		assert_p('Table', 'Text', '''TAR5015STBankstown                          Bankstown                               Unit 2, 39-41 Allingham Street          Condell Park                       2200      NSWA
54533335546667767622222222222222222222222222466677676222222222222222222222222222222256672322332332466666666257766722222222224666666256762222222222222222222222233332222224554
41250153421eb34f7e0000000000000000000000000021eb34f7e00000000000000000000000000000005e9402c039d4101cc9e781d034255400000000003fe45cc0012b000000000000000000000002200000000e371''', '    +    1|Hex (SPF Edit Style),0')
		select('Table', 'cell:    +    1|Hex (SPF Edit Style),1([B@18374c9)')
		assert_p('Table', 'Text', '''TAR5019STPenrith                            Penrith                                 58 Leland Street                        Penrith                            2750      NSWA
54533335556676762222222222222222222222222222566767622222222222222222222222222222222233246666625776672222222222222222222222225667676222222222222222222222222222233332222224554
41250193405e2948000000000000000000000000000005e2948000000000000000000000000000000000580c5c1e4034255400000000000000000000000005e294800000000000000000000000000002750000000e371''', '    +    1|Hex (SPF Edit Style),1')
		select('Table', 'cell:    +    1|Hex (SPF Edit Style),2([B@c31c7d)')
		assert_p('Table', 'Text', '''TAR5033STBlacktown                          Marayong                                Dock 2, 11 Melissa Place                Marayong                           2148      NSWA
54533335546666767622222222222222222222222222467676662222222222222222222222222222222246662322332466677625666622222222222222224676766622222222222222222222222222233332222224554
4125033342c13b4f7e00000000000000000000000000d1219fe7000000000000000000000000000000004f3b02c0110d5c933100c1350000000000000000d1219fe70000000000000000000000000002148000000e371''', '    +    1|Hex (SPF Edit Style),2')
		select('Table', 'cell:    +    1|Hex (SPF Edit Style),3([B@11de95a)')
		assert_p('Table', 'Text', '''TAR5035STRockdale                           Building B,  Portside DC                2-8 Mc Pherson Street                   Botany                             2019      NSWA
54533335556666666222222222222222222222222222476666662422256777666244222222222222222232324625667766257766722222222222222222224676672222222222222222222222222222233332222224554
4125035342f3b41c5000000000000000000000000000259c49e702c000f24394504300000000000000002d80d3008523fe034255400000000000000000002f41e9000000000000000000000000000002019000000e371''', '    +    1|Hex (SPF Edit Style),3')
		select('Table', 'cell:    +    1|Hex (SPF Edit Style),4([B@1c20de3)')
		assert_p('Table', 'Text', '''TAR5037STMiranda                            Westfield Shoppingtown                  Cnr. Urunga Pde & The Kingsway          Miranda                            2228      NSWA
54533335546766662222222222222222222222222222567766666256677666767622222222222222222246722577666256622256624666776722222222224676666222222222222222222222222222233332222224554
412503734d921e4100000000000000000000000000007534695c4038f009e74f7e0000000000000000003e2e0525e7100450604850b9e737190000000000d921e4100000000000000000000000000002228000000e371''', '    +    1|Hex (SPF Edit Style),4')
		select('Table', 'cell:    +    1|Hex (SPF Edit Style),5([B@3aab44)')
		assert_p('Table', 'Text', '''TAR5052STEastwood                           Marayong Offsite Reserve                11 Melissa Place                        Marayong                           2148      NSWA
54533335546777666222222222222222222222222222467676662466767625676776222222222222222233246667762566662222222222222222222222224676766622222222222222222222222222233332222224554
41250523451347ff4000000000000000000000000000d1219fe70f663945025352650000000000000000110d5c933100c135000000000000000000000000d1219fe70000000000000000000000000002148000000e371''', '    +    1|Hex (SPF Edit Style),5')
		select('Table', 'cell:    +    1|Hex (SPF Edit Style),2([B@c31c7d)')
		rightclick('Table', '    +    1|Hex (SPF Edit Style),2')
		select_menu('Edit Record')
##		select('Table1', 'cell:    +    1|Hex (SPF Edit Style),2([B@c31c7d)')
		select('Table', 'cell:Data,0(TAR5033STBlacktown                          Marayong                                Dock 2, 11 Melissa Place                Marayong                           2148      NSWA)')
		assert_p('Table', 'Content', '[[Data, 1, 1, TAR5033STBlacktown                          Marayong                                Dock 2, 11 Melissa Place                Marayong                           2148      NSWA, T, 544152353033335354426c61636b746f776e20202020202020202020202020202020202020202020202020204d617261796f6e672020202020202020202020202020202020202020202020202020202020202020446f636b20322c203131204d656c6973736120506c616365202020202020202020202020202020204d617261796f6e67202020202020202020202020202020202020202020202020202020323134382020202020204e535741]]')
		select('Table', 'cell:Data,0(TAR5033STBlacktown                          Marayong                                Dock 2, 11 Melissa Place                Marayong                           2148      NSWA)')
		assert_p('Table', 'Content', '[[Data, 1, 1, TAR5033STBlacktown                          Marayong                                Dock 2, 11 Melissa Place                Marayong                           2148      NSWA, T, 544152353033335354426c61636b746f776e20202020202020202020202020202020202020202020202020204d617261796f6e672020202020202020202020202020202020202020202020202020202020202020446f636b20322c203131204d656c6973736120506c616365202020202020202020202020202020204d617261796f6e67202020202020202020202020202020202020202020202020202020323134382020202020204e535741]]')
		select('Table', 'cell:Data,0(TAR5033STBlacktown                          Marayong                                Dock 2, 11 Melissa Place                Marayong                           2148      NSWA)')
		assert_p('Table', 'Text', 'cell:Data,0(TAR5033STBlacktown                          Marayong                                Dock 2, 11 Melissa Place                Marayong                           2148      NSWA)')
		select('Table', 'cell:Hex,0(544152353033335354426c61636b746f776e20202020202020202020202020202020202020202020202020204d617261796f6e672020202020202020202020202020202020202020202020202020202020202020446f636b20322c203131204d656c6973736120506c616365202020202020202020202020202020204d617261796f6e67202020202020202020202020202020202020202020202020202020323134382020202020204e535741)')
		assert_p('Table', 'Text', '544152353033335354426c61636b746f776e20202020202020202020202020202020202020202020202020204d617261796f6e672020202020202020202020202020202020202020202020202020202020202020446f636b20322c203131204d656c6973736120506c616365202020202020202020202020202020204d617261796f6e67202020202020202020202020202020202020202020202020202020323134382020202020204e535741', 'Hex,0')
		select('Table', 'cell:Hex,0(544152353033335354426c61636b746f776e20202020202020202020202020202020202020202020202020204d617261796f6e672020202020202020202020202020202020202020202020202020202020202020446f636b20322c203131204d656c6973736120506c616365202020202020202020202020202020204d617261796f6e67202020202020202020202020202020202020202020202020202020323134382020202020204e535741)')
		select('CheckBox', 'false')
		select('Table', 'cell:Hex,0([B@be568b)')
		assert_p('Table', 'Text', '''TAR5033STBlacktown                          Marayong                                Dock 2, 11 Melissa Place                Marayong                           2148      NSW
5453333554666676762222222222222222222222222246767666222222222222222222222222222222224666232233246667762566662222222222222222467676662222222222222222222222222223333222222455
4125033342c13b4f7e00000000000000000000000000d1219fe7000000000000000000000000000000004f3b02c0110d5c933100c1350000000000000000d1219fe70000000000000000000000000002148000000e37''', 'Hex,0')
		select('Table', 'cell:Hex,0([B@1aff6b1)')
		select('Table', 'cell:Hex,0([B@1589559)')
		commonBits.closeWindow(click)
		##click('BasicInternalFrameTitlePane$NoFocusButton2')
		select('Table', 'cell:    +    1|Hex (SPF Edit Style),2([B@c31c7d)')
	close()
