/*  -------------------------------------------------------------------------
 *
 *            Sub-Project: RecordEditor's version of JRecord 
 *    
 *    Sub-Project purpose: Low-level IO and record translation  
 *                        code + Cobol Copybook Translation
 *    
 *                 Author: Bruce Martin
 *    
 *                License: GPL 2.1 or later
 *                
 *    Copyright (c) 2016, Bruce Martin, All Rights Reserved.
 *   
 *    This library is free software; you can redistribute it and/or
 *    modify it under the terms of the GNU General Public License
 *    as published by the Free Software Foundation; either
 *    version 2.1 of the License, or (at your option) any later version.
 *   
 *    This library is distributed in the hope that it will be useful,
 *    but WITHOUT ANY WARRANTY; without even the implied warranty of
 *    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *    GNU General Public License for more details.
 *
 * ------------------------------------------------------------------------ */
      
package net.sf.JRecord.zTest.Parser;

import java.util.List;

import junit.framework.TestCase;
import net.sf.JRecord.CsvParser.ICsvDefinition;
import net.sf.JRecord.CsvParser.ICsvCharLineParser;

public class CommonCsvTests {

	public static void tstGetFieldList(String id, String[] lines, ICsvCharLineParser parser, ICsvDefinition csvDefinition, int fieldCount) {
		System.out.println(id);
		for (String s : lines) {
			List<String> flds = parser.getFieldList(s, csvDefinition);
			TestCase.assertEquals(id + " check counts: " + s, fieldCount, flds.size());
			for (int i = 0; i < flds.size(); i++) {
				TestCase.assertEquals(id + " Check: " + s + ", fieldNo=" + i, 
						parser.getField(i, s, csvDefinition), flds.get(i) );
			}
		}
	}
	

	public static void tstSetFieldList(String id, String[] lines, ICsvCharLineParser parser, ICsvDefinition csvDefinition, int fieldCount) {
		tstSetFieldList(id, lines, lines.length, parser, csvDefinition, fieldCount);
	}
	

	public static void tstSetFieldList(String id, String[] lines, int num, ICsvCharLineParser parser, ICsvDefinition csvDefinition, int fieldCount) {
		System.out.println(id);
		for (int i = 0; i < num; i++) {
			String s = lines[i];
			List<String> flds = parser.getFieldList(s, csvDefinition);
			TestCase.assertEquals(id + " check counts", fieldCount, flds.size());
			TestCase.assertEquals(id + " check line: ", s, parser.formatFieldList(flds, csvDefinition, null));
		}
	}

	
	
	public static String toHex(char c) {
		StringBuilder b = new StringBuilder(5).append("x'");
		String s = Integer.toHexString(c);
		if (s.length() == 1) {
			b.append('0');
		}
		return b.append(s).append('\'').toString();
	}

}
