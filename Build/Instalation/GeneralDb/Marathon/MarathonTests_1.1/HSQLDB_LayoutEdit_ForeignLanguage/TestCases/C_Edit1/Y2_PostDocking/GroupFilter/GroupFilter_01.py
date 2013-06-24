useFixture(RecordEditor)

def test():
	from Modules import commonBits
	java_recorded_version = '1.6.0_22'

	if window('Record Editor'):
		select('File_Txt', commonBits.sampleDir() + 'Ams_PODownload_20041231.txt')
		click(commonBits.fl('Edit') + '1')
		click('Filter1')
		select('TabbedPane', commonBits.fl('Group Filter'))
		select('Filter.RecordSelection_JTbl1', 'false', commonBits.fl('In Group') + ',1')
##		select('Filter.RecordSelection_JTbl1', 'cell:' + commonBits.fl('In Group') + ',1(false)')

		select('Fields.FieldRelationship_JTbl1', '8', commonBits.fl('Value') + ',0')

		select('Fields.FieldRelationship_JTbl1', 'cell:' + commonBits.fl('Field') + ',0(0)')
		click('ArrowButton')
		select_menu('ams PO Download: Detail>>Pack Qty')


		select('Fields.FieldRelationship_JTbl1', 'cell:' + commonBits.fl('Operator') + ',0(' + commonBits.fl('Contains') + ')')
		select('Fields.FieldRelationship_JTbl1', 'cell:' + commonBits.fl('Value') + ',0()')
		select('Fields.FieldRelationship_JTbl1', '<', commonBits.fl('Operator') + ',0')
		select('Fields.FieldRelationship_JTbl1', commonBits.fl('>= (Numeric)'), commonBits.fl('Operator') + ',0')
##		select('Fields.FieldRelationship_JTbl1', 'cell:' + commonBits.fl('Operator') + ',0(' + commonBits.fl('Contains') + ')')
##		click('ScrollPane$ScrollBar', 8, 106)
##		select('Fields.FieldRelationship_JTbl1', '8', commonBits.fl('Value') + ',0')
##		select('Fields.FieldRelationship_JTbl1', 'cell:' + commonBits.fl('Value') + ',1()')

		commonBits.filter2(click)
##		click(commonBits.fl('Filter') + '1')
##		select('TabbedPane1', 'Table:')
		select_menu(commonBits.fl('Window') + '>>Ams_PODownload_20041231.txt>>' + commonBits.fl('Table:'))
		click(commonBits.fl('Table:') + '1')
		assert_p('LineList.FileDisplay_JTbl1', 'Content', '[[D1, 4, 80000000, 1, 48320000, 5561, 50710000, 5, 45400000, 48, 207, 5361, , 5561, 5071, M, .ROSE 24, -6, 607 SHWL], [S1, 5036, 3, 5043, 5, 3331, 50710003, 5065, 4, 5069, 4, 5076, 4, 5079, 2, 5094, 4, 5128, 3], [S1, 5151, 4, 5180, 3, 5173, 2, , 0, , 0, , 0, , 0, , 0, , 0], [D1, 1, 60000006, 2281, 48320000, 0222, 45310000, 5, 45400000, 16, 207, 5348, , 5614, 531, D, ONKEY 24, -6, 607 SHWL], [S1, 5019, 1, 5037, 1, 5078, 1, 5085, 1, 5091, 1, 5093, 1, 5095, 1, 51 D, ONKEY 24, -6, 607 SHWL], [S1, 5171, 1, 5177, 1, 5136, 1, 5145, 1, 5096, 1, , 0, , 0, , 0, , 0], [D1, 0, 80000000, 1, 48320000, 6222, 49440000, 5, 45400000, 8, 207, 5349, , 6561, 4944, M, ILK 24-0, 660, 7 SHWL W], [S1, 5019, 1, 5037, 1, 5091, 1, 5093, 1, 5129, 1, 5177, 1, 5145, 1, , 0, , 0], [D1, 10, 80000000, 1, 48320000, 6222, 50710000, 5, 45400001, 8, 207, 5350, , 6561, 5071, M, .ROSE 24, -6, 607 SHWL], [S1, 5015, 2, 5019, 5, 5035, 2, 5037, 4, 5052, 2, 5055, 2, 5060, 2, 5070, 2, 5074, 4], [S1, 5078, 5, 5081, 2, 5090, 2, 5091, 4, 5093, 4, 5095, 4, 5129, 4, 5144, 4, 5165, 2], [S1, 5303, 2, 5169, 2, 5171, 3, 5177, 4, 5016, 2, 5089, 4, 5136, 3, 5011, 2, 5046, 2], [S1, 5145, 4, 5096, 3, 5162, 2, 5163, 2, 5164, 2, 5192, 2, 5150, 2, 5175, 2, , 0], [D1, 0, 80000000, 1, 48320000, 5222, 51560000, 5, 45400000, 8, 207, 5351, , 5561, 5156, M, .ROSE 24, -6, 607 SHWL], [S1, 5019, 1, 5037, 1, 5091, 1, 5093, 1, 5129, 1, 5177, 1, 5145, 1, , 0, , 0], [D1, 4, 40000000, 1, 48320000, 4561, 50710000, 5, 45400000, 44, 207, 5354, , 4561, 5071, M, .ROSE 24, -6, 607 SHWL], [S1, 5009, 5, 5021, 5, 5025, 4, 5026, 4, 5047, 3, 5077, 2, 5127, 5, 5134, 4, 5142, 2], [S1, 5044, 2, 5071, 2, , 0, , 0, , 0, , 0, , 0, , 0, , 0], [D1, 3, 0, 2, 92680000, 4584, 66800000, 7, 27200000, 30, 212, 736, , 4561, 5156, C, ONCERTO, BLAC, K LEATHE], [S1, 5036, 2, 5043, 3, 5057, 1, 5065, 2, 5069, 2, 5076, 3, 5079, 1, 5094, 3, 5128, 3], [S1, 5151, 3, 5180, 2, 5173, 1, , 0, , 0, , 0, , 0, , 0, , 0], [D1, 2, 90000000, 1, 98360000, 4584, 67720000, 5, 45400000, 29, 212, 1104, , 5846, 772, A, NGEL PIN, K SY, NTHETIC], [S1, 5036, 2, 5043, 3, 5057, 1, 5065, 2, 5069, 2, 5076, 3, 5079, 1, 5094, 2, 5128, 3], [S1, 5151, 3, 5180, 2, 5173, 1, , 0, , 0, , 0, , 0, , 0, , 0], [D1, 2, 90000000, 1, 98360000, 4584, 74890000, 5, 45400000, 29, 212, 1627, , 4584, 7489, A, NGEL PIN, K SY, NTHETIC], [S1, 5036, 2, 5043, 3, 5057, 1, 5065, 2, 5069, 2, 5076, 2, 5079, 1, 5094, 3, 5128, 3], [S1, 5151, 3, 5180, 2, 5173, 1, , 0, , 0, , 0, , 0, , 0, , 0], [D1, 2, 50000000, 4, 65480000, 4584, 87070000, 9, 9000000, 25, 217, 9843, , 4584, 8707A, A, NGEL PIN, K SY, NTHETIC], [S1, 5036, 2, 5043, 2, 5057, 1, 5065, 2, 5069, 2, 5076, 2, 5079, 1, 5094, 2, 5128, 2], [S1, 5151, 2, 5180, 2, 5173, 1, , 0, , 0, , 0, , 0, , 0, , 0], [D1, 0, 80000000, 0, 82160000, 4616, 47900000, 3, 63600000, 8, 220, 3070, , 4616, 4790B8, A, NGEL PIN, K SY, NTHETIC], [S1, 5043, 1, 5045, 1, 5069, 1, 5076, 1, 5094, 1, 5128, 1, 5151, 1, , 0, , 0], [D1, 2, 40000000, 1, 12970000, 4616, 47900000, 3, 63600000, 24, 220, 3056, , 4616, 4790, A, NGEL PIN, K SY, NTHETIC], [S1, 5036, 1, 5043, 2, 5057, 1, 5065, 2, 5069, 2, 5076, 2, 5079, 1, 5094, 2, 5128, 2], [S1, 5151, 3, 5180, 2, 5173, 1, , 0, , 0, , 0, , 0, , 0, , 0], [D1, 2, 30000000, 1, 12970000, 4616, 53600000, 3, 63600000, 23, 220, 3072, , 4616, 5360, C, ABERETCA, RAME, L MICRO], [S1, 5036, 1, 5043, 2, 5057, 1, 5065, 2, 5069, 2, 5076, 2, 5079, 1, 5094, 1, 5128, 2], [S1, 5151, 3, 5180, 2, 5173, 1, , 0, , 0, , 0, , 0, , 0, , 0], [D1, 0, 80000000, 0, 83840000, 4592, 85530000, 3, 63600000, 8, 220, 3222, , 4592, 8553B8, C, ABERETCA, RAME, L MICRO], [S1, 5043, 1, 5045, 1, 5076, 1, 5094, 1, 5128, 1, 5151, 1, 5180, 1, , 0, , 0], [D1, 2, 20000000, 1, 25760000, 4592, 85530000, 3, 63600000, 22, 220, 3219, , 4592, 8553, C, ABERETCA, RAME, L MICRO], [S1, 5036, 1, 5043, 2, 5057, 1, 5065, 1, 5069, 2, 5076, 2, 5079, 1, 5094, 2, 5128, 2], [S1, 5151, 2, 5180, 2, 5173, 1, , 0, , 0, , 0, , 0, , 0, , 0], [D1, 2, 20000000, 1, 25760000, 1593, 57590000, 3, 63600000, 22, 220, 3223, , 593, 5759, J, AZZ DUST, Y PI, NK HEELE], [S1, 5036, 1, 5043, 2, 5057, 1, 5065, 1, 5069, 2, 5076, 2, 5079, 1, 5094, 2, 5128, 2], [S1, 5151, 3, 5180, 1, 5173, 1, , 0, , 0, , 0, , 0, , 0, , 0]]')
		select_menu(commonBits.fl('Window') + '>>Ams_PODownload_20041231.txt>>' + commonBits.fl('Filter Options'))
		select('Fields.FieldRelationship_JTbl1', '10', commonBits.fl('Value') + ',0')
		select('Fields.FieldRelationship_JTbl1', 'cell:' + commonBits.fl('Value') + ',1()')

		commonBits.filter2(click)
##		click(commonBits.fl('Filter') + '1')
##		select('TabbedPane1', 'Table:')
		select_menu(commonBits.fl('Window') + '>>Ams_PODownload_20041231.txt>>' + commonBits.fl('Filter Options'))
		select_menu(commonBits.fl('Window') + '>>Ams_PODownload_20041231.txt>>' + commonBits.fl('Table:'))
		assert_p('LineList.FileDisplay_JTbl2', 'Content', '[[D1, 4, 80000000, 1, 48320000, 5561, 50710000, 5, 45400000, 48, 207, 5361, , 5561, 5071, M, .ROSE 24, -6, 607 SHWL], [S1, 5036, 3, 5043, 5, 3331, 50710003, 5065, 4, 5069, 4, 5076, 4, 5079, 2, 5094, 4, 5128, 3], [S1, 5151, 4, 5180, 3, 5173, 2, , 0, , 0, , 0, , 0, , 0, , 0], [D1, 1, 60000006, 2281, 48320000, 0222, 45310000, 5, 45400000, 16, 207, 5348, , 5614, 531, D, ONKEY 24, -6, 607 SHWL], [S1, 5019, 1, 5037, 1, 5078, 1, 5085, 1, 5091, 1, 5093, 1, 5095, 1, 51 D, ONKEY 24, -6, 607 SHWL], [S1, 5171, 1, 5177, 1, 5136, 1, 5145, 1, 5096, 1, , 0, , 0, , 0, , 0], [D1, 10, 80000000, 1, 48320000, 6222, 50710000, 5, 45400001, 8, 207, 5350, , 6561, 5071, M, .ROSE 24, -6, 607 SHWL], [S1, 5015, 2, 5019, 5, 5035, 2, 5037, 4, 5052, 2, 5055, 2, 5060, 2, 5070, 2, 5074, 4], [S1, 5078, 5, 5081, 2, 5090, 2, 5091, 4, 5093, 4, 5095, 4, 5129, 4, 5144, 4, 5165, 2], [S1, 5303, 2, 5169, 2, 5171, 3, 5177, 4, 5016, 2, 5089, 4, 5136, 3, 5011, 2, 5046, 2], [S1, 5145, 4, 5096, 3, 5162, 2, 5163, 2, 5164, 2, 5192, 2, 5150, 2, 5175, 2, , 0], [D1, 4, 40000000, 1, 48320000, 4561, 50710000, 5, 45400000, 44, 207, 5354, , 4561, 5071, M, .ROSE 24, -6, 607 SHWL], [S1, 5009, 5, 5021, 5, 5025, 4, 5026, 4, 5047, 3, 5077, 2, 5127, 5, 5134, 4, 5142, 2], [S1, 5044, 2, 5071, 2, , 0, , 0, , 0, , 0, , 0, , 0, , 0], [D1, 3, 0, 2, 92680000, 4584, 66800000, 7, 27200000, 30, 212, 736, , 4561, 5156, C, ONCERTO, BLAC, K LEATHE], [S1, 5036, 2, 5043, 3, 5057, 1, 5065, 2, 5069, 2, 5076, 3, 5079, 1, 5094, 3, 5128, 3], [S1, 5151, 3, 5180, 2, 5173, 1, , 0, , 0, , 0, , 0, , 0, , 0], [D1, 2, 90000000, 1, 98360000, 4584, 67720000, 5, 45400000, 29, 212, 1104, , 5846, 772, A, NGEL PIN, K SY, NTHETIC], [S1, 5036, 2, 5043, 3, 5057, 1, 5065, 2, 5069, 2, 5076, 3, 5079, 1, 5094, 2, 5128, 3], [S1, 5151, 3, 5180, 2, 5173, 1, , 0, , 0, , 0, , 0, , 0, , 0], [D1, 2, 90000000, 1, 98360000, 4584, 74890000, 5, 45400000, 29, 212, 1627, , 4584, 7489, A, NGEL PIN, K SY, NTHETIC], [S1, 5036, 2, 5043, 3, 5057, 1, 5065, 2, 5069, 2, 5076, 2, 5079, 1, 5094, 3, 5128, 3], [S1, 5151, 3, 5180, 2, 5173, 1, , 0, , 0, , 0, , 0, , 0, , 0], [D1, 2, 50000000, 4, 65480000, 4584, 87070000, 9, 9000000, 25, 217, 9843, , 4584, 8707A, A, NGEL PIN, K SY, NTHETIC], [S1, 5036, 2, 5043, 2, 5057, 1, 5065, 2, 5069, 2, 5076, 2, 5079, 1, 5094, 2, 5128, 2], [S1, 5151, 2, 5180, 2, 5173, 1, , 0, , 0, , 0, , 0, , 0, , 0], [D1, 2, 40000000, 1, 12970000, 4616, 47900000, 3, 63600000, 24, 220, 3056, , 4616, 4790, A, NGEL PIN, K SY, NTHETIC], [S1, 5036, 1, 5043, 2, 5057, 1, 5065, 2, 5069, 2, 5076, 2, 5079, 1, 5094, 2, 5128, 2], [S1, 5151, 3, 5180, 2, 5173, 1, , 0, , 0, , 0, , 0, , 0, , 0], [D1, 2, 30000000, 1, 12970000, 4616, 53600000, 3, 63600000, 23, 220, 3072, , 4616, 5360, C, ABERETCA, RAME, L MICRO], [S1, 5036, 1, 5043, 2, 5057, 1, 5065, 2, 5069, 2, 5076, 2, 5079, 1, 5094, 1, 5128, 2], [S1, 5151, 3, 5180, 2, 5173, 1, , 0, , 0, , 0, , 0, , 0, , 0], [D1, 2, 20000000, 1, 25760000, 4592, 85530000, 3, 63600000, 22, 220, 3219, , 4592, 8553, C, ABERETCA, RAME, L MICRO], [S1, 5036, 1, 5043, 2, 5057, 1, 5065, 1, 5069, 2, 5076, 2, 5079, 1, 5094, 2, 5128, 2], [S1, 5151, 2, 5180, 2, 5173, 1, , 0, , 0, , 0, , 0, , 0, , 0], [D1, 2, 20000000, 1, 25760000, 1593, 57590000, 3, 63600000, 22, 220, 3223, , 593, 5759, J, AZZ DUST, Y PI, NK HEELE], [S1, 5036, 1, 5043, 2, 5057, 1, 5065, 1, 5069, 2, 5076, 2, 5079, 1, 5094, 2, 5128, 2], [S1, 5151, 3, 5180, 1, 5173, 1, , 0, , 0, , 0, , 0, , 0, , 0]]')
	close()