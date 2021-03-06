/*
 * @Author Bruce Martin
 * Created on 8/01/2007
 *
 * Purpose:
 * File & layout details used by all the wizard screens
 *
 * Changes
 * # Version 0.61b Bruce Martin 2007/05/05
 *  - Changes o support user selecting the default type
 *
 */
package net.sf.RecordEditor.layoutWizard;

import java.io.IOException;
import java.util.ArrayList;

import net.sf.JRecord.Common.Conversion;
import net.sf.JRecord.Common.RecordException;
import net.sf.JRecord.Details.LayoutDetail;
import net.sf.JRecord.Details.RecordDetail;
import net.sf.JRecord.External.ExternalRecord;
import net.sf.JRecord.External.Def.ExternalField;
import net.sf.JRecord.IO.AbstractLineReader;
import net.sf.JRecord.IO.LineIOProvider;
import net.sf.JRecord.Types.Type;
import net.sf.RecordEditor.utils.common.Common;


/**
 * File & layout details used by all the wizard screens
 *
 * @author Bruce Martin
 *
 */
public class Details {
	public static final int RT_FIXED_LENGTH_FIELDS = 0;
	public static final int RT_DELIMITERED_FIELDS  = 1;
	public static final int RT_MULTIPLE_RECORDS  = 2;

    //private final static Integer CHAR_TYPE = new Integer(Type.ftChar);
	public  String filename         = "";
    public     int fileStructure    = 0;
    public     int recordType       = 0;
    public     int system           = 0;
    public     int recordLength     = 0;
    public  String layoutName       = "Wizard_";
    public  String layoutDescription = "";
    public  String fontName         = "";
    public Integer defaultType      = KeyField.CHAR_TYPE;
    public  String fieldSeperator   = "";
    public  String actualSeperator  = "";
    public  String quote            = "";
    public  String actualQuote      = "";
    public     int parserType       = 0;
    public boolean fieldNamesOnLine = false;
    public boolean embeddedCr       = false;
    public boolean unicode		    = false;
    public boolean generateFieldNames = false;
    public boolean editFile         = true;

    public  String layoutDirectory  = "";
    public     int layoutWriterIdx  = -1;

    //protected     int numRecords = 0;
    //protected byte[][] records = new byte[30][];

    //protected ColumnList columnDtls = new ColumnList();
    //protected ArrayList<ColumnDetails> columnDtls = new ArrayList<ColumnDetails>();
    public RecordDefinition standardRecord = new RecordDefinition();

    public ArrayList<RecordDefinition> recordDtls = new ArrayList<RecordDefinition>();
    public ArrayList<RecordDefinition> recordDtlsFull = new ArrayList<RecordDefinition>();

//    protected String keyName = "Record_Type";
//    protected int keyStart = 0;
//    protected int keyLength = 0;
    public int textPct = 100;
//    protected Integer keyType = KeyField.CHAR_TYPE;

    public ArrayList<KeyField> keyFields = new ArrayList<KeyField>();

    public Details() {
    	KeyField k = new KeyField();
    	k.keyName = "Record_Type";
    	keyFields.add(k);
    }

    public KeyField getMainKey() {
    	if (keyFields.size() == 0) {
    		keyFields.add(new KeyField("Record_Type", 0, 0, defaultType));
    	}
    	return keyFields.get(0);
    }

    public final ExternalRecord createRecordLayout() {
     	ExternalRecord rec;

    	switch (recordType) {
    	case (Details.RT_FIXED_LENGTH_FIELDS) :
    		rec = new ExternalRecord(-1, layoutName,
    				layoutDescription,
    				Common.rtRecordLayout, system, "Y", "",
    				"<Tab>", "", 0, Common.DEFAULT_STRING,
    				Common.CRLF_BYTES, fontName,
    				parserType, fileStructure,
    				false
    		);
    		nameFields(rec, standardRecord);
    		addFields(rec, standardRecord);
    	break;
    	case (Details.RT_MULTIPLE_RECORDS):
    		ExternalRecord childRecord;

    		rec = new ExternalRecord(-1, layoutName,
    				layoutDescription,
    				Common.rtGroupOfRecords, system, "Y", "",
    				"<Tab>", "", 0, Common.DEFAULT_STRING,
    				Common.CRLF_BYTES, fontName,
    				parserType, fileStructure,
    				false
    		);
	 		String value;
    		for (RecordDefinition child : recordDtls) {
    			if (child.include) {
	    			childRecord = new ExternalRecord(-1, child.name,
	        				"",
	        				Common.rtRecordLayout, system, "N", "",
	        				"<Tab>", "", 0, Common.DEFAULT_STRING,
	        				Common.CRLF_BYTES, fontName,
	        				parserType, fileStructure,
	        				false
	        		);

	    			nameFields(childRecord, child);
	    			childRecord.setDefaultRecord(child.defaultRec.booleanValue());
	    			System.out.println("Record: " + child.name + "\t" + childRecord.isDefaultRecord());
	    			for (int i = 0; i < keyFields.size(); i++) {
		    			if (child.getKeyValue()[i] != null) {
		    				value = child.getKeyValue()[i].toString();
		    				childRecord.addTstField(keyFields.get(i).keyName, value);
		    			}
	    			}
	    			addFields(childRecord, child);
	    			childRecord.setNew(true);

	    			rec.addRecord(childRecord);
    			}
    		}
    	break;
    	default:
    		String delim = fieldSeperator;

	    	if ("<Default>".equalsIgnoreCase(delim)) {
	    		delim = actualSeperator;
	    	}

	    	delim = Conversion.encodeCharStr(delim);
	    	rec = new ExternalRecord(-1, layoutName,
	    			layoutDescription,
	    			Common.rtDelimited, system, "Y", "",
	    			delim, actualQuote, 0,
	    			Common.DEFAULT_STRING,
	    			Common.CRLF_BYTES, fontName,
	    			parserType, fileStructure,
	    			false
	    	);
	    	nameFields(rec, standardRecord);
	    	addFields(rec, standardRecord);
    	}

    	rec.setNew(true);
    	return rec;
    }

    /**
     * Add Fields to a external record definition
     * @param rec external record
     * @param recordDef Wizard Record
     */
    private void addFields(ExternalRecord rec, RecordDefinition recordDef) {
       	int i;
    	ColumnDetails column;
    	ExternalField field;

    	for (i = 0; i < recordDef.columnDtls.size(); i++) {
    		column = recordDef.columnDtls.get(i);

    		if (column.include) {
    			field = new ExternalField(
    					column.start,
    					column.length,
    					column.name,
    					"",
    					column.type,
    					column.decimal,
    					Common.FORMAT_DEFAULT,
    					"",
    					"",
    					"",
    					i
    			);

    			rec.addRecordField(field);
    		}
    	}
    }

    private void nameFields(ExternalRecord rec, RecordDefinition recordDef) {
     	ColumnDetails column;

    	for (int i = 0; i < recordDef.columnDtls.size(); i++) {
    		column = recordDef.columnDtls.get(i);

			if (column.name == null || "".equals(column.name)) {
				column.name = "Field_" + i;
			}
    	}
    }


    /**
     * Get a line Reader
     * @return requested line reader
     *
     * @throws RecordException any RecordEditor Exceptions that occur
     * @throws IOException any IO Errors
     */
    @SuppressWarnings("unchecked")
	public AbstractLineReader<LayoutDetail> getReader() throws RecordException, IOException {
        AbstractLineReader<LayoutDetail> reader = LineIOProvider.getInstance().getLineReader(fileStructure);
        LayoutDetail emptyLayout;
        RecordDetail[] recs;


        if (fileStructure == Common.IO_FIXED_LENGTH) {
            RecordDetail.FieldDetails[] field = new RecordDetail.FieldDetails[1];

            field[0] = new RecordDetail.FieldDetails("", "", Type.ftChar, 0, "",  0, "");
            field[0].setPosLen(1, recordLength);
            recs = new RecordDetail[1];
            recs[0] = new RecordDetail(
                    	"", "", "", Common.rtRecordLayout, "", "", "", field, parserType, 0
                    );
        } else {
            recs = new RecordDetail[0];
        }
        emptyLayout = new LayoutDetail("", recs, "",
                fileStructure,
                null, "", fontName, null,
                fileStructure, -1
        );

        reader.open(filename, emptyLayout);
        return reader;
    }

    public void setFieldSearch() {
    	standardRecord.searchForFields = true;

    	if (recordDtls != null) {
    		for (int i = 0; i<recordDtls.size(); i++) {
    			recordDtls.get(i).searchForFields = true;
    		}
    	}
    }
    
    public String getFileDataAsString() {
    	int numRecords = Math.min(200, standardRecord.numRecords);
		StringBuilder b = new StringBuilder(numRecords * 40);
		String sep = "";
    	for (int i = 0; i < numRecords; i++) {
    		b.append(sep).append(Conversion.toString(standardRecord.records[i], fontName));
    		sep = "\n";
    	}
    	
    	return b.toString();
    }
}
