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
      
package net.sf.JRecord.IO;

import java.io.IOException;
import java.io.InputStream;
import java.util.List;

import net.sf.JRecord.ByteIO.ByteTextReader;
import net.sf.JRecord.ByteIO.IByteReader;
import net.sf.JRecord.Common.Constants;
import net.sf.JRecord.Common.RecordException;
import net.sf.JRecord.CsvParser.CsvDefinition;
import net.sf.JRecord.CsvParser.ICsvByteLineParser;
import net.sf.JRecord.CsvParser.ICsvDefinition;
import net.sf.JRecord.CsvParser.CsvParserManagerByte;
import net.sf.JRecord.Details.AbstractLayoutDetails;
import net.sf.JRecord.Details.AbstractRecordDetail;
import net.sf.JRecord.Details.LayoutDetail;
import net.sf.JRecord.Details.LineProvider;
import net.sf.JRecord.Details.RecordDetail;
import net.sf.JRecord.Types.Type;
import net.sf.JRecord.detailsBasic.CsvCharDetails;

/**
 * This class will read and AbstractLine from a standard Windows/*nix Text file. It is similar in function
 * to <b>TextLineReader</b>, the difference being <b>TextLineReader</b> uses Standard BufferedReader
 * (String based) Class to the reading and can not handle Hex (i.e. x'FF') values correctly, while this class
 * uses streams and is able to handle Hex values. This class is based on <b>ByteTextReader</b>.
 * <p>This class was written to support hex field (x'FF') separators in csv (delimited) files.
 *
 * @see TextLineReader
 * @see ByteTextReader
 *
 * @author Bruce Martin
 * @version 0.68
 *
 */
public class BinTextReader extends LineReaderWrapper {

	private String defaultQuote  = "'";
	private boolean readNames;

	public BinTextReader(LineProvider provider, boolean nameOn1stLine) {
		this(provider, nameOn1stLine, new ByteTextReader());
	}

	public BinTextReader(LineProvider provider, boolean nameOn1stLine, IByteReader reader) {
		super(provider, reader);

		readNames = nameOn1stLine;
	}

	   /**
     * @see net.sf.JRecord.IO.StandardLineReader#open(java.io.InputStream, net.sf.JRecord.Details.LayoutDetail)
     */ @Override
    public void open(InputStream inputStream, AbstractLayoutDetails layout)
    throws IOException, RecordException {

        super.open(inputStream, layout);

		if (readNames) {
			if ((layout instanceof LayoutDetail)
			&& ((LayoutDetail) layout).useThisLayout()) {
				super.rawRead();
			} else {
				createLayout(super.rawRead());
			}
		}
    }


    /**
     * create a layout
     *
     * @param pReader file read
     *
     * @throws IOException sny IO error that occurs
     */
    protected void createLayout(byte[] line) throws IOException, RecordException {
        LayoutDetail layout;

        AbstractRecordDetail rec = null;
        boolean binCsv = false;
	    int fieldType = Type.ftChar;
        int decimal   = 0;
        int format    = 0;
        int parser    = 0;
        int structure = Constants.IO_NAME_1ST_LINE;
        String param  = "";
        String font   = "";
        byte[] recordSep = Constants.SYSTEM_EOL_BYTES;
        boolean embeddedCr = false;
        CsvCharDetails delim  = CsvCharDetails.newDelimDefinition("<tab>", font);
        //String delimStr = "x'00'";
        CsvCharDetails quote  = CsvCharDetails.newQuoteDefinition(defaultQuote, font);

	    try {
	    	AbstractLayoutDetails suppliedLayout = getLayout();
			int ts = suppliedLayout.getFileStructure();
	    	if (ts != Constants.IO_GENERIC_CSV) {
	    		structure = ts;
	    	}
	    	delim     = suppliedLayout.getDelimiterDetails();
	    	//delimStr  = suppliedLayout.getDelimiter();
	        rec = suppliedLayout.getRecord(0);
	        binCsv = suppliedLayout.isBinCSV();
	        quote     = rec.getQuoteDefinition();
	        parser    = rec.getRecordStyle();
	        fieldType = rec.getField(0).getType();
	        decimal   = rec.getField(0).getDecimal();
	        format    = rec.getField(0).getFormat();
	        param     = rec.getField(0).getParamater();
	        recordSep = suppliedLayout.getRecordSep();
	        font      = suppliedLayout.getFontName();

	        if (recordSep == Constants.SYSTEM_EOL_BYTES) {
	        	recordSep = null;
	        }

	        if (rec instanceof RecordDetail) {
	        	embeddedCr = ((RecordDetail) rec).isEmbeddedNewLine();
	        }
	    } catch (Exception e) {
        }

	    //System.out.println(" Quote  ->" + quote + " " + (getLayout() == null));

	    layout = createLayout(line, rec, binCsv,
	    		recordSep, font,  delim, 
                parser, fieldType, decimal, format,
                param, quote, structure, embeddedCr);
	    //System.out.println(" Quote  ->");

	    if (layout != null) {
	        setLayout(layout);
	    }
    }

    /**
     * create a Layout from the first line in the file
     * @param line line being built
     * @param recordSep record seperator
     * @param fontName font name
     * @param delimiter field delitmiier
     * @param delimStr field delitmiier as a string
     * @param parser Identifier of the CSV parser to use
     * @param fieldType field type
     * @param decimal number of decimal places
     * @param format format to use
     * @param param param to add to each field
     * @param quote Quote
     * @param Structure file structure
     * @return Create a Layout description form a supplied line (first line of a file ?)
     * + other details
     * @throws IOException any error
     */
    public static LayoutDetail createLayout(byte[] line, AbstractRecordDetail rec,
    		boolean binCsv, byte[] recordSep,
            String fontName, CsvCharDetails delimiter, int parser,
            int fieldType, int decimal, int format, String param,
            CsvCharDetails quote, int structure, boolean embeddedCr) throws IOException {

        int i;
        LayoutDetail ret = null;
        String s;

        if (line != null) {
            //RecordDetail rec = getLayout().getRecord(0);
        	
        	int len;
            RecordDetail.FieldDetails[] flds;
            RecordDetail[] recs;

            if (fieldType < 0) {
                fieldType = Type.ftChar;
            }

            ICsvDefinition csvDef;

        	if (rec instanceof ICsvDefinition) {
        		csvDef = (ICsvDefinition) rec;
        	} else {
        		csvDef = new CsvDefinition(delimiter, quote, false);
        	}
        	
        	List<String> fieldList;
          	ICsvByteLineParser csvParser = CsvParserManagerByte.getInstance().get(parser, binCsv);
        	fieldList = csvParser.getFieldList(line, csvDef);
//            if (binCsv) {
////	        	BinaryCsvParser csvPaser = new BinaryCsvParser(delimiter.asByte());
////	            //String fontName = fontname;
////	            len = csvPaser.countTokens(line);
////	            flds = new RecordDetail.FieldDetails[len];
////	            recs = new RecordDetail[1];
////		
////	            for (i = 0; i < len; i++) {
////	                s = csvPaser.getValue(line, i+1, fontName);
////	                flds[i] = createField(rec, fontName, fieldType, decimal, format, param, s);
////	                flds[i].setPosOnly(i + 1);
////	            }
//              	ICsvByteLineParser csvParser = CsvParserManagerByte.getInstance().get(parser);
//            	fieldList = csvParser.getFieldList(line, csvDef);
//            } else {;
//              	ICsvCharLineParser csvParser = CsvParserManagerChar.getInstance().get(parser);
//            	fieldList = csvParser.getFieldList(Conversion.toString(line, fontName), csvDef);
//            }
        	len = fieldList.size();
            flds = new RecordDetail.FieldDetails[len];
            recs = new RecordDetail[1];
            for (i = 0; i < len; i++) {
                flds[i] = createField(rec, fontName, fieldType, decimal, format, param, fieldList.get(i));
                flds[i].setPosOnly(i + 1);
            }

            recs[0] = new RecordDetail("", "", "", Constants.rtDelimited,
            		delimiter.jrDefinition(), quote.jrDefinition(), fontName, flds, parser, 0, embeddedCr);

            try {
                ret =
                    new LayoutDetail("", recs, "",
                        Constants.rtDelimited,
                        recordSep, "", fontName, null,
                        structure
                    );
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
        return ret;
    }

	protected static RecordDetail.FieldDetails createField(AbstractRecordDetail rec, String fontName, int fieldType,
			int decimal, int format, String param, String s) {
		int fldType;
		int idx;
		RecordDetail.FieldDetails f;
		fldType = fieldType;
		if (rec != null
		&& (idx = rec.getFieldIndex(s)) >= 0) {
			fldType = rec.getField(idx).getType();
		}
		f = new RecordDetail.FieldDetails(s, s, fldType, decimal,
		        fontName, format, param);
		return f;
	}

}
