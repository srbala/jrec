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
      
package net.sf.JRecord.zExamples;

import net.sf.JRecord.Common.Constants;
import net.sf.JRecord.Details.AbstractLine;
import net.sf.JRecord.Details.LayoutDetail;
import net.sf.JRecord.Details.Line;
import net.sf.JRecord.External.CopybookLoader;
import net.sf.JRecord.External.ExternalRecord;
import net.sf.JRecord.External.RecordEditorXmlLoader;
import net.sf.JRecord.IO.AbstractLineWriter;
import net.sf.JRecord.IO.LineIOProvider;
import net.sf.JRecord.zTest.Common.TstConstants;

/**
 * Example of writing a File using a RecordEditor - XML copybook
 * definition
 *
 * @author Bruce Martin
 *
 */
public final class XmplLineIO8 {


	    /**
	     * Example of
	     * 1) Loading an XML copybook (RecordEditor-Xml) - External Record
	     * 3) LineWrite classes
	     */
	    private XmplLineIO8() {
	        super();

		    String installDir     = TstConstants.SAMPLE_DIRECTORY;
		    String salesFileOut   = installDir + "DTAR020out8.bin";
		    String copybookName   = TstConstants.RECORD_EDITOR_XML_DIRECTORY
	    					+ "DTAR020.Xml";
	        int lineNum = 0;

	        try {
	            int fileStructure = Constants.IO_FIXED_LENGTH;
	            CopybookLoader loader = new RecordEditorXmlLoader();
	            ExternalRecord extlayout = loader.loadCopyBook(copybookName, 0, 0, "", 0, 0, null);
	            /*
	             * Converting from the interchange (ExternalRecord) format to LayoutDetail
	             */
	            LayoutDetail layout = extlayout.asLayoutDetail();
	            AbstractLine saleRecord = new Line(layout);
	            AbstractLineWriter writer  = LineIOProvider.getInstance().getLineWriter(fileStructure);

	            writer.open(salesFileOut);

	            saleRecord.getFieldValue("KEYCODE-NO").set(1331);
	            saleRecord.getFieldValue("STORE-NO").set(1);
	            saleRecord.getFieldValue("DATE").set(80921);
	            saleRecord.getFieldValue("DEPT-NO").set(100);
	            saleRecord.getFieldValue("QTY-SOLD").set(7);
	            saleRecord.getFieldValue("SALE-PRICE").set(7.00);
	            writer.write(saleRecord);

	            saleRecord.getFieldValue("STORE-NO").set(11);
	            writer.write(saleRecord);

	            saleRecord.getFieldValue("STORE-NO").set(121);
	            writer.write(saleRecord);

	            System.out.println(" " + saleRecord.getFieldValue("SALE-PRICE").asString());
	            writer.close();
	        } catch (Exception e) {
	            System.out.println("~~> " + lineNum + " " + e.getMessage());
	            System.out.println();

	            e.printStackTrace();
	        }
	    }

	    public static void main(String[] args) {
	    	new XmplLineIO8();
	    }
}
