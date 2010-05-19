/*
 * Changes
 *
 * # Version 0.61 Bruce Martin 2007/04/14
 *   - Changed to store values in a ExternalRecord variable
 *     rather than local class variables
 */
package net.sf.RecordEditor.layoutEd.Record;

import net.sf.JRecord.Common.Constants;
import net.sf.JRecord.External.ExternalRecord;
import net.sf.RecordEditor.utils.common.Common;
import net.sf.RecordEditor.utils.jdbc.AbsRecord;

/**
 *   This class holds the fields extracted from a SQL statement:
 *
 *   <pre>
 *       Select
 *              RecordId,
 *              RecordName,
 *              Description,
 *              RecordType,
 *              System,
 *              ListChar,
 *              CopyBook,
 *              Delimiter,
 *              Quote,
 *              PosRecInd,
 *              RecSepList,
 *              RecordSep,
 *              Canonical_Name,
 *              Record_Style recordStyle,
 *              File_Structure fileStructure
 *       From Tbl_R_Records
 *
 *   </pre>
 * This class also provides both specific field access methods
 * and Generic (based on Field number) access
 *
 * @Author Generated by BuildJava.Rexx by Bruce Martin
 *
 */
public class RecordRec extends AbsRecord {

  public static int BF_NOT_DEFINED = 0; 
  public static int BF_NO_BINARY_FIELDS = 1; 
  public static int BF_BINARY_FIELDS = 2; 
  
  private ExternalRecord value;

  private int initRecordId;
  
  private int binaryFields = BF_NOT_DEFINED;


  /**
   * Create External Record Definition
   *
   */
  public RecordRec () {
      super();

      value = new ExternalRecord();
      setExternalValue(value);

      setKeys();
  }

  public RecordRec (
                    final int pRecordId
                  , final String pRecordName
                  , final String pDescription
                  , final int pRecordType
                  , final int pSystem
                  , final String pListChar
                  , final String pCopyBook
                  , final String pDelimiter
                  , final String pQuote
                  , final int pPosRecInd
                  , final String pRecSepList
                  , final byte[] pRecordSep
                  , final String pFontName
                  , final int precordStyle
                  , final int pfileStructure
                  ) {
      this(new ExternalRecord(
              pRecordId
              , pRecordName
              , pDescription
              , pRecordType
              , pSystem
              , pListChar
              , pCopyBook
              , pDelimiter
              , pQuote
              , pPosRecInd
              , pRecSepList
              , pRecordSep
              , pFontName
              , precordStyle
              , pfileStructure));
  }

  /**
   * Create DB record with external value
   * @param record external record details
   */
  public RecordRec(final ExternalRecord record) {
      super(false);

      value = record;
      setExternalValue(value);
      setNew(value.isNew());

      setKeys();
  }


  /**
   *  This method copies the key fields to the Init* fields
   */
  public void setKeys() {

      initRecordId = value.getRecordId();
  }

  /**
   *  This method returns clones the current record
   *
   *  @return a duplicate of the current record
   */
  public Object clone() {

      super.clone();

      RecordRec ret = new RecordRec(
                        value.fullClone()
                    );

      ret.setNew(true);

      return ret;
  }



  /**
   *  This method returns clones the current record
   * @return field count
   */
  public int getFieldCount() {
      return 15;
  }




  /**
   *  This method returns a field (specified by field number)
   *
   *  @param fieldNum the field number (in the record)
   *  @return the request field
   */
  public Object getField(int fieldNum) {

      if (updateStatus == NULL_INT_VALUE) return "";

      switch (fieldNum) {
        case (0) : return new Integer(value.getRecordId());
        case (1) : return value.getRecordName();
        case (2) : return value.getDescription();
        case (3) : return new Integer(value.getRecordType());
        case (4) : return new Integer(value.getSystem());
        case (5) : return value.getListChar();
        case (6) : return value.getCopyBook();
        case (7) : return value.getDelimiter();
        case (8) : return value.getQuote();
        case (9) : return new Integer(value.getPosRecInd());
        case (10) : return value.getRecSepList();
        case (11) : return value.getRecordSep();
        case (12) : return value.getFontName();
        case (13) : return new Integer(value.getRecordStyle());
        case (14) : return new Integer(value.getFileStructure());
        default  : return "";
      }
  }


  /**
   *  This method sets a field (specified by field number) with a string value
   *
   *  @param fieldNum the field number (in the record)
   *  @param val the value to be assigned to the field
   */
  protected void setFieldWithString(int fieldNum, String val) {

      switch (fieldNum) {
        case (0) : value.setRecordId(cnvToInt(value.getRecordId(), val, "Record Id" ));
        break;
        case (1) : value.setRecordName(val);
        break;
        case (2) : value.setDescription(val);
        break;
        case (3) : value.setRecordType(cnvToInt(value.getRecordType(), val, "Record Type" ));
        break;
        case (4) : value.setSystem(cnvToInt(value.getSystem(), val, "System" ));
        break;
        case (5) : value.setListChar(val);
        break;
        case (6) : value.setCopyBook(val);
        break;
        case (7) : value.setDelimiter(val);
        break;
        case (8) : value.setQuote(val);
        break;
        case (9) : value.setPosRecInd(cnvToInt(value.getPosRecInd(), val, "PosRecInd" ));
        break;
        case (10) : value.setRecSepList(val);
        break;
        case (11) : value.setRecordSep(val.getBytes());
        break;
        case (12) : value.setFontName(val);
        break;
        case (13) : value.setRecordStyle(cnvToInt(value.getRecordStyle(), val, "Record_Style" ));
        break;
        case (14) : value.setFileStructure(cnvToInt(value.getFileStructure(), val, "File_Structure" ));
        break;
        default  : ;
      }
  }


  /**
   *  This method sets a field (specified by field number) with an object value
   *
   *  @param fieldNum the field number (in the record)
   *  @param val the value to be assigned to the field
   */
  protected void setFieldWithObject(int fieldNum, Object val) {

      switch (fieldNum) {
        case (0) : value.setRecordId(((Integer) val).intValue());
        break;
        case (3) : value.setRecordType(((Integer) val).intValue());
        break;
        case (4) : value.setSystem(((Integer) val).intValue());
        break;
        case (9) : value.setPosRecInd(((Integer) val).intValue());
        break;
        case (11) : value.setRecordSep((byte[]) val);
        break;
        case (13) : value.setRecordStyle(((Integer) val).intValue());
        break;
        case (14) : value.setFileStructure(((Integer) val).intValue());
        break;
        default  : setFieldWithString(fieldNum, (String) val) ;
      }
  }

	/**
	 * Create a new record
	 * @param pRecordName name of the new record
	 * @param fontName fontname to use
	 *
	 * @return the new record
	 */
	public static final RecordRec getNullRecord(final String pRecordName,
			final String fontName) {

	    return getNullRecord(pRecordName, Common.rtRecordLayout, fontName);
	}


	/**
	 * Create a new record
	 * @param pRecordName name of the new record
	 * @param recordType record type for the record
	 * @param fontName fontname to use
	 *
	 * @return the new record
	 */
	public static final RecordRec getNullRecord(final String pRecordName,
	        									final int recordType,
	        									final String fontName) {

	    return new RecordRec(-1, pRecordName, "", recordType, 0, "N",
			"", "<Tab>", "", 0, Common.DEFAULT_STRING, Common.LFCR_BYTES, 
			fontName, 0, Constants.IO_DEFAULT);
	}

	/**
	 * @return Returns the initRecordId.
	 */
	public int getInitRecordId() {
	    return initRecordId;
	}

	/**
	 * @return Returns the value.
	 */
	public ExternalRecord getValue() {
	    return value;
	}


    /**
     * @return record identifier
     */
    public int getRecordId() {
        return value.getRecordId();
    }

    /**
     * @return record name
     */
    public String getRecordName() {
        return value.getRecordName();
    }

    /**
     * @return System
     */
    public int getSystem() {
        return value.getSystem();
    }

	/**
	 * @return the binaryFields
	 */
	public final int getBinaryFields() {
		return binaryFields;
	}

	/**
	 * @param binaryFields the binaryFields to set
	 */
	public final void setBinaryFields(int binaryFields) {
		this.binaryFields = binaryFields;
	}
}
