package net.sf.RecordEditor.layoutEd.Record;

import net.sf.RecordEditor.utils.jdbc.AbsRecord;

/**
 *   This class holds the fields extracted from a SQL statement:
 *
 *   <pre>
 *       Select
 *              ChildRecord,
 *              FieldStart as Start,
 *              Field,
 *              FieldValue
 *       from Tbl_RS_SubRecords
 *       where RecordId = ?
 *
 *   </pre>
 * This class also provides both specific field access methods
 * and Generic (based on Field number) access
 *
 * @Author Generated by BuildJava.Rexx by Bruce Martin
 *
 */
public class ChildRecordsRec extends AbsRecord {

  private int ChildRecord;
  protected int initChildRecord ;
  private int Start;
  private String Field;
  private String FieldValue;
  private int parentRecord;



  public ChildRecordsRec () {
      super();

      ChildRecord = 0;
      Start = 0;
      Field = "";
      FieldValue = "";

      setKeys();
  }

  public ChildRecordsRec (
                    int pChildRecord
                  , int pStart
                  , String pField
                  , String pFieldValue
                  , int pParentRecord
                  ) {
      super(false);

      ChildRecord = pChildRecord;
      Start = pStart;
      Field = pField;
      FieldValue = pFieldValue;
      parentRecord = pParentRecord;

      setKeys();
  }


  /**
   *  This method copies the key fields to the Init* fields
   */
  public void setKeys() {

      initChildRecord = ChildRecord;
  }
  


  /**
   * @see net.sf.RecordEditor.utils.jdbc.AbsRecord#hasTheKeyChanged()
   */
  @Override
  public boolean hasTheKeyChanged() {
	  return initChildRecord != ChildRecord;
  }

  
/**
   *  This method returns clones the current record
   *
   *  @return a duplicate of the current record
   */
  public Object clone() {

      super.clone();

      ChildRecordsRec ret = new ChildRecordsRec(
                        ChildRecord
                      , Start
                      , Field
                      , FieldValue
                      , parentRecord
                    );

      ret.setNew(true);

      return ret;
  }



  /**
   *  This method returns clones the current record
   */
  public int getFieldCount() {
      return 5;
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
        case (0) : return new Integer(ChildRecord);
        case (1) : return new Integer(Start);
        case (2) : return Field;
        case (3) : return FieldValue;
        case (4) : return new Integer(parentRecord);
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
        case (0) : setChildRecord(cnvToInt(ChildRecord, val, "Child Record" ));
        break;
        case (1) : setStart(cnvToInt(Start, val, "Field Start" ));
        break;
        case (2) : setField(val);
        break;
        case (3) : setFieldValue(val);
        break;
        case (4) : setParentRecord(cnvToInt(parentRecord, val, "Parent Record" ));
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
        case (0) : setChildRecord(((Integer) val).intValue());
        break;
        case (1) : setStart(((Integer) val).intValue());
        break;
        case (4) : setParentRecord(((Integer) val).intValue());
        break;
        default  : setFieldWithString(fieldNum, (String) val) ;
      }
  }

  /**
   *  This method gets the vaule of ChildRecord
   */
  public int getChildRecord() {
      return ChildRecord;
  }

  /**
   *  This method sets the vaule of ChildRecord
   *
   * @param val value to be assigned to ChildRecord
   */
  public void setChildRecord(int val) {

      if ((val != ChildRecord) || (updateStatus == NULL_INT_VALUE)) {
           ChildRecord = val;
           updateStatus = UPDATED;
      }
  }

  /**
   *  This method gets the vaule of Start
   */
  public int getStart() {
      return Start;
  }

  /**
   *  This method sets the vaule of Start
   *
   * @param val value to be assigned to Start
   */
  public void setStart(int val) {

      if ((val != Start) || (updateStatus == NULL_INT_VALUE)) {
           Start = val;
           updateStatus = UPDATED;
      }
  }

  /**
   *  This method gets the vaule of Field
   */
  public String getField() {
      return Field;
  }

  /**
   *  This method sets the vaule of Field
   *
   * @param val value to be assigned to Field
   */
  public void setField(String val) {

      if ((val == null || "".equals(val))
      && (Field == null || "".equals(Field))) {
          return;
      }

      if ((val == null) || (! val.equals(Field)) || (updateStatus == NULL_INT_VALUE)) {
           Field = val;
           updateStatus = UPDATED;
      }
  }

  /**
   *  This method gets the vaule of FieldValue
   */
  public String getFieldValue() {
      return FieldValue;
  }

  /**
   *  This method sets the vaule of FieldValue
   *
   * @param val value to be assigned to FieldValue
   */
  public void setFieldValue(String val) {

      if ((val == null || "".equals(val))
      && (FieldValue == null || "".equals(FieldValue))) {
          return;
      }

      if ((val == null) || (! val.equals(FieldValue)) || (updateStatus == NULL_INT_VALUE)) {
           FieldValue = val;
           updateStatus = UPDATED;
      }
  }

  /**
   * @return the parentRecord
   */
  public int getParentRecord() {
	  return parentRecord;
  }

  /**
   * @param parentRecord the parentRecord to set
   */
  public void setParentRecord(int parentRecord) {
	  
	  if (this.parentRecord != parentRecord) {
		  this.parentRecord = parentRecord;
		  updateStatus = UPDATED;
	  }
  }

}
